# Generated by Django 2.2.5 on 2019-10-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0017_auto_20191015_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='ecom.Product'),
        ),
    ]
