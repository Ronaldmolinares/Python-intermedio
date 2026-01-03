items = [
    {
        "name": "Laptop",
        "price": 1200,
    },
    {
        "name": "Smartphone",
        "price": 800,
    },
    {
        "name": "Tablet",
        "price": 400,
    },
]

prices = list(map(lambda item: item["price"], items))
print(prices)

# iva = list(map(lambda price: price + price * 0.19, prices))
# print(iva)

# for product, total_price in zip(items, iva):
#     product["price_iva"] = total_price

# print(items)


# forma del video:
def total_price1(item):
    item["value"] = item["price"] * 0.19
    return item


result = list(map(total_price1, items))
print(result)
