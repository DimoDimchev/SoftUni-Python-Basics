deposited=float(input())
lenghtd=int(input())
interest=(float(input()))/100

total = deposited + lenghtd*((deposited*interest)/12)

print(total)