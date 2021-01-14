import sys

n=int(input())
max=-sys.maxsize
sum=0

for i in range(0,n):
    number=int(input())
    if number>max:
        max=number
    sum+=number

if max==sum-max:
    print("Yes")
    print(f"Sum = {max}")
else:
    print("No")
    print(f"Diff = {abs((sum-max)-max)}")