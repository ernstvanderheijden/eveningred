from django.contrib.auth.forms import SetPasswordForm
from users.models import User


# Form for registering user via e-email
class PasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ('password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Nieuw wachtwoord'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Herhaal wachtwoord'
