from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home/', views.home_page, name='home_page'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register_page'),
    path('record/<int:pk>', views.customer_record, name="record_page"), # localhost:1234/record/2
    path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
    path('add_record/', views.add_record, name="add_record"),
    path('update_record/<int:pk>',views.update_record, name="update_record")
]


