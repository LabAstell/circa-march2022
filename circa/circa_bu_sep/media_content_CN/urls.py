from django.urls import path
from . import views


app_name = 'media_content_CN'
urlpatterns = [
    path('', views.index_CN, name='index_CN'),
    path("image/<int:pk>/", views.image_detail_CN, name="image_detail_CN"),
    path("video/<int:pk>/", views.video_detail_CN, name="video_detail_CN"),
    path("audio/<int:pk>/", views.audio_detail_CN, name="audio_detail_CN"),
    ]



