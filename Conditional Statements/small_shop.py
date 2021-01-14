product= input()
city= input()
amount=float(input())

total=0
priceCoffee=0
priceWater=0
priceBeer=0
priceSweets=0
pricePeanuts=0


if city=="Sofia":
    priceCoffee = 0.50
    priceWater = 0.80
    priceBeer = 1.20
    priceSweets = 1.45
    pricePeanuts = 1.60

    if product=="coffee":
        total= amount*priceCoffee
    elif product=="water":
        total = amount * priceWater
    elif product == "beer":
        total = amount * priceBeer
    elif product == "sweets":
        total = amount * priceSweets
    elif product == "peanuts":
        total = amount * pricePeanuts

    print(total)
elif city == "Plovdiv":
    priceCoffee = 0.40
    priceWater = 0.70
    priceBeer = 1.15
    priceSweets = 1.30
    pricePeanuts = 1.50

    if product == "coffee":
        total = amount * priceCoffee
    elif product == "water":
        total = amount * priceWater
    elif product == "beer":
        total = amount * priceBeer
    elif product == "sweets":
        total = amount * priceSweets
    elif product == "peanuts":
        total = amount * pricePeanuts

    print(total)
elif city == "Varna":
    priceCoffee = 0.45
    priceWater = 0.70
    priceBeer = 1.10
    priceSweets = 1.35
    pricePeanuts = 1.55

    if product == "coffee":
        total = amount * priceCoffee
    elif product == "water":
        total = amount * priceWater
    elif product == "beer":
        total = amount * priceBeer
    elif product == "sweets":
        total = amount * priceSweets
    elif product == "peanuts":
        total = amount * pricePeanuts

    print(total)