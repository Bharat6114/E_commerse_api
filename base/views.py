from email import message
from email.mime import image
from itertools import product
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.
from .models import Product
from .serializers import ProductSerializer,UserSerializer
from base import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status



@api_view(['GET'])
def getroutes(request):
    routes=[
        '/api/products/',
        '/api/products/create/',
        '/api/products/update/',
        '/api/products/</id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/update/<id>/',
    ]
    return Response(routes)
#view ton get all products from product model
@api_view(['GET'])
def getproducts(request):
    products= Product.objects.all()
    serializer =ProductSerializer(products,many=True)
    return Response(serializer.data)

#view to get single product
@api_view(["GET"])
def getproduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)
#class based view to get refres and access token with additional info about user
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data=super().validate(attrs)
        data['username'] =self.user.username
        data['email'] =self.user.email
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#view to get user info (user who is login)
@api_view(['GET'])
def getUserProfile(request):
    user = request.user
    serializer =UserSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    user = User.objects.all()
    serializer =UserSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerUsers(request):
    data = request.data
    try:
        user =User.objects.create(
        first_name = data['name'],
        username =data['email'],
        email = data['email'],
        password = make_password(data['password']))

        serializer =UserSerializer(user,many=False)
        return Response(serializer.data)
    except:
        message ={'detail:userwith this email is already exist'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request,pk):
    userfordeletion = User.objects.get(id=pk)
    userfordeletion.delete()
    return Response('user is deleted')

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def upadateUser(request,pk):
    user = User.objects.get(id=pk)
    data = request.data
    user.firstname =data['name'],
    user.username = data['email'],
    user.email = data['email'],
    user.is_staff = data['isAdmin'],
    user.save()
    serializer = UserSerializer (user ,many=False)
    return Response(serializer.data,"update is done")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def productDelete(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product is deleted')

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProducts(request):
    user =request.User
    data =request.data
    product =Product.objects.create(
        name = data['name'],
        price= data['price'],
        brand =data['brand'],
        countinstock =data['countinstock'],
        category = data['category'],
        desscription = data['desscription'],
        rating= data['rating'] ,)
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)
@api_view(['PUT'])
def upadateProduct(request,pk):
    product = Product.objects.get(id=pk)
    data = request.data
    product.name =data['name'],
    product.price= data['price'],
    product.brand =data['brand'],
    product.countinstock =data['countinstock'],
    product.category = data['category'],
    product.desscription = data['desscription'],
    product.rating= data['rating'],
    product.save()
    serializer = ProductSerializer(product ,many=False)
    return Response(serializer.data,"update is done")