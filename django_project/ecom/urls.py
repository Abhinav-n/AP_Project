from django.urls import path, include
from . import views
from users.views import guest_page
from carts.views import checkout_address
from wishlist.views import wishlist_home
urlpatterns = [
    path('', views.home, name='ecommerce-base'),
    path('men/', views.men, name='ecommerce-men'),
    path('home/', views.home, name='ecommerce-home'),
    path('women/', views.women, name='ecommerce-women'),
    path('s/', views.search, name='search'),
    path('filter/', views.searchfilter, name='searchfilter'),
    path('register/guest/', guest_page, name='guest_page'),
    path('checkout_address', checkout_address, name='checkout_address'),
    path('kids/', views.kids, name='ecommerce-kids'),
    path('loggedin/', views.loggedin, name='ecommerce-loggedin'),
    path('accounts/', include('allauth.urls')),
    path('cart/', views.cart, name='ecommerce-cart'),
    path('productview/<int:id>/', views.productdetail, name="detail")

]
