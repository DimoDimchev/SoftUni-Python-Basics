days=int(input())
bakers=int(input())
cakes=int(input())
gofret=int(input())
pancakes=int(input())

money= days*(bakers*cakes*45.0)+days*(bakers*gofret*5.80)+days*(bakers*pancakes*3.20)
total=money-((1/8)*money)

print(total)