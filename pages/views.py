from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework import generics
from .models import Proprietor, User
from . import serializers

# Create your views here.
def index(request):
	return render(request, 'pages/index.html', {})

def success(request):
	return render(request, 'pages/successpage.html', {})

def err(request):
	return render(request, 'pages/errorpage.html', {})

class CreateUserPatron(generics.CreateAPIView):
	serializer_class = serializers.CreatePatronSerializer


class CreateUserProprietor(generics.CreateAPIView):
	serializer_class = serializers.CreateProprietorSerializer


class AuthView(ObtainAuthToken):
	serializer_class =	serializers.AuthTokenSerializer
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class Proprietors(generics.ListAPIView):
	serializer_class = serializers.ProprietorDetail
	queryset = Proprietor.objects.all()


class UMain(generics.RetrieveAPIView):
	serializer_class = serializers.ProprietorDetail
	queryset = User.objects.all()

#class UMain(generics.RetrieveAPI)
