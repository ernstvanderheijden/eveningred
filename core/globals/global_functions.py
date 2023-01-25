import json
import locale

from dateutil.relativedelta import relativedelta

from configuration.models import Configuration
from datetime import timedelta, datetime
from django.core.exceptions import ValidationError
from django.apps import apps
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from pydoc import locate
from shared.variables.view_variables import set_user_variables
from urllib import parse
from users.models import User


def check_session_variables(request):
    """ If not already done, set the request session variables"""
    if 'variables_loaded' in request.session:
        if not request.session['variables_loaded']:
            set_user_variables(request)
    else:
        set_user_variables(request)


def set_rights_for_module(request, rights_crud):
    list_rights_crud = {"read": False, "write": False}
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        for rights in rights_crud:
            if getattr(user, rights['read']):
                list_rights_crud.update({"read": True})
            if getattr(user, rights['write']):
                list_rights_crud.update({"write": True})
    # return list_rights_crud
    return {"read": True, "write": True}


def get_model_from_fragment(request):
    package = request.GET.get('package', '')
    fragment = request.GET.get('fragment', '')
    modulepath = 'shared.packages.' + package.lower() + '.fragments.' + fragment
    modelname = getattr(locate(modulepath), 'modelname')
    return apps.get_model(package.lower(), modelname)


def set_pagination(request, records, page, paginate, paginatesize, paginatesize_overwrite=''):
    configuration = Configuration.default.get()
    if not paginate:
        return []
    if request.GET.get('page', ''):
        page = int(request.GET.get('page', 1))
    if paginatesize_overwrite:
        paginator = Paginator(records, paginatesize_overwrite)
    else:
        paginator = Paginator(records, paginatesize)
    # If the requested pagenumber is bigger then the existing, set the page to the last existing page
    if paginator.num_pages < page:
        page = paginator.num_pages
    page_elided = paginator.get_elided_page_range(page, on_each_side=configuration.on_each_side, on_ends=configuration.on_ends)
    page_ellipsis = paginator.ELLIPSIS
    records = paginator.get_page(page)
    return [paginator, page, records, page_elided, page_ellipsis]


