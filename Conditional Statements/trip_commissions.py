city = input()
sales = float(input())

comission = 0

if city == "Sofia":
    if sales >= 0 and sales <= 500:
        comission = (5 / 100) * sales
        print('{0:.2f}'.format(comission))
    elif sales > 500 and sales <= 1000:
        comission = (7 / 100) * sales
        print('{0:.2f}'.format(comission))
    elif sales > 1000 and sales <= 10000:
        comission = (8 / 100) * sales
        print('{0:.2f}'.format(comission))
    elif sales > 10000:
        comission = (12 / 100) * sales
        print('{0:.2f}'.format(comission))
    else:
        print("error")

elif city == "Varna":
    if sales >= 0 and sales <= 500:
        comission = (4.5 / 100) * sales
        print('{0:.2f}'.format(comission))
    elif sales > 500 and sales <= 1000:
        comission = (7.5 / 100) * sales
        print('{0:.2f}'.format(comission))
    elif sales > 1000 and sales <= 10000:
        comission = (10 / 100) * sales
        print('{0:.2f}'.format(comission))
    elif sales > 10000:
        comission = (13 / 100) * sales
        print('{0:.2f}'.format(comission))
    else:
        print("error")

elif city == "Plovdiv":
    if sales >= 0 and sales <= 500:
        comission = (5.5 / 100) * sales
        print('{0:.2f}'.format(comission))
    elif sales > 500 and sales <= 1000:
        comission = (8 / 100) * sales
        print('{0:.2f}'.format(comission))
    elif sales > 1000 and sales <= 10000:
        comission = (12 / 100) * sales
        print('{0:.2f}'.format(comission))
    elif sales > 10000:
        comission = (14.5 / 100) * sales
        print('{0:.2f}'.format(comission))
    else:
        print("error")

else:
    print("error")