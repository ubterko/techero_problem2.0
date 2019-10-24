from rest_framework import serializers
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model, authenticate
from . import models

class CreateProprietorSerializer(serializers.ModelSerializer):
    """This is the serializer for creating proprietor user"""

    class Meta:
        model = get_user_model()
        fields = [
            'email','password','name',
            'is_proprietor',
        ]

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class CreatePatronSerializer(serializers.ModelSerializer):
    """This is the serializer for creating patron user"""

    class Meta:
        model = get_user_model()
        fields = ['email','password','name']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)




class AuthTokenSerializer(serializers.Serializer):
    """Serializer for creating a token for authentication"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email, password=password
        )

        if not user:
            raise serializers.ValidationError(_('This is not a valid user'), code=authorization)

        attrs['user'] = user
        return attrs


class ProprietorDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Proprietor
        fields = ['user','car_model','liscence_no']


class SetTrip(serializers.ModelSerializer):
    class Meta:
        model = models.trip
        fields = ['patron','distance','time']
