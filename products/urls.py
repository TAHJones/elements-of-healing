from django.urls import path
from products import views

urlpatterns = [
    path('products/', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/update/<int:product_id>/', views.update_product, name='update_product'),
]
