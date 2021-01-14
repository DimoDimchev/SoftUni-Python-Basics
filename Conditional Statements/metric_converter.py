number= float(input())
metric1= input()
metric2= input()

if metric1=="m" and metric2=="cm":
    number=number*100
    print('{0:.3f}'.format(number))
elif metric1=="cm" and metric2=="mm":
    number=number*10
    print('{0:.3f}'.format(number))
elif metric1=="m" and metric2=="mm":
    number=number*1000
    print('{0:.3f}'.format(number))
elif metric1=="cm" and metric2=="m":
    number=number/100
    print('{0:.3f}'.format(number))
elif metric1=="mm" and metric2=="cm":
    number=number/10
    print('{0:.3f}'.format(number))
elif metric1=="mm" and metric2=="m":
    number=number/1000
    print('{0:.3f}'.format(number))
else:
    print('{0:.3f}'.format(number))