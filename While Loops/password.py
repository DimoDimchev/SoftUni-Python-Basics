username = input()
password = input()
password_check = input()

while password_check != password:
    password_check = input()

print(f"Welcome {username}!")