def find_product(products, product_id):
    lookup = {}
    for product in products:
        lookup[product["id"]] = product
    
    return lookup.get(product_id)


if __name__ == "__main__":
    products = [
        {"id": 101, "name": "Airtime", "price": 500},
        {"id": 102, "name": "Data", "price": 1500},
        {"id": 103, "name": "Electricity", "price": 3000},
    ]

    print(find_product(products, 101))
    print(find_product(products, 103))
    print(find_product(products, 999))




