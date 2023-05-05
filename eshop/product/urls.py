
from . import views
from django.urls import path

urlpatterns = [
    path('products/' , views.get_products, name="products"),
    path('products/new/' , views.new_product, name="new_product"),
    path('products/upload_images/' , views.upload_product_images, name= "upload_product_images"),
    path('products/<str:pk>/' , views.get_products, name= "get_product_details"),
    path('products/<str:pk>/update/' , views.update_product, name= "update_product"),
    path('products/<str:pk>/delete/' , views.delete_product, name= "delete_product")
    
]