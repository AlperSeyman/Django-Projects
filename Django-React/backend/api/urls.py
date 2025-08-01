from django.urls import path
from .views import CreateUserView, NotesListCreate, NoteDelete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('user/register/', CreateUserView.as_view(), name='create_user'),
    path('token/', TokenObtainPairView.as_view(), name="get_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
    path('notes/', NotesListCreate.as_view(), name="note-list"),
    path('notes/delete/<int:pk>/', NoteDelete.as_view(), name="delete-note")
    
]