from django.db import models
from carts.models import Cart
from django.contrib.auth.models import User


class Billing(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Address(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,default='')
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    House = models.CharField(max_length=150)
    Postalcode = models.CharField(max_length=6)
    City = models.CharField(max_length=150)
    State = models.CharField(max_length=150)

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    billing = models.ForeignKey(Billing, null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def checkdone(self):
        billing = self.billing
        address = self.address
        total = self.address
        if billing and address and total > 0:
            return True
        return False
