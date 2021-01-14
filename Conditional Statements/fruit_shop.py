product= input()
day= input()
amount=float(input())

price=0;

if day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday":
    price_banana=2.50
    price_apple=1.20
    price_orange=0.85
    price_grapefruit=1.45
    price_kiwi=2.70
    price_pineapple=5.50
    price_grapes=3.85

    if product=="banana":
        price=price_banana*amount
        print('{0:.2f}'.format(price))
    elif product=="apple":
        price = price_apple * amount
        print('{0:.2f}'.format(price))
    elif product == "orange":
        price = price_orange * amount
        print('{0:.2f}'.format(price))
    elif product == "grapefruit":
        price = price_grapefruit * amount
        print('{0:.2f}'.format(price))
    elif product == "kiwi":
        price = price_kiwi * amount
        print('{0:.2f}'.format(price))
    elif product == "pineapple":
        price = price_pineapple * amount
        print('{0:.2f}'.format(price))
    elif product == "grapes":
        price = price_grapes * amount
        print('{0:.2f}'.format(price))
    else:
        print("error")

elif day=="Saturday" or day=="Sunday":
    price_banana=2.70
    price_apple=1.25
    price_orange=0.90
    price_grapefruit=1.60
    price_kiwi=3.00
    price_pineapple=5.60
    price_grapes=4.20

    if product=="banana":
        price=price_banana*amount
        print('{0:.2f}'.format(price))
    elif product=="apple":
        price = price_apple * amount
        print('{0:.2f}'.format(price))
    elif product == "orange":
        price = price_orange * amount
        print('{0:.2f}'.format(price))
    elif product == "grapefruit":
        price = price_grapefruit * amount
        print('{0:.2f}'.format(price))
    elif product == "kiwi":
        price = price_kiwi * amount
        print('{0:.2f}'.format(price))
    elif product == "pineapple":
        price = price_pineapple * amount
        print('{0:.2f}'.format(price))
    elif product == "grapes":
        price = price_grapes * amount
        print('{0:.2f}'.format(price))
    else:
        print("error")
else:
    print("error")