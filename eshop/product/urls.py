
from . import views
from django.urls import path

urlpatterns = [
    path('products/' , views.get_products, name="products"),
    path('products/<str:pk>/' , views.get_products, name= "get_product_details")
]