age= int(input())
machine_price=float(input())
toy_price=int(input())

money_received=0
money_per_birthday=10
toy_money=0
money_lost=0
money_saved=0

for i in range(1,age+1):
    if i%2==0:
        money_received+=money_per_birthday
        money_lost+=1
        money_per_birthday+=10
    else:
        toy_money+=toy_price

money_saved=(toy_money+money_received)-money_lost

if money_saved>=machine_price:
    print("Yes! "+'{0:.2f}'.format(money_saved-machine_price))
else:
    print("No! "+'{0:.2f}'.format(machine_price-money_saved))