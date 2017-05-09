from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import getpass
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Create user and obtain access key'
            
    def handle(self, *args, **options):
        username = input("Enter username : ")
        password = getpass.getpass("Enter password : ")
        try:
            user = User.objects.get(username=username)
            print ("User "+username+" already exists.")
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print ("User "+username+" created.")
        token, created = Token.objects.get_or_create(user=user)
        print ("Access key for " + username + " : ")
        print (token)
