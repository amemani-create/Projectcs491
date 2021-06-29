from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'store/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True,
                                )
    cart_product_form = CartAddProductForm()

    return render(request,
                  'store/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form}
                  )


def search_products(request):
    query = request.GET['q']
    s_products = Product.objects.filter(name__icontains=query, available=True)
    return render(request,
                  'store/product/search_list.html',
                  {'s_products': s_products})
