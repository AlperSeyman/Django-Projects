from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model

# Define a Note model to represent notes in the database
class Note(models.Model):
    # Title of the note (max 100 characters)
    title = models.CharField(max_length=100)
    
    # Content of the note (can be multiple lines of text)
    content = models.TextField()
    
    # Automatically set this field to the current date and time when the note is created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ForeignKey creates a relationship between the note and the user who created it
    # on_delete=models.CASCADE means: if the user is deleted, their notes will also be deleted
    # related_name="notes" allows you to access a user's notes with user.notes.all()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    # This method controls how the note appears when printed or shown in the admin panel
    def __str__(self):
        return self.title
