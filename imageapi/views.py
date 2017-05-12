from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from imageapi.renderers import ImageRenderer
import os


class ImageList(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if 'myfile' in request.FILES:
            myfile = request.FILES['myfile']
            username = request.user.username
            location = os.path.join(settings.MEDIA_ROOT, username)
            fs = FileSystemStorage(location=location)
            filename = fs.save(myfile.name, myfile)
            content = {
                'uploaded_file_name': filename
            }
            return Response(content, status=status.HTTP_201_CREATED)
        else:
            content = {
                "message": "File not found in request"
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        username = request.user.username
        images = os.listdir(os.path.join(settings.MEDIA_ROOT, username))
        content = []
        for image in images:
            content.append({
                "filename": image
            })
        return Response(content)


class ImageDetail(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ImageRenderer, JSONRenderer, )

    def get(self, request, img):
        username = request.user.username
        images = os.listdir(os.path.join(settings.MEDIA_ROOT, username))
        if img in images:
            path = os.path.join(settings.MEDIA_ROOT, username, img)
            image = open(path, "rb").read()
            return Response(image, content_type="image/*")
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, img):
        username = request.user.username
        images = os.listdir(os.path.join(settings.MEDIA_ROOT, username))
        if img in images:
            path = os.path.join(settings.MEDIA_ROOT, username, img)
            os.remove(path)
            if 'myfile' in request.FILES:
                myfile = request.FILES['myfile']
                location = os.path.join(settings.MEDIA_ROOT, username)
                fs = FileSystemStorage(location=location)
                filename = fs.save(img, myfile)
                content = {
                    'uploaded_file_name': filename
                }
                print (content)
                return Response(content, content_type="application/json")
            else:
                content = {
                    "message": "File not found in request"
                }
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, img):
        username = request.user.username
        images = os.listdir(os.path.join(settings.MEDIA_ROOT, username))
        if img in images:
            path = os.path.join(settings.MEDIA_ROOT, username, img)
            os.remove(path)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
