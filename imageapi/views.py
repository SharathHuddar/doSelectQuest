from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework import generics
# from imageapi.serializers import  UserSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserList(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth)
        }
        return Response(content)
        
class ImageDetail(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        myfile = request.FILES['myfile']
        print (request.user.username)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        content = {
            'uploaded_file_url': fs.url(filename)
        }
        return Response(content)