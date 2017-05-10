from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from imageapi import views
urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^imagedetail/$', views.ImageDetail.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from rest_framework.authtoken import views

urlpatterns += [
    url(r'^api-token-auth/$', views.obtain_auth_token)
]