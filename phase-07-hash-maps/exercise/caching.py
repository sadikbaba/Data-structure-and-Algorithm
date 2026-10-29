def get_product(products, product_id, cache):
    # Your implementation
    if product_id in cache:
        return cache[product_id]
     
    for product in products:
        if product["id"] == product_id:
            cache[product_id] = product
            return product
    return None

if __name__ == "__main__":
    products = [
        {"id": 101, "name": "Airtime"},
        {"id": 102, "name": "Data Bundle"},
        {"id": 103, "name": "Electricity"},
    ]

    cache = {}

    print(get_product(products, 101, cache))
    print(get_product(products, 101, cache))
    print(get_product(products, 102, cache))
    print(get_product(products, 103, cache))
    print(get_product(products, 999, cache))
