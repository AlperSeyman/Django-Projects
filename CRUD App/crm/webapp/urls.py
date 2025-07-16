from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


    # CRUD
    path('dashboard/',views.dashboard, name='dashboard'),
    path('record/<int:pk>', views.show_individual_record, name='show_record'), # read one single record
    path('create-record/', views.create_record, name='create_record'), # create
    path('update-record/<int:pk>', views.update_record, name='update_record'), # update
    path('delete-record/<int:pk>', views.delete_record, name='delete_record'), # delete 
    
]