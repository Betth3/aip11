import csv

with open("products.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("Нужно купить:")

    total = 0

    for row in reader:
        name = row["Продукт"]
        quantity = int(row["Количество"])
        price = int(row["Цена"])
        cost = quantity * price
        total += cost
        print(f"{name} - {quantity} шт. за {price} руб.")

print(f"Итоговая сумма: {total} руб.")
