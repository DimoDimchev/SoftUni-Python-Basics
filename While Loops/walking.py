command = input()

success = False
total_steps = 0

while command != "Going home":
    steps_made = int(command)
    total_steps += steps_made
    if total_steps >= 10000:
        difference = total_steps - 10000
        success = True
        break
    command = input()

if success:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    command = int(input())
    total_steps += command
    if total_steps < 10000:
        difference = 10000 - total_steps
        print(f"{difference} more steps to reach goal.")
    else:
        difference = total_steps - 10000
        print("Goal reached! Good job!")
        print(f"{difference} steps over the goal!")