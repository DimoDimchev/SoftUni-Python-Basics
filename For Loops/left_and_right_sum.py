n=int(input())

total1=0
total2=0

for i in range(1,n+1):
    number=int(input())
    total1+=number

for i in range(1,n+1):
    number=int(input())
    total2+=number

if total1==total2:
    print(f"Yes, sum = {total1}")
else:
    print(f"No, diff = {abs(total1-total2)}")



