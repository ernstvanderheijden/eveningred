from . import views
from django.conf import settings
from django.contrib.staticfiles.views import serve
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path("", views.goto_dashboard, name='home'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('admin/', admin.site.urls, name='admin'),
    path('core/', include('core.urls')),
    path('shared/', include('shared.urls')),
    path('public/', include('public.urls')),
    path('favicon.ico', RedirectView.as_view(url='/media/favicon.ico')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('users/', include('users.urls')),
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path('setpassword/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', views.setpassword, name='setpassword'),
    # re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('403/', views.permission_denied_view),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
