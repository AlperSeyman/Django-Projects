from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home/', views.home_page, name='home_page'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout, name='logout'),
    path('post/<str:pk>', views.post_page, name='post_page'), # Dynamic Urls
    path('counter/', views.counter_page, name='counter_page'),
]