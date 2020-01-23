from django.urls import path
from . import views


urlpatterns = [
    path('', views.show),
    path('homework/', views.homework),
    path('html_form/', views.show_html),
    path('get/', views.get_html_form),
    path('post', views.post_html_form),
    path('model_form/', views.show_model),
    path('class_form/', views.show_class),
    path('validator/', views.show_validator),
]
