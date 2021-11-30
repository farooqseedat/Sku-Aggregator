from django.contrib import admin

from products.models import (
    Product, SKU,
    ProductImage, ProductCategory,
    ProductDescription
)


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductDescription)
admin.site.register(ProductImage)
admin.site.register(SKU)
