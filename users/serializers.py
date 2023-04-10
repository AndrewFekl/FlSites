from rest_framework import serializers
from .models import User
from registrar.serializers import OrganizationSerializer
from django.contrib.auth import authenticate, login

class UserSerializer(serializers.ModelSerializer):

    #organizations = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    organizations = OrganizationSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'last_name', 'first_name', 'phone', 'avatar', 'organizations', 'password')
        #read_only_fields = ('id', 'email')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance





