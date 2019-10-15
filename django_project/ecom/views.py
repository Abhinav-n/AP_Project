from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Review
from carts.models import Cart
from django.db.models import Q
from wishlist.models import Wishlist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    productmen = Product.objects.filter(filters='men')[:3]
    productwomen = Product.objects.filter(filters='women')[:3]
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)
    context = {
        'title': 'Home',
        'cart': cart_obj,
        'productmen': productmen,
        'productwomen': productwomen,
    }
    return render(request, 'ecom/home.html', context)


def contact(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'ecom/contact.html', context)


def cart(request):
    context = {
        'title': 'Cart',
    }
    return render(request, 'ecom/cart.html', context)


def kids(request):
    products = Product.objects.filter(filters='accessories')
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)
    context = {
        'title': 'kids',
        'cart': cart_obj,
        'products': products,
        'wishlist': wishlist_obj,
    }
    return render(request, 'ecom/kids.html', context)


def women(request):
    products = Product.objects.filter(filters='women')
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)
    context = {
        'products': products,
        'cart': cart_obj,
        'wishlist': wishlist_obj,
    }
    return render(request, 'ecom/women.html', context)


def men(request):
    products = Product.objects.filter(filters='men')
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    cart_obj, new_obj = Cart.objects.new_or_get(request)
    wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)

    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    context = {
        'cart': cart_obj,
        'title': 'Men',
        'products': products,
        'wishlist': wishlist_obj,
        'filter': product_filter,
    }
    return render(request, 'ecom/men.html', context)


def loggedin(request):
    context = {
        'title': 'Loggedin',
    }
    return render(request, 'ecom/loggedin.html', context)


def productdetail(request, id):
    product = Product.objects.get(id=id)
    #size = Size.objects.get(product=Product.objects.get(id=id))
    review_query = Review.objects.filter(product=product.id)
    try:
        review0 = review_query[0]
    except:
        review0 = None
    try:
        review1 = review_query[1]
    except:
        review1 = None
    try:
        review2 = review_query[2]
    except:
        review2 = None
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)

    context = {
        'product': product,
        # 'size': size,
        'review0': review0,
        'review1': review1,
        'review2': review2,
        'cart': cart_obj,
        'wishlist': wishlist_obj,
    }
    return render(request, 'ecom/productview.html', context)


def search(request):

    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)
        lookup = Q(name__icontains=q) | Q(description__icontains=q) | Q(category__icontains=q) | Q(filters__icontains=q)
        products = Product.objects.filter(lookup)
        context = {'query': q, 'products': products, 'cart': cart_obj, 'wishlist': wishlist_obj, }
        template = 'ecom/results.html'
    else:
        context = {}
        template = 'ecom/home.html'
    return render(request, template, context)


from .filters import ProductFilter


def searchfilter(request):
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'ecom/product_list.html', {'filter': product_filter})
