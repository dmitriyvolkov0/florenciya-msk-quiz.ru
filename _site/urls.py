from django.urls import path
from . import views


app_name = '_site'


urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.not_found, name='not_found'),
]