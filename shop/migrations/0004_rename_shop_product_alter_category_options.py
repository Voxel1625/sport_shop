# Generated by Django 4.2.1 on 2023-06-21 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_category_options_alter_shop_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shop',
            new_name='Product',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Category ', 'verbose_name_plural': 'Categories'},
        ),
    ]
