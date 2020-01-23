from django.urls import path
from . import views


urlpatterns = [
    path('', views.show),
    path('starter/', views.show_starter),
    path('respond/', views.RespondFormView.as_view()),
]
