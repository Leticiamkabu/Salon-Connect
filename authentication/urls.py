from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



app_name = 'auth'


urlpatterns = [
    path('customer_login/',customer_login_view, name = "customer_login"),
    path('service_provider_login/',service_provider_login_view, name = "service_provider_login"),
    path('customer_registration/',customer_registration_view, name = "customer_registration"),
    path('service_provider_registration/',service_provider_registration_view, name = "service_provider_registration"),
    
    path('log_reg/',login_register_view, name = "login_register"),
    
]