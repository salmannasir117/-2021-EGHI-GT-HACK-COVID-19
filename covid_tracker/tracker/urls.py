from django.urls import path

from . import views

app_name = 'tracker' #adds a namespace

urlpatterns = [
    path('', views.test_static, name="static-test"),
]