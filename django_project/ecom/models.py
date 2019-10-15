from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='')
    category = models.CharField(max_length=100, default='')
    filters = models.CharField(max_length=100, default='')
    average_rating = models.FloatField(default=0)
    number_of_reviews = models.IntegerField(default=0)
    image = models.URLField(default='')
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


#class Size(models.Model):
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #size = models.CharField(max_length=5)

    #def __str__(self):
        #return self.size


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    review = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.review
