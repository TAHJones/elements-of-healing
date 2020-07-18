from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view to show all remedies and remedy kits, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products.html', context)


def product_detail(request, product_id):
    """ A view to show individual remedies and remedy kits """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product_detail.html', context)
