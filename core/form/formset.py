from core.globals.global_form import set_fieldlist, set_formset
from core.globals.global_functions import encode_string, decode_string
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, HTML
from django.forms import NumberInput, Textarea
from django import forms


class FormsetBuilder:
    def __init__(self, request, ctx):
        self.deny_delete = False

        """Set variables """
        self.ctx = ctx
        self.package = request.GET.get('package', '').lower()
        self.crud = request.GET.get('crud', '')
        self.fragment = request.GET.get('fragment', '')
        self.fragmentrefresh = request.GET.get('fragmentrefresh', '')
        self.nameform = request.GET.get('nameform', '')
        self.errorlist = None
        self.formset = None
        self.fields = None
        self.strlevel = request.GET.get('level', '')
        self.record = ctx['record']
        self.records = ctx['records']
        self.fk = request.GET.get('fk', '')
        if 'viewtype' in ctx:
            self.viewtype = ctx['viewtype']

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

        """set form, fields and fieldlist, based on modules """
        self.formset = set_formset(request, self.package, self.record, self.ctx)

        """Declare the Crispy form.helper"""
        self.formset.helper = FormHelper()
        self.formset.helper.layout = Layout()

        fieldlist = set_fieldlist(request, self.package.lower())
        try:
            if not fieldlist:
                self.errors = True
        except AttributeError:
            fieldlist = dict()
            self.errors = True

        cntr = 0
        """Set the Crispy row"""
        crispyrow = Row(css_class='mb-1')

        """Loop the inlineforms"""
        for index, singleform in enumerate(self.formset.forms):
            cntr += 1

            """Set the Crispy row"""
            crispyrow = Row(css_class='mb-1')

            for f in list(singleform.fields):  # self.fields is the list with all fields from the module
                if f not in fieldlist:
                    del singleform.fields[f]

            for f in fieldlist:  # fieldlist is the list with all fields from the form
                """Set the Crispy column"""
                crispycolumn = Column(css_class='')

                fieldclass = ""   # Collect all classes en put them in fieldclass
                if 'required' in fieldlist[f]:
                    singleform.fields[f].required = fieldlist[f]['required']
                if 'readonly' in fieldlist[f]:
                    singleform.fields[f].widget.attrs['readonly'] = True
                if 'disabled' in fieldlist[f]:
                    singleform.fields[f].disabled = "disabled"
                if 'initial' in fieldlist[f]:
                    if fieldlist[f]['initial']:
                        singleform.fields[f].initial = fieldlist[f]['initial']
                if 'hidden' in fieldlist[f]:
                    if fieldlist[f]['hidden']:
                        singleform.fields[f].widget = forms.HiddenInput()
                if 'label' in fieldlist[f]:
                    if cntr > 1:
                        singleform.fields[f].label = ""
                    else:
                        singleform.fields[f].label = fieldlist[f]['label']
                if 'choicelist' in fieldlist[f]:
                    singleform.fields[f].choices = fieldlist[f]['choicelist']
                if 'onchange' in fieldlist[f]:
                    singleform.fields[f].widget.attrs['onchange'] = fieldlist[f]['onchange']
                if 'autofocus' in fieldlist[f]:
                    # singleform.fields[f].widget.attrs.update({'autofocus': fieldlist[f]['autofocus']})
                    fieldclass = fieldclass + "focus"
                if 'class' in fieldlist[f]:
                    fieldclass = fieldclass + " " + fieldlist[f]['class']
                if fieldclass:
                    singleform.fields[f].widget.attrs.update({'class': fieldclass})

                crispycolumn.append(Field(f))

                if 'field_as_label' in fieldlist[f]:
                    singleform.fields[f].widget = forms.HiddenInput()
                    if request.method == "GET":
                        singleform.fields["field_as_label"] = forms.CharField()
                        singleform.fields["field_as_label"].initial = fieldlist[f]['choicelist'][(singleform.initial[f]-1)][1]
                        singleform.fields["field_as_label"].label = ''
                        singleform.fields["field_as_label"].required = False
                        singleform.fields["field_as_label"].disabled = True
                        singleform.fields["field_as_label"].widget.attrs.update({'class': "bg-transparent border-0 text-dark p-0"})
                        if index == 0:
                            singleform.fields["field_as_label"].label = singleform.fields[f].label
                        crispycolumn.append(
                            Field("field_as_label")
                        )
                elif 'fieldtype' in fieldlist[f]:
                    match fieldlist[f]['fieldtype']:
                        case 'radio':
                            singleform.fields[f] = forms.TypedChoiceField(
                                                    choices=fieldlist[f]['choicelist'],
                                                    coerce=lambda x: x,  # 'coerce': lambda x: bool(int(x))
                                                    widget=forms.RadioSelect,
                                                    label=fieldlist[f]['label'],
                                                )
                            if 'initial' in fieldlist[f]:
                                singleform.fields[f].initial = fieldlist[f]['initial']
                            if 'required' in fieldlist[f]:
                                singleform.fields[f].required = fieldlist[f]['required']
                        case 'pre_filled_hidden':
                            if self.viewtype == 'create' and self.fk:
                                singleform.fields[f].initial = self.fk
                            singleform.fields[f].widget = forms.HiddenInput()
                            crispycolumn.css_class = "d-none"
                        case 'date':
                            if 'initial_value' in fieldlist[f]:
                                singleform.fields[f].widget = NumberInput(attrs={'type': 'date', 'value': fieldlist[f]['initial_value']})
                            else:
                                singleform.fields[f].widget = NumberInput(attrs={'type': 'date'})
                            if 'data-attr' in fieldlist[f]:
                                singleform.fields[f].widget.attrs.update(fieldlist[f]['data-attr'])
                            if 'readonly' in fieldlist[f]:
                                singleform.fields[f].widget.attrs['readonly'] = True
                            if 'keyboard' in fieldlist[f]:
                                if not fieldlist[f]['keyboard']:
                                    singleform.fields[f].widget.attrs.update({'onkeydown': 'return false'})
                            if 'onchange' in fieldlist[f]:
                                singleform.fields[f].widget.attrs.update({"onchange": fieldlist[f]['onchange']})
                        case 'include':
                            crispycolumn.append(
                                HTML("{% include '" + fieldlist[f]['templatename'] + "' %}")
                            )
                        case 'textarea':
                            singleform.fields[f].widget = Textarea(attrs=fieldlist[f]['attributes'])
                elif 'onclick' in fieldlist[f]:
                    pass

                crispyrow.append(crispycolumn)
        self.formset.helper.layout.append(
            crispyrow
        )

        # """Set the fields to form.fields"""
        # singleform.fields = self.fields

        """Set the rest of the Crispy form.helper"""
        self.formset.helper.form_id = "form" + self.strlevel
        self.formset.helper.form_class = 'js-save-form'
        self.formset.helper.form_method = 'POST'
        self.formset.helper.attrs = {'novalidate': 'novalidate'}

    def create(self):
        if 'form_action' in self.ctx:
            self.formset.helper.form_action = self.ctx['form_action']
        else:
            self.formset.helper.form_action = "/core/create/?level=" + self.strlevel + "&fk=" + str(self.fk) + "&package=" + self.package.lower() + "&crud=" + self.crud.lower() + "&fragment=" + self.fragment + "&formset=true&pk=" + str(self.record.id) + "&refreshtarget=data&fragmentrefresh=" + self.fragmentrefresh + "&nameform=" + self.nameform + "&successurl=" + self.successurl
        return self.formset

    def update(self):
        if 'form_action' in self.ctx:
            self.formset.helper.form_action = self.ctx['form_action']
        else:
            self.formset.helper.form_action = "/core/update/" + str(self.record.id) + "/?level=" + self.strlevel + "&package=" + self.package.lower() + "&crud=" + self.crud.lower() + "&fragment=" + self.fragment + "&formset=true&pk=" + str(self.record.id) + "&refreshtarget=data&fragmentrefresh=" + self.fragmentrefresh + "&nameform=" + self.nameform + "&successurl=" + self.successurl
        return self.formset
