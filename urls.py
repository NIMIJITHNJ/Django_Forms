from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Product_Review/', views.Product_Review, name='Product_Review'),
    path('Review_Confirmation/',views.Review_Confirmation, name='Review_Confirmation'),
]