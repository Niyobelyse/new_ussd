from django.urls import path
from .import views

urlpatterns = [
    path('ussd/', views.home, name="home"),
]