from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


# View to create/register a new user (POST request)
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()               # Define the base queryset (used by DRF internally)
    serializer_class = UserSerializer           # Use UserSerializer to validate and format user data
    permission_classes = [AllowAny]             # No authentication required — anyone can register


# View to list all notes for a user and create a new note
class NotesListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer           # Use NoteSerializer to handle note data
    permission_classes = [IsAuthenticated]      # Only authenticated (logged-in) users can access

    # GET method handler – fetch notes that belong only to the current user
    def get_queryset(self):
        user = self.request.user                     # Get the logged-in user
        return Note.objects.filter(author=user)      # Only return notes created by this user

    # POST method handler – create a new note and assign the current user as the author
    def perform_create(self, serializer):
        if serializer.is_valid():                    # Check if the submitted data is valid
            serializer.save(author=self.request.user)  # Save with the current user as author
        else:
            print(serializer.errors)                 # Optional: print errors for debugging


# View to delete a specific note that belongs to the user
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]          # User must be logged in

    # Only allow users to delete their own notes
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
