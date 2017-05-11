from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from imageapi import views
urlpatterns = [
    url(r'^image/$', views.ImageList.as_view()),
    url(r'^image/(?P<img>(.*?))/$', views.ImageDetail.as_view())
]

from rest_framework.authtoken import views

urlpatterns += [
    url(r'^api-token-auth/$', views.obtain_auth_token)
]