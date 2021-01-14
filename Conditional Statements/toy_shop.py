price_puzzle=2.60
price_doll=3.0
price_bear=4.1
price_minion=8.2
price_truck=2.0

price_trip= float(input())

puzzles=int(input())
dolls=int(input())
bears=int(input())
minions=int(input())
trucks=int(input())

total_toys=puzzles+dolls+bears+minions+trucks

price_toys= puzzles*price_puzzle+dolls*price_doll+bears*price_bear+minions*price_minion+trucks*price_truck

price_toys=price_toys-((10/100)*price_toys)

if total_toys>=50:
    price_toys= price_toys-((25/100)*price_toys)

if price_toys>=price_trip:
    print(f"Yes! {'{:.2f}'.format(price_toys-price_trip)} lv left.")
else:
    print(f"Not enough money! {'{:.2f}'.format(price_trip-price_toys)} lv needed.")