n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif 400 <= number <= 599:
        p3 += 1
    elif 600 <= number <= 799:
        p4 += 1
    else:
        p5 += 1

p1 = '{0:.2f}'.format(p1 / n * 100)
p2 = '{0:.2f}'.format(p2 / n * 100)
p3 = '{0:.2f}'.format(p3 / n * 100)
p4 = '{0:.2f}'.format(p4 / n * 100)
p5 = '{0:.2f}'.format(p5 / n * 100)

print(p1+"%")
print(p2+"%")
print(p3+"%")
print(p4+"%")
print(p5+"%")