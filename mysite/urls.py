"""mysite URL Configuration

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
from login.admin import admin_site
from django.urls import path,include
from login import views
from detection.views import video_feed_1,camera_1,video_feed_2,camera_2


urlpatterns = [
    path('polls/',include('polls.urls')),
    path('base/',views.base),
    path('index/',views.index),
    path('login/',views.login),
    path('to_admin/',views.to_admin),
    path('register/',views.register),
    path('logout/',views.logout),
    path('admin/', admin_site.urls),
    path('captcha',include('captcha.urls')),
    path('video_feed_1/',video_feed_1,name="video-feed-1"),
    path('video_feed_1/',video_feed_2,name="video-feed-2"),
    path('camera_1/',camera_1),
    path('camera_2/',camera_2),

]
