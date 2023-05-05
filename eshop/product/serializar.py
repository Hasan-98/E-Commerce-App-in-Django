from rest_framework import serializers
from .models import *
class ProductImagesSerializar(serializers.ModelSerializer):
    class Meta:
        model: ProductImages
        fields = "__all__"

         
class ProductSerializar(serializers.ModelSerializer):

    images = ProductImagesSerializar(many=True , read_only=True)
    class Meta:
        model: Product
        fields = ('id' ,'name', 'description', 'price', 'brand','ratings', 'category' , 'stock' , 'user' , 'images')
        extra_kwars = {
            "name":{"required": True , 'allow_blank': False},
             "description":{"required": True , 'allow_blank': False},
             "brand":{"required": True , 'allow_blank': False},
             "category":{"required": True , 'allow_blank': False},
        }

