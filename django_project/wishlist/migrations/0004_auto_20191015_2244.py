# Generated by Django 2.2.5 on 2019-10-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0003_auto_20191015_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(blank=True, to='ecom.Product'),
        ),
    ]