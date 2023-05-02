from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from .models import Product
from rest_framework.response import Response
from .serializar import ProductSerializar
from .filters import ProductsFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.

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
