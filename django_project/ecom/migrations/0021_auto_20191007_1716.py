# Generated by Django 2.2.5 on 2019-10-07 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0020_auto_20191007_1642'),
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
