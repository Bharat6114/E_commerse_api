from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only =True)
    class Meta:
        model =User
        fields = ['username','email','id',"isAdmin"]
    def get_isAdmin(self,obj):
        return obj.is_staff