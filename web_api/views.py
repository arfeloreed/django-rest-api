from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer, RegistrationSerializer


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


# creating a user
@api_view(["POST"])
def register(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            # save the newly created user to the database
            user = serializer.save()
            print(f"\n{serializer}\n")
            data["response"] = "Succefully created new user"

            auth_token = Token.objects.get(user=user).key
            data["token"] = auth_token
        else:
            data = serializer.errors

        return Response(data)
