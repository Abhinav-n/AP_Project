from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from carts.views import cart_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('carts.urls'), name='cart'),
    path('wishlist/', include('wishlist.urls'), name='wishlist'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.userprofile, name='profile'),
    path('edit/', user_views.edit, name='edit'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('ecom.urls')),
]
