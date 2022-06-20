from django.shortcuts import render, HttpResponse

# Create your views here.

def landing_page(request):
    return render(request, "home/landing_page.html")

def user_page_view(request):
    return render(request, "user/user_page.html")

def service_provider_view(request):
    return render(request, "service_provider/service_provider_page.html")
