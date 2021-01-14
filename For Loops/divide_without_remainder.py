n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

p1 = '{0:.2f}'.format(p1 / n * 100)
p2 = '{0:.2f}'.format(p2 / n * 100)
p3 = '{0:.2f}'.format(p3 / n * 100)

print(p1+"%")
print(p2+"%")
print(p3+"%")