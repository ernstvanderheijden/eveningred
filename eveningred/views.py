from .forms import LoginForm
from core.tokens import url_one_job_token
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from core.globals.global_private_views import GlobalPrivateTemplate
from shared.packages.users.forms.userpasswordform import PasswordForm
from users.models import User


class Home(GlobalPrivateTemplate):

    def get_context_data(self, **kwargs):  # This def is here for loading view_variables
        context = super().get_context_data(**kwargs)
        context['ctx']['templatename'] = "shared/home/home.html"
        return context


def login_request(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        form = LoginForm()
        return render(request=request, template_name="login/base_login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    return redirect("/login/")


def goto_dashboard(request):
    return redirect("/core/template/?level=0&package=dashboard&chapter=detail")


def setpassword(request, uidb64, token):
    ctx = dict()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid, is_active=True)
        ctx['username'] = user.username
        ctx['first_name'] = user.first_name
        ctx['last_name'] = user.last_name
        ctx['email'] = user.email
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("User does not exist or is not active")
        user = None

    if user is not None and url_one_job_token.check_token(user, token):
        if request.method == 'POST':
            form = PasswordForm(user, data=request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                return redirect('/login/')
        else:
            form = PasswordForm(user)
        ctx['template_name'] = 'login/base_login.html'
        ctx['template_inner'] = 'login/setpassword.html'
        return render(request, ctx['template_name'], {'form': form, 'ctx': ctx})
    else:
        ctx['template_name'] = 'login/base_login.html'
        ctx['template_inner'] = 'login/expired_activation.html'
        return render(request, ctx['template_name'], {'ctx': ctx})


def permission_denied_view(request):
    raise PermissionDenied
