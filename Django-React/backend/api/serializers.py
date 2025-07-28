from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# Serializer for the User model (for registration)
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User                                     # This serializer is for the built-in Django User model
        fields = ['id', 'username', 'password']         # We only expose these fields
        extra_kwargs = {"password": {"write_only": True}}  # Prevent password from being readable in API response

    def create(self, validated_data):
        # Create the user using Django's built-in create_user method (which hashes the password)
        user = User.objects.create_user(**validated_data)
        return user


# Serializer for the Note model (for reading and writing notes)
class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note                                     # This serializer is for your custom Note model
        fields = ['id', 'title', 'content', 'created_at', 'author']  # Fields to include in API
        extra_kwargs = {'author': {"read_only": True}}  # Prevent users from setting author manually — it is set automatically
