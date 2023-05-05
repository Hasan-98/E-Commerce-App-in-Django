from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from .models import Product , ProductImages
from rest_framework.response import Response
from .serializar import *
from .filters import ProductsFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
# Create your views here.



@api_view(['POST'])
def new_product(request):
    data = request.data
    serializer = ProductSerializar(data=data )
    if serializer.is_valid():
                
        product= Product.objects.create(**data)
        res = ProductSerializar(product , many=False)
        return Response({"product":  res.data})


    else:
        return Response(serializer.errors)


@api_view(['GET'])
def get_products(request):
    filterset = ProductsFilter(request.GET , queryset=Product.objects.all())
    count = filterset.qs.count()
    resultPerPage = 2
    paginator = PageNumberPagination()
    paginator.page_size = resultPerPage

    queryset = paginator.paginate_queryset(filterset.qs  , request)
    serializer = ProductSerializar(queryset , many = True)
    return Response({
        "count": count,
        "resPerPage" : resultPerPage,
        "products" : serializer.data})


@api_view(['GET'])
def get_product(request , pk):
    products = get_object_or_404(Product, id=pk)
    serializer = ProductSerializar(products , many = True)
    return Response({"product" : serializer.data})

@api_view(['POST'])
def upload_product_images(request):
    data = request.data
    files = request.files.getlist('images')
    images = []
    for f in files:
        image = ProductImages.object.create(product=Product(data['product']), image = f)
        images.append(image)
    
    serializer = ProductImagesSerializar(images , many = True)
  
    return Response(serializer.data)
  
    return Response(serializer.data)


@api_view(['PUT'])
def update_product(request, pk):
    product = get_object_or_404(Product , id = pk)

    #Check if user is same
    product.name = request.data['name']
    product.description = request.data['description']
    product.price = request.data['price']
    product.category = request.data['category']
    product.brand = request.data['brand']
    product.ratings = request.data['ratings']
    product.stock = request.data['stock']
 
    product.save()
    serializer = ProductSerializar(product , many = False)
  
    return Response(serializer.data)



@api_view(['DELETE'])
def delete_product(request, pk):
    product = get_object_or_404(Product , id = pk)
  #Check if user is same
    product.delete()
   
    return Response({"Details": "Product is Deleted"}, status= status.HTTP_200_OK)


