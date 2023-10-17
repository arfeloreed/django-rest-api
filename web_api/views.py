from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
# all products view
@api_view(["GET", "POST"])
def products(request):
    # getting a list of all the products
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    # adding a product in the database
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# invidual product view
@api_view(["GET", "PUT", "DELETE"])
def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # query = Product.objects.get(pk=pk)

    # querying for a specific product
    if request.method == "GET":
        serializer = ProductSerializer(product)

        return Response(serializer.data)

    # updating a product
    if request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    # deleting a product
    if request.method == "DELETE":
        product.delete()

        return Response()
