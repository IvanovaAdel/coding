products = [("Хлеб", 40, 12), ("Молоко", 60, 83), ("Яблоки", 100), 41]
for product in products:
    print(f"Товар: {product[0]}, цена: {product[1]}")

def price_less_than_eighty():
    for product in products:
        if product[1] < 80:
            print(product[1])
        else:
            continue
print(price_less_than_eighty())
