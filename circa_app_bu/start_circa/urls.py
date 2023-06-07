from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_circa, name='start_circa'),
    #path("media_ca", views.image_detail, name="media_ca"),
    #path("media_cn", views.video_detail, name="media_cn"),
    ]
