from rest_framework import serializers
from django.db import transaction

from products.models import Product, SKU, ProductImage
from products.models import ProductCategory, ProductDescription


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['size', 'color', 'price', 'currency', 'sku_id','out_of_stock']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields =['url']

    def to_representation(self, instance):
        return instance.url


class ProductDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDescription
        fields = ['description']

    def to_representation(self, instance):
        return instance.description


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category']

    def to_representation(self, instance):
        return instance.category


class ProductSerializer(serializers.ModelSerializer):
    skus = SKUSerializer(many=True)
    description = ProductDescriptionSerializer(many=True)
    image_urls = ProductImageSerializer(many=True)
    category = ProductCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create_skus(self, validated_skus, product):
        skus_serializer = self.fields['skus']
        for each in validated_skus:
            each['product'] = product
        skus = skus_serializer.create(validated_skus)

    def create_descriptions(self, validated_descriptions, product):
        product_description_serializer = self.fields['description']
        for each in validated_descriptions:
            each['product'] = product
        description = product_description_serializer.create(validated_descriptions)

    def create_product_images(self, validated_image_urls, product):
        product_image_serializer = self.fields['image_urls']
        for each in validated_image_urls:
            each['product'] = product
        image_urls = product_image_serializer.create(validated_image_urls)

    def create_categories(self, validated_categories, product):
        category_serializer = self.fields['category']
        for each in validated_categories:
            each['product'] = product
        category = category_serializer.create(validated_categories)

    @transaction.atomic
    def create(self, validated_data):
        validated_skus = validated_data.pop('skus', [])
        validated_image_urls = validated_data.pop('image_urls', [])
        validated_categories = validated_data.pop('category', [])
        validated_descriptions = validated_data.pop('description', [])
        product = super().create(validated_data)
        self.create_skus(validated_skus, product)
        self.create_descriptions(validated_descriptions, product)
        self.create_product_images(validated_image_urls, product)
        self.create_categories(validated_categories, product)
        return product

    def update(self, instance, validated_data):
        validated_skus = validated_data.pop('skus', [])
        validated_image_urls = validated_data.pop('image_urls', [])
        validated_categories = validated_data.pop('category', [])
        validated_descriptions = validated_data.pop('description', [])
        product = super().update(instance, validated_data)
        self.update_skus(validated_skus, product)
        return product

    def update_skus(self, validated_skus, product):
        existing_skus = SKU.objects.filter(product=product)
        for sku in validated_skus:
            sku['product'] = product
            existing_skus.update_or_create(sku_id=sku.get("sku_id"),defaults=sku)
                
        return existing_skus
