from datetime import datetime

from django.template.loader import render_to_string
from tinymce.widgets import TinyMCE

from core.globals.global_form import set_form, set_fieldlist
from core.globals.global_functions import encode_string, decode_string, check_datepicker_mindate_maxdate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, HTML
from django import forms


class FormBuilder:
    def __init__(self, request, ctx):
        self.deny_delete = False
        self.ctx = ctx
        self.package = request.GET.get('package', '').lower()
        # self.chapter = request.GET.get('chapter', '')
        self.crud = request.GET.get('crud', '')
        self.fragment = request.GET.get('fragment', '')
        self.fragmentrefresh = request.GET.get('fragmentrefresh', '')
        self.nameform = request.GET.get('nameform', '')
        self.errors = False
        self.errorlist = list()
        self.form = None
        self.all_fields = False
        self.fields = None
        self.strlevel = request.GET.get('level', '')
        self.record = ctx['record']
        self.fk = request.GET.get('fk', '')
        if 'viewtype' in ctx:
            self.viewtype = ctx['viewtype']

        """set form, fields and fieldlist, based on modules """
        self.form = set_form(request, self.package, self.record)
        self.fields = self.form.fields
        fieldlist = set_fieldlist(request, self.package.lower())
        if 'all_fields' in fieldlist:
            self.all_fields = fieldlist['all_fields']
            del fieldlist['all_fields']
            for fname, fdata in self.form.fields.items():
                if fname not in fieldlist:
                    fieldlist.update({fname: {}})

        """Set successurl"""
        if 'successurl' in self.ctx:
            self.successurl = self.ctx['successurl']
        else:
            self.successurl = request.GET.get('successurl', '')
        if self.fragment:
            self.successurl_decoded = decode_string(self.successurl) + "&filter=" + request.GET.get('filter', '')
        else:
            self.successurl_decoded = decode_string(self.successurl)
        self.successurl = encode_string(self.successurl_decoded)

        try:
            if not fieldlist:
                self.errors = True
            if self.viewtype == 'update' and ctx['deny_del_or_upd']:
                self.viewtype = self.viewtype + "_deny_del_or_upd"
        except AttributeError:
            fieldlist = dict()
            self.errors = True

        """Declare the Crispy form.helper"""
        self.form.helper = FormHelper()
        self.form.helper.layout = Layout()

        if not self.all_fields:
            for f in list(self.fields):  # self.fields is the list with all fields from the module
                if f not in fieldlist:
                    del self.fields[f]

        for f in fieldlist:  # fieldlist is the list with all fields from the form
            fieldclass = ""  # Collect all classes en put them in fieldclass
            if 'required' in fieldlist[f]:
                self.fields[f].required = fieldlist[f]['required']
            if 'readonly' in fieldlist[f]:
                self.fields[f].widget.attrs['readonly'] = True
            if 'disabled' in fieldlist[f]:
                self.fields[f].disabled = "disabled"
            if 'initial' in fieldlist[f]:
                if fieldlist[f]['initial']:
                    self.fields[f].initial = fieldlist[f]['initial']
            if 'hidden' in fieldlist[f]:
                if fieldlist[f]['hidden']:
                    self.fields[f].widget = forms.HiddenInput()
            if 'label' in fieldlist[f]:
                self.fields[f].label = fieldlist[f]['label']
            if 'choicelist' in fieldlist[f]:
                self.fields[f].choices = fieldlist[f]['choicelist']
            if 'onchange' in fieldlist[f]:
                self.fields[f].widget.attrs['onchange'] = fieldlist[f]['onchange']
            if 'placeholder' in fieldlist[f]:
                self.fields[f].widget.attrs['placeholder'] = fieldlist[f]['placeholder']
            if 'autofocus' in fieldlist[f]:
                # self.fields[f].widget.attrs.update({'autofocus': fieldlist[f]['autofocus']})
                fieldclass = fieldclass + "focus"
            if 'class' in fieldlist[f]:
                fieldclass = fieldclass + " " + fieldlist[f]['class']
            if fieldclass:
                self.fields[f].widget.attrs.update({'class': fieldclass})
            if 'keyboard' in fieldlist[f]:
                if not fieldlist[f]['keyboard']:
                    self.fields[f].widget.attrs.update({'onkeydown': 'return false'})

            if self.viewtype == 'delete':
                if 'deny_delete' in fieldlist[f]:
                    if fieldlist[f]['deny_delete']:
                        self.deny_delete = True
                if f != 'include':
                    self.fields[f].widget = forms.HiddenInput()
                    self.fields[f].required = False
                    self.form.helper.layout.append(f)
            else:
                """Set the Crispy form.helper"""
                crispyrow = Row(css_class='mb-1')
                crispycolumn = Column(css_class='')

                if 'href' in fieldlist[f]:
                    if fieldlist[f]['href']:
                        crispycolumn.append(
                            HTML("<a href='" + fieldlist[f]['href_url'] + "' target=" + fieldlist[f]['href_target'] + ">" + fieldlist[f]['href_description'] + " <i class='fas fa-external-link-alt'></i></a>")
                        )

                if 'field_blocked' in fieldlist[f]:
                    if fieldlist[f]['field_blocked']:  # str(getattr(self.record, f))
                        self.fields[f].widget = forms.HiddenInput()
                        crispycolumn.append(
                            HTML("<div class='container-fluid'><div class='row'><div class='col'>" + fieldlist[f]['label'] + "</div><div class='col'><span class='blocked_field'>" + str(getattr(self.record, f)) + "</span></div></div></div>")
                        )
                elif 'blocked_when_used' in fieldlist[f] and '_deny_del_or_upd' in self.viewtype:
                    if fieldlist[f]['blocked_when_used']:  # str(getattr(self.record, f))
                        # self.fields[f].widget = forms.HiddenInput()
                        self.fields[f].widget.attrs['readonly'] = True

                        # crispycolumn.append(
                        #     HTML("<span class='blocked_field'>" + str(getattr(self.record, f)) + "</span>")
                        # )

                if f == 'include':  # This field tells us that there is an include file to insert in the form
                    if 'templatename' in fieldlist[f]:
                        if 'templatedata' in fieldlist[f]:
                            crispycolumn.append(HTML(render_to_string(fieldlist[f]['templatename'], {'data': fieldlist[f]['templatedata']})))
                        else:
                            crispycolumn.append(HTML("{% include '" + fieldlist[f]['templatename'] + "' %}"))
                elif 'included' in fieldlist[f]:
                    self.fields[f].widget.attrs.update({'class': 'form-control'})
                    # This means that there is an `include` in the form and
                    pass  # this field is part of it and must be loaded as formfield, but not shown as formfield

                elif 'datepicker' in fieldlist[f]:
                    params = dict()
                    datemax = str()
                    datemin = str()
                    if 'min' in fieldlist[f]:
                        datemin = fieldlist[f]['min']
                        params.update({'data_datepickermin': datemin})

                    if 'max' in fieldlist[f]:
                        datemax = fieldlist[f]['max']
                        params.update({'data_datepickermax': datemax})

                    if 'start' in fieldlist[f]:
                        datestart = fieldlist[f]['start']
                    else:
                        datestart = datetime.today().date()
                    params.update({'data_datepickerstart': datestart})

                    crispycolumn.append(
                        Field(f, **params, template="core/widgets/datepicker.html")
                    )
                    # Error handling datepicker (1)
                    if request.POST:
                        self.errorlist = check_datepicker_mindate_maxdate(request.POST.copy(), f, datemin, datemax, self.errorlist)

                elif 'modal_select' in fieldlist[f]:
                    self.fields[f].widget = forms.HiddenInput()
                    showvalue = ''
                    if self.record:
                        showvalue = str(getattr(self.record, f))
                    elif 'initial' in fieldlist[f]:
                        showvalue = fieldlist[f]['showvalue']

                    if request.method == "POST":
                        post = request.POST.copy()
                        if f in post:
                            self.fields[f].initial = post[f]
                            showvalue = post['modal_select_' + f]
                    crispycolumn.append(
                        Field(f, onclick=fieldlist[f]['onclick'], showvalue=showvalue, template="core/widgets/modal_select.html")
                    )
                else:
                    crispycolumn.append(Field(f))
                    if 'fieldtype' in fieldlist[f]:
                        match fieldlist[f]['fieldtype']:
                            case 'tinymce':
                                self.fields[f] = forms.CharField(widget=TinyMCE(attrs={'cols': fieldlist[f]['tinymce']['cols'], 'rows': fieldlist[f]['tinymce']['rows']}))
                            case 'radio':
                                self.fields[f] = forms.TypedChoiceField(
                                    choices=fieldlist[f]['choicelist'],
                                    coerce=lambda x: x,  # 'coerce': lambda x: bool(int(x))
                                    widget=forms.RadioSelect,
                                    label=fieldlist[f]['label'],
                                )
                                if 'initial' in fieldlist[f]:
                                    self.fields[f].initial = fieldlist[f]['initial']
                                if 'required' in fieldlist[f]:
                                    self.fields[f].required = fieldlist[f]['required']
                                if 'disabled' in fieldlist[f]:
                                    self.fields[f].disabled = fieldlist[f]['disabled']
                            case 'pre_filled_hidden':
                                if self.viewtype == 'create' and self.fk:
                                    self.fields[f].initial = self.fk
                                self.fields[f].widget = forms.HiddenInput()
                            case 'date':
                                if 'initial_value' in fieldlist[f]:
                                    self.fields[f].widget = forms.NumberInput(attrs={'type': 'date', 'value': fieldlist[f]['initial_value']})
                                else:
                                    self.fields[f].widget = forms.NumberInput(attrs={'type': 'date'})
                                if 'data-attr' in fieldlist[f]:
                                    self.fields[f].widget.attrs.update(fieldlist[f]['data-attr'])
                                if 'readonly' in fieldlist[f]:
                                    self.fields[f].widget.attrs['readonly'] = True
                                if 'keyboard' in fieldlist[f]:
                                    if not fieldlist[f]['keyboard']:
                                        self.fields[f].widget.attrs.update({'onkeydown': 'return false'})
                                if 'onchange' in fieldlist[f]:
                                    self.fields[f].widget.attrs.update({"onchange": fieldlist[f]['onchange']})
                            case 'include':
                                crispycolumn.append(
                                    HTML("{% include '" + fieldlist[f]['templatename'] + "' %}")
                                )
                            case 'textarea':
                                self.fields[f].widget = forms.Textarea(attrs=fieldlist[f]['attributes'])
                    elif 'onclick' in fieldlist[f]:
                        pass
                crispyrow.append(crispycolumn)
                self.form.helper.layout.append(
                    crispyrow
                )

        # Error handling datepicker (2)
        if self.errorlist:
            for err in self.errorlist:
                if err[1]:
                    self.form.add_error(err[0], err[1])

        # """Set the fields to form.fields"""  This problably has no use, throw it away next time
        # self.form.fields = self.fields

        self.record_id = 0
        if self.record:
            if self.record.id:
                self.record_id = self.record.id

        """Set the rest of the Crispy form.helper"""
        if not self.strlevel:
            self.strlevel = "0"
        self.form.helper.form_id = "form" + self.strlevel
        self.form.helper.form_class = 'js-save-form'
        self.form.helper.form_method = 'POST'
        self.form.helper.attrs = {'novalidate': 'novalidate'}

    def create(self):
        if 'form_action' in self.ctx:
            self.form.helper.form_action = self.ctx['form_action']
        else:
            self.form.helper.form_action = "/core/create/?level=" + self.strlevel + "&fk=" + str(self.fk) + "&package=" + self.package.lower() + "&crud=" + self.crud.lower() + "&fragment=" + self.fragment + "&refreshtarget=data&fragmentrefresh=" + self.fragmentrefresh + "&nameform=" + self.nameform + "&successurl=" + self.successurl
        if self.errors:
            return "empty_form"
        else:
            return self.form

    def update(self):
        self.form.ctx = self.ctx

        if 'form_action' in self.ctx:
            self.form.helper.form_action = self.ctx['form_action']
        else:
            self.form.helper.form_action = "/core/update/" + str(self.record_id) + "/?level=" + self.strlevel + "&package=" + self.package.lower() + "&crud=" + self.crud.lower() + "&fragment=" + self.fragment + "&fk=" + str(self.fk) + "&pk=" + str(self.record_id) + "&refreshtarget=data&fragmentrefresh=" + self.fragmentrefresh + "&nameform=" + self.nameform + "&successurl=" + self.successurl
        if self.errors:
            return "empty_form"
        else:
            return self.form

    def delete(self):
        if self.deny_delete:
            return "empty_form"
        self.form.helper.layout.append(  # Set description for the form
            HTML(str(self.record) + " verwijderen?")
        )

        # Set the successurl for use after delete, this will be placed in the request. Not in the ctx
        closelevel = int(self.strlevel) - 1
        if closelevel <= 0:
            closelevel = ''
        else:
            closelevel = str(closelevel)
        # refreshlevel = str(int(self.strlevel) - 2)

        # Set the form action. Also, to be found in the request
        self.form.helper.form_action = "/core/delete/" + str(self.record_id) + \
                                       "/?level=" + self.strlevel + \
                                       "&closelevel=" + closelevel + \
                                       "&package=" + self.package.lower() + \
                                       "&crud=" + self.crud.lower() + \
                                       "&nameform=" + self.nameform + \
                                       "&successurl=" + self.successurl
        if self.errors:
            return "empty_form"
        else:
            return self.form
