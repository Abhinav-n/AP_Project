# Generated by Django 2.2.5 on 2019-10-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0014_auto_20191011_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='ecom.Product'),
        ),
    ]
