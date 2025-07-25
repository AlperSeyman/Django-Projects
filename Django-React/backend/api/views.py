from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()           # get all users (used internally by the view)
    serializer_class = UserSerializer       # convert User instances to/from JSON and validate data
    permission_classes = [AllowAny]         # allow anyone to access (no login required)


class NotesListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer       # serialize notes to/from JSON
    permission_classes = [IsAuthenticated]  # user must be logged in 

    def get_queryset(self):
        user = self.request.user                 # Get the current logged-in user from the request
        return Note.objects.filter(author=user)  # Return only notes where author is this user
    

    def perform_create(self, serializer):
        # Save the new Note object with the 'author' field set to the currently logged-in user
        # We tell the serializer to save the Note and automatically assign this user as the author
        # self.request.user is the user who made the request (the logged-in user)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)