from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-index'),
    path('sent/', views.contactus, name='contactus-form')
]
