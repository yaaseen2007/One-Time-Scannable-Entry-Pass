
from django.urls import path
from . import views

urlpatterns = [

    path('', views.register, name='register'),
    path('thank_you/', views.thank_you, name='thankyou'),
    path('pending_users/', views.pending_users, name='pendingusers')
]