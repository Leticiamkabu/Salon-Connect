from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'


urlpatterns = [
    path('',landing_page, name = "home"),
    path('user_page/',user_page_view, name = "user_page"),
    path('service_provider_page',service_provider_view, name = "service_provider_page"),
    
    
]


urlpatterns += staticfiles_urlpatterns()