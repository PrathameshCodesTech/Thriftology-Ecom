from django.urls import path
from product.views import Home,ProductDetail,OuterWear,AddCart,ShowCart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',Home,name="Home-Page"),
    path('product-details/<int:pk>',ProductDetail.as_view(),name="Product-Detail"),
    path('Outer-wear-page/',OuterWear,name="Outer-wear"),
    path('outer-wear-page/product-detail/<int:pk>/', ProductDetail.as_view(), name="Outer-Wear-Product-Detail"),


    
    path('add-to-cart/',AddCart,name="Add_Cart"),
    path('cart/',ShowCart,name="Show_Cart"),
]   