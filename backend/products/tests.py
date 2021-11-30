from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import json
from django.forms.models import model_to_dict

import factory

from products.models import Product
from users.models import User
from products.factory import (
    ProductFactory,
    ProductDescriptionFactory,
    ProductImageFactory,
    ProductCategoryFactory,
    SKUFactory
)
from users.models import User


class ProductTests(APITestCase):
    @classmethod
    def setUpClass (cls):
        super(ProductTests, cls).setUpClass()
        User.objects.create_superuser(email="farooqseedat@gmail.com",password="123456fs")
        
    def setUp (self):
        self.product_json={
            "skus": [
                {
                    "size": "8",
                    "color": "",
                    "price": "4241",
                    "currency": "GBP",
                    "sku_id": "32620985843809",
                    "out_of_stock": "False"
                },
                {
                    "size": "10",
                    "color": "",
                    "price": "4200",
                    "currency": "GBP",
                    "sku_id": "32620985876577",
                    "out_of_stock": "False"
                }
            ],
            "description": [
            {"description": "Glamorous Women’s Blue Pink Rose Satin Midi Wrap Dress"}
            ],
            "image_urls": [
                {"url":"https://cdn.shopify.com/s/files/1/0265/1760/2401/products/CK55161_150x150.jpg?v=1597150676"},
            ],
            "category": [
                {"category":"Blue Pink Rose Satin Midi Dress"}
            ],
            "gender": "women",
            "currency": "GBP",
            "price": "4203",
            "market": "UK",
            "retailer": "glamorous-uk",
            "retailer_sku": "CK5516-CJ33-XS",
            "brand": "Glamorous",
            "url": "https://www.glamorous.com/products/blue-pink-rose-satin-midi-dress",
            "url_original": "https://www.glamoro2us.xcom/collections/dresses/producssts/blue-pink3-rose-satin-midi-dress",
            "product_hash": "4726805233761glamorous_uk_crawl",
            "name": "Blue Pink Rose Satin Midi Dress",
            "spider_name": "glamorous-uk-crawl"
        }
        self.client.login(username="farooqseedat@gmail.com",password="123456fs")

    def test_empty_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']),0)
    
    def test_product_list(self):
        url = reverse('product-list')
        product_data = ProductFactory.create_batch(5)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']),5)
     
    def test_product_create_unauthorized(self):
        url = reverse('product-list')
        self.client.logout()
        response = self.client.post(url, self.product_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Product.objects.count(),0)

    def test_product_create_authorized(self):
        url = reverse('product-list')
        response = self.client.post(url, self.product_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(),1)

    def test_create_duplicate_product(self):
        url = reverse('product-list')
        response = self.client.post(url, self.product_json, format='json')
        response = self.client.post(url, self.product_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(),1)

    def test_update_product(self):
        url_create = reverse('product-list')
        response = self.client.post(url_create, self.product_json, format='json')
        product = response.data
        url = reverse('product-detail', args=[product.get("id")])
        response = self.client.put(url, data=self.product_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product_unauthorized(self):
        url_create = reverse('product-list')
        response = self.client.post(url_create, self.product_json, format='json')
        self.assertEqual(Product.objects.count(),1)
        product = response.data
        url = reverse('product-detail', args=[product.get("id")])
        self.client.logout()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Product.objects.count(),1)
        
    def test_delete_product(self):
        url_create = reverse('product-list')
        response = self.client.post(url_create, self.product_json, format='json')
        self.assertEqual(Product.objects.count(),1)
        product = response.data
        url = reverse('product-detail', args=[product.get("id")])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(),0)
    