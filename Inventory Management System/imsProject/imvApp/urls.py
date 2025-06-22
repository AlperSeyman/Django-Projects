from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('create/',views.create_product_page, name='create_product'),
    path('list/',views.read_product_page, name='product_list'),
    path('update/<int:product_id>',views.update_product_page ,name='update_product'),
    path('delete/<int:product_id>',views.delete_product_page, name='delete_product'),
]
