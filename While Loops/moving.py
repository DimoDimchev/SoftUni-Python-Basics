space_width = int(input())
space_lenght = int(input())
space_height = int(input())

space_volume = space_width * space_height * space_lenght

taken_space = 0

user_input = input()
failed = 0

while user_input != "Done":
    number_boxes = int(user_input)
    taken_space += number_boxes
    if space_volume < taken_space:
        failed += 1
        print(f"No more free space! You need {taken_space - space_volume} Cubic meters more.")
        break
    user_input = input()

if failed == 0:
    print(f"{space_volume - taken_space} Cubic meters left.")