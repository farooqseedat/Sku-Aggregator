from random import randint

import factory
from faker import Factory

from products.models import (
    Product,
    ProductCategory,
    ProductDescription,
    ProductImage,
    SKU
)

faker = Factory.create()

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    price = faker.random_int()
    currency = faker.currency_name()
    gender = faker.random_element(elements=("male", "female", "unisex"))
    market = faker.random_element(elements=("GB", "Europe"))
    retailer = faker.random_element(elements=("glamorous", "europe361"))
    retailer_sku = faker.random_number(digits=10)
    brand = retailer
    url = faker.url()
    url_original = url
    product_hash = factory.LazyAttributeSequence(lambda o, n: f"{n}{o.retailer}")
    name = faker.sentence(nb_words=10)
    spider_name = f"{retailer}-crawl"

    
        
    @factory.post_generation
    def create_fk_attributes(obj, create, extracted, **kwargs):
        if not create:
            return
        SKUFactory.create_batch(randint(1,9), product=obj)
        ProductImageFactory.create_batch(randint(1,9), product=obj)
        ProductDescriptionFactory.create_batch(randint(1,9), product=obj)
        ProductCategoryFactory.create_batch(randint(1,9), product=obj)
    

class SKUFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SKU

    color = faker.color_name()
    sku_id = faker.random_number()
    price = faker.random_int()
    size = faker.random_int(max=99)
    currency = faker.currency_name()
    out_of_stock = faker.pybool()
    product = factory.SubFactory(ProductFactory)


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductCategory

    category = faker.word()
    product = factory.SubFactory(ProductFactory)
    

class ProductDescriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductDescription

    description = faker.paragraph(nb_sentences=10)
    product = factory.SubFactory(ProductFactory)


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    url = faker.image_url()
    product = factory.SubFactory(ProductFactory)
