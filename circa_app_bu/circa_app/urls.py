"""circa_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start_circa/', include('start_circa.urls')),
    path('media_content/', include('media_content.urls', namespace='media_content')),
    path('media_content_CN/', include('media_content_CN.urls', namespace='media_content_CN')),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('media_content/', include('media_content.urls')),
#]
