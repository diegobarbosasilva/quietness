from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def register(request):
    return HttpResponse('teste')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register', register),
]
