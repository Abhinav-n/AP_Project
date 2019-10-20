from django.shortcuts import render, redirect
from ecom.models import Product
from .models import Wishlist
from django.http import HttpResponseRedirect
from carts.models import Cart


def wishlist_home(request):
    wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = wishlist_obj.products.all()
    total = 0
    for i in products:
        total = total + i.price
    print(total)
    wishlist_obj.total = total
    wishlist_obj.save()
    context = {
        'wishlist': wishlist_obj,
        'cart': cart_obj,
    }
    return render(request, "wishlist/home.html", context)


def wishlist_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        product_obj = Product.objects.get(id=product_id)
        wishlist_obj, new_obj = Wishlist.objects.new_or_get(request)
        if product_obj in wishlist_obj.products.all():
            wishlist_obj.products.remove(product_obj)
        else:
            wishlist_obj.products.add(product_obj)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
