from django.conf.urls import url
from django.urls import path, include
from .views import wishlist_home, wishlist_update

urlpatterns = [
    path('', wishlist_home, name='wishlist_home'),
    path('wishlist_update/', wishlist_update, name='wishlist_update'),
]
