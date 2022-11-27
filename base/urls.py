from unicodedata import name
from django.urls import path
from . import views
from .views import  MyTokenObtainPairView



urlpatterns =[
    path('users/login/',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/',views.registerUsers, name='userregister'),


    path('',views.getroutes,name="routes"),
    path('products/',views.getproducts,name="products"),
    path('products/<int:pk>/',views.getproduct,name="product"),
    path('users/profile/',views.getUserProfile,name="userprofile"),
    path('users/',views.getUsers,name="users"),
    path('users/delete/<int:pk>/',views.deleteUser,name="deleteuser"),
    path('users/update/<int:pk>/',views.upadateUser,name="updateuser"),
    path('products/delete/<int:pk>/',views.productDelete,name="productdelete"),
    path('products/create/',views.createProducts,name="createproduct"),
    path('products/update/<int:pk>/',views.upadateProduct,name="upadateProduct"),

]
