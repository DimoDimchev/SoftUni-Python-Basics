import sys

user_input = input()

min_num = sys.maxsize

while user_input != "Stop":
    string_num = int(user_input)
    if string_num < min_num:
        min_num = string_num
    user_input = input()

print(min_num)