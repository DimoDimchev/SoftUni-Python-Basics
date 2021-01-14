hour= int(input())
day=input()

if day=="Sunday" or hour>18 or hour<10:
    print("closed")
else:
    print("open")