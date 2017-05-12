from django.conf.urls import url, include
from imageapi import views
from rest_framework.authtoken import views as authViews

urlpatterns = [
    url(r'^image/$', views.ImageList.as_view()),
    url(r'^image/(?P<img>(.*?))/$', views.ImageDetail.as_view()),
    url(r'^api-token-auth/$', authViews.obtain_auth_token)
]
