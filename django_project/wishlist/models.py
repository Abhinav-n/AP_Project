from django.db import models
from django.contrib.auth.models import User
from ecom.models import Product


class WishlistManager(models.Manager):
    def new_or_get(self, request):
        wishlist_id = request.session.get("wishlist_id", None)
        qs = Wishlist.objects.filter(id=wishlist_id)
        if qs.count() == 1:
            new_obj = False
            wishlist_obj = qs.first()
            if request.user.is_authenticated and wishlist_obj.user is None:
                wishlist_obj.user = request.user
                wishlist_obj.save()
        else:
            wishlist_obj = Wishlist.objects.new(user=request.user)
            new_obj = True
            request.session['wishlist_id'] = wishlist_obj.id
        return wishlist_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Wishlist(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    objects = WishlistManager()

    def __str__(self):
        return str(self.id)
