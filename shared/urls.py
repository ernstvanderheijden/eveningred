from django.urls import path  # , re_path

from shared import views
from shared.actions import action

app_name = "shared"

urlpatterns = [
    path('action/save_right/<int:pk>/', views.save_right, name='save_right'),
    path('execute_download_xlsx/', views.execute_download_xlsx, name='execute_download_xlsx'),

    # path('action/move_item/', views.move_item, name='move_up'),

    # path('action/actions/', action.actions, name='actions'),

    # path('save_checkbox/', views.save_checkbox, name='save_checkbox'),
    # path('save_value/', views.save_value, name='save_value'),
    # path('save_record/', views.save_record, name='save_record'),

    # path('invoice/check_mollie_status/', views.check_mollie_status, name='check_mollie_status'),
]
