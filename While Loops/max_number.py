import sys

user_input = input()

max_num = -sys.maxsize

while user_input != "Stop":
    string_num = int(user_input)
    if string_num > max_num:
        max_num = string_num
    user_input = input()

print(max_num)