# Generated by Django 2.2.5 on 2019-10-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_auto_20191008_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='ecom.Product'),
        ),
    ]
