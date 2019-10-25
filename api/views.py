from django.shortcuts import render
from rest_framework import generics
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from pages.models import Proprietor

class CreateUserView(generics.CreateAPIView):
	serializer_class = serializers.CreateUser


class CreatePatronView(generics.CreateAPIView):
	serializer_class = serializers.CreatePatron


class CreateProprietorView(generics.CreateAPIView):
	serializer_class = serializers.CreateProprietor


class AuthView(ObtainAuthToken):
	serializer_class =	serializers.AuthTokenSerializer
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProprietorProfile(generics.RetrieveAPIView):
	serializer_class = serializers.ProprietorProfile

class PatronProfile(generics.RetrieveAPIView):
	serializer_class = serializers.PatronProfile

class Home(generics.ListAPIView):
	serializer_class = serializers.UMain
	queryset = Proprietor.objects.all()

class SetTrip(generics.RetrieveAPIView):
	serializer_class = serializers.SetTrip
