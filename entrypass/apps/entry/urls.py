from django.urls import path
from . import views

urlpatterns = [

    path('approve/<str:unique_id>', views.approve_registration, name='approve'),
    path('pass_detail/<str:unique_id>', views.pass_detail, name='passdetail'),
    path('validate/<str:unique_id>', views.validate, name='validate')
    
]