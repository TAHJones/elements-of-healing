from django.urls import path
from products import views

urlpatterns = [
    path('products/', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]