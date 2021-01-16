money_needed = float(input())
starting_money = float(input())

days_spending = 0
total_days = 0

command = input()
command_money = float(input())

finished = False

while starting_money < money_needed:
    if command == "spend":
        if command_money > starting_money:
            starting_money = 0
            days_spending += 1
            total_days += 1
        else:
            starting_money -= command_money
            days_spending += 1
            total_days += 1
    elif command == "save":
        starting_money = starting_money + command_money
        days_spending = 0
        total_days += 1

    if days_spending == 5:
        break

    if starting_money >= money_needed:
        finished = True
        break

    command = input()
    command_money = float(input())

if finished:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(f"{total_days}")