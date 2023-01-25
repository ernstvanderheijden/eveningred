from django.contrib.auth.forms import AuthenticationForm
# from users.models import User
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User

    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        return user
