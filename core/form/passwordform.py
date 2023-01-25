from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Column, Layout
from core.globals.global_functions import encode_string, decode_string
from django.contrib.auth.forms import PasswordChangeForm
from users.models import User


class PasswordformBuilder:
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
        self.record = User.objects.get(id=request.user.id)
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

        if request.method == 'POST':
            self.form = PasswordChangeForm(request.user, request.POST)
        else:
            self.form = PasswordChangeForm(request.user)
        self.fields = self.form.fields

        """Declare the Crispy form.helper"""
        self.form.helper = FormHelper()
        self.form.helper.layout = Layout()

        for namefield, formfield in self.fields.items():
            crispyrow = Row(css_class='mb-1')
            crispycolumn = Column(css_class='')
            crispycolumn.append(namefield)
            crispyrow.append(crispycolumn)
            self.form.helper.layout.append(
                crispyrow
            )

        self.form.helper.form_id = "form" + self.strlevel
        self.form.helper.form_class = 'js-save-form'
        self.form.helper.form_method = 'POST'
        self.form.helper.attrs = {'novalidate': 'novalidate'}
        self.form.helper.form_action = "/core/update/" + str(self.record.id) + "/?level=" + self.strlevel + "&package=users&crud=crudchangepassword&nameform=userprofileform&passwordform=true&successurl=" + self.successurl

    def update(self):
        self.form.ctx = self.ctx
        return self.form
