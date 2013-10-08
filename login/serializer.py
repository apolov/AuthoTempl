from rest_framework import serializers
from .models import Service
from django.contrib.auth.models import User 


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('url', 'name','serviceprovider',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'last_name',)