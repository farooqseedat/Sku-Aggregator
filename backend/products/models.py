from django.db import models


class Product(models.Model):
    gender = models.CharField(max_length=15)
    currency = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    market = models.CharField(max_length=20, blank=True, default='')
    retailer = models.CharField(max_length=20)
    retailer_sku = models.CharField(max_length=20, blank=True, default='')
    brand = models.CharField(max_length=30)
    url = models.URLField()
    url_original = models.URLField()
    product_hash = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    spider_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.id}/{self.name}"


class SKU(models.Model):
    color = models.CharField(max_length=30, blank=True, default='')
    currency = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    sku_id = models.BigIntegerField()
    out_of_stock = models.BooleanField()
    size = models.CharField(max_length=30)
    product = models.ForeignKey(
        Product,
        related_name='skus',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.product.id}/{self.sku_id}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='image_urls',
        on_delete=models.CASCADE
    )
    url = models.URLField()

    def __str__(self):
        return f"{self.product.id}/{self.url}"


class ProductDescription(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='description',
        on_delete=models.CASCADE
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.product.id}/{self.description}"


class ProductCategory(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='category',
        on_delete=models.CASCADE
    )
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product.id}/{self.category}"
