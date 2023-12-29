from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, default=None)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    def __str__(self) -> str:
        return f"Mahsulot: {self.name} | Kategoriya: {self.category}"

    def save(self, *args, **kwargs):
        if not self.description:
            # Translate the 'name' field to Russian and set it as the default description
            self.description = _(f"{self.name} haqida ma'lumot: ...")
        super().save(*args, **kwargs)