from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm, GuestForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import GuestEmail
from django.utils.http import is_safe_url
from .forms import LoginForm
from carts.models import Cart
from ecom.models import Product
from orders.models import Order, Billing


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ecommerce-loggedin')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def userprofile(request):
    user = request.user
    cart_query = Cart.objects.filter(user=user)
    cart_obj0 = cart_query.first()
    try:
        cart_obj1 = cart_query[1]
    except:
        cart_obj1 = None
    try:
        cart_obj2 = cart_query[2]
    except:
        cart_obj2 = None
    context = {
        'cart0': cart_obj0,
        'cart1': cart_obj1,
        'cart2': cart_obj2,
    }
    return render(request, 'users/profile.html', context)


def edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'users/profile.html')

    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'users/edit.html', {'form': form})


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticated(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('home')
    return render(request, 'accounts/login.html', context)


def guest_page(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get("email")
        new_guest = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('register')
    return redirect('register')