def is_ajax_request(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return True
    else:
        return False


def set_ajax_variables(request, ctx, data, context, templatename):
    empty_form = False
    if 'form' in context:
        if context['form'] == "empty_form":
            empty_form = True

    if empty_form:
        data['messagelist'] = ["Onvoldoende rechten", "warning", "long"]
        data['form_is_valid'] = False
    else:
        if 'level' in ctx:
            data['level'] = ctx['level']
        if 'fragment' in ctx:
            data['fragment'] = ctx['fragment']
        if 'modalsize' in ctx:
            data['modalsize'] = ctx['modalsize']
        if 'url' in ctx:
            data['url'] = ctx['url']
        if 'html_header' in ctx:
            data['html_header'] = render_to_string(ctx['html_header'], context, request=request)
        if templatename:
            data['html_body'] = render_to_string(templatename, context, request=request)
        if 'templatename' in ctx:
            data['html_body'] = render_to_string(ctx['templatename'], context, request=request)
        if 'html_footer' in ctx:
            data['html_footer'] = render_to_string(ctx['html_footer'], context, request=request)
        data['form_is_valid'] = True


def prepare_message(request, ctx, data, messages):
    if 'messagelist' in ctx:
        if "core/template" in data['successurl']:
            if type(ctx['messagelist']) == list:
                match ctx['messagelist'][1]:
                    case "success":
                        messages.success(request, ctx['messagelist'][0])
                    case "error":
                        messages.error(request, ctx['messagelist'][0])
                    case _:
                        messages.success(request, ctx['messagelist'][0])
            else:
                messages.success(request, ctx['messagelist'])
        else:
            data['messagelist'] = ctx['messagelist']
    return [ctx, data, messages]


def set_url(request):
    url_path = request.path
    url_get = ''
    for rg, data in request.GET.items():
        if url_get:
            url_get = url_get + "&" + rg + "=" + data
        else:
            url_get = "?" + rg + "=" + data
    url = url_path + url_get
    return url


def create_ctx_slug(ctx):
    """ This slug is used to call the ctx modal with context data from where you are at that specific moment"""
    temp_ctx = dict()
    for key, keydata in ctx.items():
        temp_ctx.update({key: str(keydata)})
    if 'fragment' in temp_ctx:
        del temp_ctx['fragment']
    if 'fragments' in temp_ctx:
        del temp_ctx['fragments']
    ctx['slug'] = encode_string(temp_ctx)
    return ctx


def save_paginatesize(request):
    data = dict()
    fldname = 'paginatesize'
    paginatesize = 5
    user = User.objects.get(id=request.user.id)
    if request.GET.get('paginatesize', ''):
        paginatesize = int(request.GET.get('paginatesize'))
        fldname = 'paginatesize'
    elif request.GET.get('paginatesize_modal', ''):
        paginatesize = int(request.GET.get('paginatesize_modal'))
        fldname = 'paginatesize_modal'
    if paginatesize != 5 and paginatesize != 10 and paginatesize != 25 and paginatesize != 50 and paginatesize != 100 and not request.user.is_superuser:
        paginatesize = 5

    user.__dict__[fldname] = paginatesize
    user.save()
    set_user_variables(request)
    data['level'] = request.GET.get('level')
    data['form_is_valid'] = True
    return JsonResponse(data)


def encode_string(a_string):
    return urlsafe_base64_encode(force_bytes(json.dumps(a_string, indent=4, sort_keys=True)))


def decode_string(a_string):
    return json.loads(urlsafe_base64_decode(a_string))


def put_variables_in_ctx(self):
    ctx = vars(self)
    return ctx


def set_strfilter_and_strorderby(request, searchresult, order_by):
    strfilter = dict()
    str_order_by_operator = ''
    if 'order_by' not in searchresult:
        searchresult['order_by'] = order_by
    searchresult['filterfieldvalue'] = dict()
    searchresult['filter'] = request.GET.get('filter', '')
    if "filter" in searchresult:
        if searchresult['filter']:
            for filterpart in searchresult['filter'].split(";"):
                filteritems = filterpart.split("~~")
                if filteritems[2] and filteritems[0] != 'order_by':
                    # if "^" in filteritems[0]:
                    #     strfilter.update({filteritems[0].split("^")[2] + filteritems[1]: filteritems[2]})
                    #     searchresult['filterfieldvalue'].update({filteritems[0].split("_")[2]: filteritems[2]})
                    # else:
                    strfilter.update({filteritems[0] + filteritems[1]: filteritems[2]})
                    searchresult['filterfieldvalue'].update({filteritems[0]: filteritems[2]})
                elif filteritems[0] == 'order_by':
                    if filteritems[2]:
                        if filteritems[1] == 'asc':
                            str_order_by_operator = '-'
                        searchresult['order_by'] = str_order_by_operator + filteritems[2]
    searchresult['filter'] = strfilter
    return searchresult


def use_filter(request, records, order_by):
    searchresult = dict()
    searchresult['records'] = records
    searchresult = set_strfilter_and_strorderby(request, searchresult, order_by)
    if searchresult['filter']:
        searchresult['records'] = searchresult['records'].filter(**searchresult['filter'])
    if searchresult['order_by'] and searchresult['order_by'] != "-":
        searchresult['records'] = searchresult['records'].order_by(searchresult['order_by'])
    return searchresult


def set_ctx_records_filter_ordering_paginate(request, ctx):
    searchresult = use_filter(request, ctx['records'], ctx['order_by'])
    ctx['records'] = searchresult['records']
    ctx['filter'] = searchresult['filter']
    ctx['filterfieldvalue'] = searchresult['filterfieldvalue']
    if searchresult['order_by']:
        ctx['order_by'] = searchresult['order_by']

    if 'paginate' in ctx:
        if ctx['paginate']:
            ctx['paginatesize'] = request.user.paginatesize
            paginatelist = set_pagination(request,
                                          ctx['records'],
                                          ctx['page'],
                                          ctx['paginate'],
                                          ctx['paginatesize'],
                                          ctx['paginatesize_overwrite'])  # [paginator, page, records, page_elided, page_ellipsis]
            ctx['paginator'] = paginatelist[0]
            ctx['records'] = paginatelist[2]
            ctx['elided'] = paginatelist[3]
            ctx['ellipsis'] = paginatelist[4]
    return ctx


def clean_fields(self, exclude=None):
    """
    Cleans all fields and raises a ValidationError containing message_dict
    of all validation errors if any occur.
    """
    if exclude is None:
        exclude = []

    errors = {}
    for f in self._meta.fields:
        if f.name in exclude:
            continue
        # Skip validation for empty fields with blank=True. The developer
        # is responsible for making sure they have a valid value.
        raw_value = getattr(self, f.attname)
        if f.blank and raw_value in f.empty_values:
            continue
        try:
            setattr(self, f.attname, f.clean(raw_value, self))  # to_python()
        except ValidationError as e:
            errors[f.name] = e.error_list[0]
            return errors[f.name]

    if errors:
        raise ValidationError(errors)


def date_rangelist(startdate, enddate):
    # Return list of datetime.date objects between startdate and enddate (inclusive).
    datelist = []
    currdate = startdate
    while currdate <= enddate:
        datelist.append(currdate)
        currdate += timedelta(days=1)
    return datelist


def date_formatted_rangelist(startdate, enddate):
    # Return list of datetime.date objects between startdate and enddate (inclusive).
    datelist = []
    currdate = startdate
    while currdate <= enddate:
        datelist.append(format(currdate, "%d-%m-%Y"))
        currdate += timedelta(days=1)
    return datelist


def date_range_dictionary(startdate, enddate):
    date_range_dict = dict()
    locale.setlocale(locale.LC_TIME, 'nl_NL.UTF-8')
    for listdate in date_rangelist(startdate, enddate):
        date_range_dict.update({
            format(listdate, "%d-%m-%Y"):
                {
                    "startdate": startdate,
                    "startday": startdate.isocalendar()[2],
                    "listdate": listdate,
                    "year": listdate.isocalendar()[0],
                    "week": listdate.isocalendar()[1],
                    "weekday": listdate.isocalendar()[2],
                    "dd": listdate.strftime("%a").title(),
                    "day": listdate.strftime("%d").title(),
                    "month": listdate.strftime("%m").title(),
                }})
    return date_range_dict


def add_months(start_date, amount_months):
    if start_date:
        return start_date + relativedelta(months=amount_months)
    return None


def update_successurl(successurl, recordid):
    if 'returnpath' in successurl:
        query_def = parse.parse_qs(parse.urlparse(str(successurl)).query)['returnpath'][0]
        if query_def == 'new_record':
            successurl = successurl + "&pk=" + str(recordid)
    return successurl


def check_datepicker_mindate_maxdate(post_copy, name_field, datemin, datemax, errorlist):
    try:
        if datemin:
            datemin = datetime.strptime(str(datemin), "%Y-%m-%d").date()
        if datemax:
            datemax = datetime.strptime(str(datemax), "%Y-%m-%d").date()
        if name_field in post_copy:
            if post_copy[name_field]:
                datefield = datetime.strptime(post_copy[name_field], "%d-%m-%Y").date()
                if datemin:
                    if datefield < datemin:
                        errorlist.append([name_field, "De opgegeven datum moet groter of gelijk zijn aan " + format(datemin, "%d-%m-%Y") + "."])
                if datemax:
                    if datefield > datemax:
                        errorlist.append([name_field, "De opgegeven datum moet kleiner of gelijk zijn aan " + format(datemax, "%d-%m-%Y") + "."])
    except ValueError:
        pass
    return errorlist
