from core.globals.global_functions import set_rights_for_module, encode_string, set_ctx_records_filter_ordering_paginate, create_ctx_slug, prepare_message
from shared.variables.template_variables import add_variables
from django.template.loader import render_to_string
from pydoc import locate


class RenderCtxAndContext:
    def __init__(self, request, ctx):
        self.ctx = ctx
        self.ctx['rights'] = set_rights_for_module(request, self.ctx['rights_crud'])
        self.render_templates = ""
        self.ctx['successurl'] = encode_string(self.ctx['successurl_decoded'])
        if 'records' in self.ctx:
            self.ctx = set_ctx_records_filter_ordering_paginate(request, self.ctx)
        self.ctx = create_ctx_slug(self.ctx)
        self.context = add_variables(request)
        if 'records' in self.ctx:
            self.context.update({"ctx": self.ctx, "records": self.ctx['records']})
        elif 'record' in self.ctx:
            self.context.update({"ctx": self.ctx, "record": self.ctx['record']})
        else:
            self.context.update({"ctx": self.ctx})
        self.render_templates = self.ctx['render_templates']

    def render_fragment_list(self):
        self.ctx['list_html'] = ""
        if self.ctx['rights']['read']:
            self.ctx['list_inner_data_html'] = render_to_string(self.render_templates['list_inner_data_html'], self.context)
            self.ctx['list_pagination_html'] = render_to_string(self.render_templates['list_pagination_html'], self.context)
            self.ctx['list_inner_html'] = render_to_string(self.render_templates['list_inner_html'], self.context)
            self.ctx['list_html'] = render_to_string(self.render_templates['list_html'], self.context)
        return self.ctx['list_html']

    def render_fragment_list_inner(self):
        self.ctx['list_inner_data_html'] = ""
        self.ctx['list_pagination_html'] = ""
        if self.ctx['rights']['read']:
            self.ctx['list_inner_data_html'] = render_to_string(self.render_templates['list_inner_data_html'], self.context)
            if self.ctx['paginate']:
                self.ctx['list_pagination_html'] = render_to_string(self.render_templates['list_pagination_html'], self.context)
        return [self.ctx['list_inner_data_html'], self.ctx['list_pagination_html']]

    def render_fragment_summary(self):
        self.ctx['summary_html'] = ""
        if self.ctx['rights']['read']:
            if 'summary_inner_html' in self.ctx:
                self.ctx['summary_inner_html'] = render_to_string(self.render_templates['summary_inner_html'], self.context)
            self.ctx['summary_html'] = render_to_string(self.render_templates['summary_html'], self.context)
        return self.ctx['summary_html']

    def render_fragment_summary_inner(self):
        self.ctx['summary_inner_html'] = ""
        if self.ctx['rights']['read']:
            self.ctx['summary_inner_html'] = render_to_string(self.render_templates['summary_inner_html'], self.context)
        return self.ctx['summary_inner_html']

    def render_fragment_action(self):
        self.ctx['action_html'] = ""
        if self.ctx['rights']['read']:
            self.ctx['action_html'] = render_to_string(self.render_templates['action_html'], self.context)
        return self.ctx['action_html']

    def render_fragment_inlineformset(self):
        self.ctx['inlineformset_html'] = ""
        if self.ctx['rights']['read']:
            self.ctx['inlineformset_html'] = render_to_string(self.render_templates['inlineformset_html'], self.context)
        return self.ctx['inlineformset_html']

    def render_fragment_grid(self):
        self.ctx['grid_html'] = ""
        if self.ctx['rights']['read']:
            self.ctx['grid_inner_html'] = render_to_string(self.render_templates['grid_inner_html'], self.context)
            self.ctx['grid_html'] = render_to_string(self.render_templates['grid_html'], self.context)
        return self.ctx['grid_html']

    def render_fragment_grid_inner(self):
        self.ctx['grid_inner_html'] = ""
        if self.ctx['rights']['read']:
            self.ctx['grid_inner_html'] = render_to_string(self.render_templates['grid_inner_html'], self.context)
        return self.ctx['grid_inner_html']


