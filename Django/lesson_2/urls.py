from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.show),
    path('python-starter/', views.show_starter),
    path('python-essential/', views.show_essential),
    path('python-advanced/', views.show_advanced),
    path('python-django/', views.show_django),

]
