from django.db import models
from django.contrib.auth.models import User
from ecom.models import Product


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):

    products = models.ManyToManyField(Product, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)