def create_json_response_fragmentdata(request, data, level, ctx):
    data['fragment'] = request.GET.get('fragment', '')
    data['fragmentrefresh'] = request.GET.get('fragmentrefresh', '')
    data['refreshtarget'] = request.GET.get('refreshtarget', '')
    if not data['refreshtarget']:
        data['refreshtarget'] = 'fragment'
    if ctx['fragmenttype'] == "list":
        if data['refreshtarget'] == 'fragment':
            data['html_body'] = RenderCtxAndContext(request, ctx).render_fragment_list()
        else:
            data['html_body'], data['html_pagination'] = RenderCtxAndContext(request, ctx).render_fragment_list_inner()
    elif ctx['fragmenttype'] == "summary":
        if data['refreshtarget'] == 'fragment':
            data['html_body'] = RenderCtxAndContext(request, ctx).render_fragment_summary()
        else:
            data['html_body'] = RenderCtxAndContext(request, ctx).render_fragment_summary_inner()
    elif ctx['fragmenttype'] == "action":
        data['html_body'] = RenderCtxAndContext(request, ctx).render_fragment_action()
    elif ctx['fragmenttype'] == "inlineformset":
        data['html_body'] = RenderCtxAndContext(request, ctx).render_fragment_inlineformset()
    elif ctx['fragmenttype'] == "grid":
        if data['refreshtarget'] == 'fragment':
            data['html_body'] = RenderCtxAndContext(request, ctx).render_fragment_grid()
        else:
            data['html_body'] = RenderCtxAndContext(request, ctx).render_fragment_grid_inner()

    if 'html_header' in ctx:
        data['html_header'] = render_to_string(ctx['html_header'], {'ctx': ctx}, request=request)
    if 'html_footer' in ctx:
        data['html_footer'] = render_to_string(ctx['html_footer'], {'ctx': ctx}, request=request)

    if 'modalsize' in ctx:
        if ctx['modalsize']:
            data['modalsize'] = ctx['modalsize']

    if 'donotclose' in ctx:
        if ctx['donotclose']:
            data['donotclose'] = ctx['donotclose']

    if 'clickevent' in ctx:
        data['clickevent'] = ctx['clickevent']

    if 'messagelist' in ctx:
        data['messagelist'] = ctx['messagelist']

    data['level'] = level
    data['form_is_valid'] = True
    return data


def create_json_response_confirmdata(request, data, level, ctx):
    data['html_body'] = render_to_string(ctx['templatename'], {'ctx': ctx}, request=request)
    data['html_header'] = render_to_string('core/modals/modalheader.html', {'ctx': ctx}, request=request)
    data['html_footer'] = render_to_string('core/modals/modalfooter.html', {'ctx': ctx}, request=request)

    if 'modalsize' in ctx:
        if ctx['modalsize']:
            data['modalsize'] = ctx['modalsize']

    if 'donotclose' in ctx:
        if ctx['donotclose']:
            data['donotclose'] = ctx['donotclose']

    prepare_message(request, ctx, data, '')
    # if 'messagelist' in ctx:
    #     data['messagelist'] = ctx['messagelist']

    data['level'] = level
    data['form_is_valid'] = True
    return data


def fragmentdatabuilder(request, data):
    level = request.GET.get('level', 0)
    package = request.GET.get('package', '')
    modulename = request.GET.get('fragment', '').lower()
    method = request.GET.get('fragment', '').title()
    pk = request.GET.get('pk', 0)
    modulepath = "shared.packages." + package.lower() + ".fragments." + modulename
    nameclass = getattr(locate(modulepath), method)
    # ctx = vars(nameclass(request, "", pk))  # At contractdescription the reserved place for viewtype gives an error, but maybe somewhere else this is needed.
    ctx = vars(nameclass(request, pk))
    data = create_json_response_fragmentdata(request, data, level, ctx)
    return data


def confirmdatabuilder(request, data):
    level = request.GET.get('level', 0)
    package = request.GET.get('package', '')
    modulename = request.GET.get('confirm', '').lower()
    method = request.GET.get('confirm', '').title()
    pk = request.GET.get('pk', 0)
    modulepath = "shared.packages." + package.lower() + ".confirms." + modulename
    nameclass = getattr(locate(modulepath), method)
    ctx = vars(nameclass(request, '', pk))
    ctx = create_ctx_slug(ctx)
    data = create_json_response_confirmdata(request, data, level, ctx)
    return data
