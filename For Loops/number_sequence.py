import sys

n= int(input())

max_number=-sys.maxsize
min_number=sys.maxsize

for i in range(1,n+1):
    number = int(input())
    if number>max_number:
        max_number=number

    if number<min_number:
        min_number=number


print(f"Max number: {max_number}")
print(f"Min number: {min_number}")