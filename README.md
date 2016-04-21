AliExpress API Client
============

Python client library for AliExpress API

Usage example
------------

**Configuration:**
``` python
from aliexpress_api_client import AliExpress

aliexpress = AliExpress('api_key', 'affiliate_id')
```

**Get product list:**
``` python
products = aliexpress.get_product_list(['productId', 'productTitle', 'salePrice'])

for product in products:
    print '#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice'])
```

**Get product details:**
``` python
product = aliexpress.get_product_details(['productId', 'productTitle', 'salePrice'], product_id)

print '#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice'])
```

**Get promotion links (require `affiliate_id`):**
```
links = api.get_promotion_links(['url', 'promotionUrl'], urls)

for link in links['promotionUrls']:
    print '%s: %s' % (link['url'], link['promotionUrl'])
```
