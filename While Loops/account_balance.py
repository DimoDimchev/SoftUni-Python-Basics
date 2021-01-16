text = input()

total_money = 0

while text != "NoMoreMoney":
    sum_string = float(text)
    if sum_string <= 0:
        print("Invalid operation!")
        break
    total_money += sum_string
    print(f"Increase: {sum_string:.2f}")
    text = input()

print(f"Total: {total_money:.2f}")