# Generated by Django 2.2.5 on 2019-10-08 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0025_auto_20191008_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Product'),
        ),
        migrations.AlterField(
            model_name='size',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Product'),
        ),
    ]
