from django.urls import path
from . import views



app_name='media_content'
urlpatterns = [
    path('', views.index, name='index'),
    path("image/<int:pk>/", views.image_detail, name="image_detail"),
    path("video/<int:pk>/", views.video_detail, name="video_detail"),
    path("audio/<int:pk>/", views.audio_detail, name="audio_detail"),
    ]



