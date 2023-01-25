from django.urls import path  # , re_path

from public import views, webhooks

app_name = "public"

urlpatterns = [
    # path('invoice/<slug:slug>/', views.invoice, name='invoice'),
    # path('contract/agree/<slug:slug>/', views.contract, name='contract_agree'),
    # path('download_contract/<slug:slug>/', views.download_contract, name='download_contract'),
    # path('open_contract/<slug:slug>/', views.open_contract, name='open_contract'),
    # path('download_invoice/<slug:slug>/', views.download_invoice, name='download_invoice'),
    # path('open_invoice/<slug:slug>/', views.open_invoice, name='open_invoice'),

    path('password_forgotten/', views.password_forgotten, name='password_forgotten'),
    path('reset_password/', views.reset_password, name='password_forgotten'),

    # path('webhooks/mollie_payment/', webhooks.mollie_payment, name='mollie_payment'),
]
