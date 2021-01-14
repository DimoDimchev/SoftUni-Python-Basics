number = int(input())

bonus = float
bonus = 0

if number % 2 == 0:
    bonus += 1

if number % 10 == 5:
    bonus += 2

if number < 100:
    bonus += 5
elif number > 1000:
    bonus += (10 / 100) * number
else:
    bonus += (20 / 100) * number

number += bonus

print(bonus)
print(number)