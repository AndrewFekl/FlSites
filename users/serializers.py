from rest_framework import serializers
from .models import User
from registrar.serializers import OrganizationSerializer
from django.contrib.auth import authenticate, login

class UserSerializer(serializers.ModelSerializer):

    organizations = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    #organizations = OrganizationSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'last_name', 'first_name', 'phone', 'avatar', 'organizations')
        read_only_fields = ('id', 'email')

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")

            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")

        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        attrs['user'] = user
        return attrs



