from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product


def HomePageView(request):
    return render(request, 'index.html')


def ProductPageView(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'kategoriya': categories,
        'mahsulotlar': products
    }
    return render(request, 'products.html', context)


def ProductDetailView(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'mahsulot': product
    }
    return render(request, 'product_detail.html', context)

