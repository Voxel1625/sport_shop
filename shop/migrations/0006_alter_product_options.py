# Generated by Django 4.2.1 on 2023-06-29 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Popular product', 'verbose_name_plural': 'Popular products'},
        ),
    ]
