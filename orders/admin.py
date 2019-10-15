from django.contrib import admin
from .models import Billing, Order, Address

admin.site.register(Billing)
admin.site.register(Order)
admin.site.register(Address)
