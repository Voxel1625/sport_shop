from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Text')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Categories') #силка на таблицю категоріі в подкласі Мета
    price = models.DecimalField(max_digits=10, decimal_places=2)
# Foreignkey - метод, який вказує що звязок між продуктами і категоріями багато до одного (багато продуктів належать одній категорії)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    class Meta:
        verbose_name = "Popular product"
        verbose_name_plural = "Popular products"



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Category "
        verbose_name_plural = "Categories"
        ordering = ['id']
