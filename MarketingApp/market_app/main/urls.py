from django.urls import path
from main import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home/', views.home_page, name='home_page'),
    path('items/', views.items_page, name='items_page'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page')
]