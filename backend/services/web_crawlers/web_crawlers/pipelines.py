# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting


# useful for handling different item types with a single interface
import requests
import json

from itemadapter import ItemAdapter

from users.authentication import get_access_token, get_jwt_token


def map_list_data(data, field_name):
    mapped_data = []
    for each in data or []:
        mapped_data.append({field_name:each})
    return mapped_data


class ProductPipeline:

    def __init__(self):

        print("*****")
        tokens = get_jwt_token()
        self.refresh_token = tokens.get("refresh")
        self.access_token = tokens.get("access")
        self.url = 'http://api-sku-aggregator.com:8000/products/'
    

    def process_item(self, item, spider):
        item['image_urls'] = map_list_data(item.get('image_urls'), 'url')
        item['category'] = map_list_data(item.get('category'), 'category')
        item['description'] = map_list_data(item.get('description'), 'description')
        item['product_hash'] = f"{item.get('product_hash')}{spider.name}"
        
        adapter = ItemAdapter(item)
        json_string = json.dumps(adapter.asdict())
        json_serialized_obj = json.loads(json_string)
        
        status = requests.post(
            self.url, json=json_serialized_obj,
            headers={"Authorization": f"Bearer {self.access_token}"}
        )

        if status.status_code == 403:
            print(status.json())
            self.access_token = get_access_token(self.refresh_token)
            if self.access_token:
                status = requests.post(
                    self.url, json=json_serialized_obj,
                    headers= {"Authorization": f"Bearer {self.access_token}"}
                )

        if status.status_code!=201:
            print(json_serialized_obj['url'])
            print(status.json())
        return item
