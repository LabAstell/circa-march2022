from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_circa, name='start_circa'),
]
