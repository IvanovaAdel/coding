products = [("Хлеб", 40, 12), ("Молоко", 60, 83), ("Яблоки", 100, 41)]
for product in products:
    print(f"Товар: {product[0]}, цена: {product[1]}")

def price_less_than_eighty():
    for product in products:
        if product[1] < 80:
            print(product[1])
        else:
            continue
price_less_than_eighty()

def total_amount_of_item(): 
    for product in products: 
        full_price = int(product[1]) * int(product[2])
        print(f"Цена товара {product[0]} - всего {full_price}")
total_amount_of_item()

prices = []
def item_with_the_highest_amount():
    global prices
    for product in products: 
        full_prices = int(product[1]) * int(product[2])
        prices.append(full_prices)
    prices.sort()
    prices.reverse()
    print(prices)
    for product in products:
        if (int(product[1]) * int(product[2])) == prices[0]:
            name = product[0]
            if (int(product[1]) * int(product[2])) == prices[0]:
                print(f"Самая большая цена у товара {name} - {prices[0]}")
item_with_the_highest_amount()

def total_amount_of_goods():
    global prices
    total_prices = sum(prices)
    print(f"Общая цена товаров - {total_prices}")
total_amount_of_goods()
