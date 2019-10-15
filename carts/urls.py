from django.conf.urls import url
from django.urls import path, include
from .views import cart_home, cart_update, checkout, checkout_success

urlpatterns = [
    path('', cart_home, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('update/', cart_update, name='update'),
    path('success/', checkout_success, name='checkout_success'),
]
