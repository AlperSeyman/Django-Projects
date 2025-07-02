from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # CRUD
    path('dashboard/',views.dashboard, name='dashboard'),
    path('create-record/', views.create_record, name='create_record'),
    
]