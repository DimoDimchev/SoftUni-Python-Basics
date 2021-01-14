import sys

n=int(input())

OddSum=0
OddMin=sys.maxsize
OddMax=-sys.maxsize

EvenSum=0
EvenMin=sys.maxsize
EvenMax=-sys.maxsize

for i in range(1,n+1):
    number=float(input())
    if i%2==0:
        EvenSum+=number
        if number<EvenMin:
            EvenMin=number
        if number>EvenMax:
            EvenMax=number
    else:
        OddSum += number
        if number < OddMin:
            OddMin = number
        if number > OddMax:
            OddMax = number


if n==0:
    print(f"OddSum=" + '{0:.2f}'.format(OddSum)+",")
    print("OddMin=No"+",")
    print("OddMax=No"+",")
else:
    print(f"OddSum=" + '{0:.2f}'.format(OddSum)+",")
    print(f"OddMin=" + '{0:.2f}'.format(OddMin)+",")
    print(f"OddMax=" + '{0:.2f}'.format(OddMax)+",")

if n==1 or n==0:
    print(f"EvenSum=" + '{0:.2f}'.format(EvenSum)+",")
    print("EvenMin=No"+",")
    print("EvenMax=No"+"")
else:
    print(f"EvenSum=" + '{0:.2f}'.format(EvenSum)+",")
    print(f"EvenMin=" + '{0:.2f}'.format(EvenMin)+",")
    print(f"EvenMax=" + '{0:.2f}'.format(EvenMax))

