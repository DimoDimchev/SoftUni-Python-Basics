budget= float(input())
actors=int(input())
clothes=float(input())
scene= (10/100)*budget

price_clothes= clothes*actors

if actors>150:
    price_clothes= price_clothes-((10/100)*price_clothes)

total_price= scene+price_clothes
if budget>=total_price:
    print("Action!")
    print(f"Wingard starts filming with "+ '{0:.2f}'.format(budget-total_price)+" leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs "+ '{0:.2f}'.format(total_price-budget)+" leva more.")