from core import views
from core.functions import postcodenl
from core.globals.global_functions import save_paginatesize
from django.urls import path

app_name = "core"

urlpatterns = [
    path('template/', views.Template.as_view(), name='template'),

    path('create/', views.Create.as_view(), name='create'),
    path('update/<int:pk>/', views.Update.as_view(), name='update'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),

    path('fragment/', views.fragment, name='fragment'),
    path('confirm/', views.confirm, name='confirm'),

    path('get_address/', postcodenl.get_address, name='get_address'),
    path('save_paginatesize/', save_paginatesize, name='save_paginatesize'),

    path('showctx/', views.showctx, name='showctx'),

]
