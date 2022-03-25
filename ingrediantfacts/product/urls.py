from django.contrib import admin
from django.urls import include, path
from product import views

urlpatterns = [
    path('addproduct/', views.addproduct),
    path('product/', include('product.urls')),
]
