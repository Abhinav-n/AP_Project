from django.shortcuts import render, redirect
from .models import Cart, Product
from orders.models import Order, Billing, Address
from users.forms import LoginForm
from users.models import GuestEmail
from users.forms import GuestForm
from orders.forms import AddressForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for i in products:
        total = total + i.price
    cart_obj.total = total
    cart_obj.save()
    context = {
        'cart': cart_obj,
    }
    return render(request, "carts/home.html", context)


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        product_obj = Product.objects.get(id=product_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    products = cart_obj.products.all()
    count = 0
    for i in products:
        count = count + 1
    cart_obj.count = count
    cart_obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def checkout(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    order_obj = None
    if new_obj or cart_obj.products.count() == 0:
        return redirect('home')
    user = request.user
    billing = None
    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    guest_email_id = request.session.get('guest_email_id')

    if user.is_authenticated:
        billing, billing_created = Billing.objects.get_or_create(user=user, email=user.email)
    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing, billing_created = Billing.objects.get_or_create(email=guest_email_obj.email)
    else:
        pass

    address_query = None
    if billing is not None:
        address_query = Address.objects.filter(billing=billing)
        order_query = Order.objects.filter(billing=billing, cart=cart_obj, active=True)
        if order_query.count() == 1:
            order_obj = order_query.first()
        else:
            old_order_query = Order.objects.exclude(billing=billing).filter(cart=cart_obj)
            if old_order_query.exists():
                old_order_query.update(active=False)
            order_obj = Order.objects.create(billing=billing, cart=cart_obj)

    context = {
        'order': order_obj,
        'billing': billing,
        'guest_form': guest_form,
        'login_form': login_form,
        'address_form': address_form,
        'address_query': address_query,
    }
    return render(request, 'carts/checkout.html', context)


def checkout_address(request):
    form = AddressForm(request.POST)
    if form.is_valid():
        check_address = form.save(commit=False)
        guest_email_id = request.session.get('guest_email_id')
        user = request.user
        if user.is_authenticated:
            billing, billing_created = Billing.objects.get_or_create(user=user, email=user.email)
        elif guest_email_id is not None:
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            billing, billing_created = Billing.objects.get_or_create(email=guest_email_obj.email)
        else:
            pass
        if billing is not None:
            check_address.user = user
            check_address.billing = billing
            check_address.save()
        else:
            print(error)
            return redirect('home')
    return redirect('checkout_success')


def checkout_success(request):
    del request.session['cart_id']  # clearing the cart
    return render(request, 'carts/success.html', {})
