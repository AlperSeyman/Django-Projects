from django.urls import path
from main import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home/', views.home_page, name='home_page'),
    path('post/<str:pk>', views.post_page, name='post_page')
]