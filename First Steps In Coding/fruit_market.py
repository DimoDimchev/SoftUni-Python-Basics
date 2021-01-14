price_r=float(input())
price_m=price_r*(1/2)
price_o=price_m-((40/100)*price_m)
price_b=price_m-((80/100)*price_m)

amount_b=float(input())
amount_o=float(input())
amount_m=float(input())
amount_r=float(input())

total=price_r*amount_r+price_b*amount_b+price_o*amount_o+price_m*amount_m
print(total)