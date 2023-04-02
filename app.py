import random, 

print("Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()_-+={[}]|:;'<,>.?/"

def passgen():
    password = ''
    length = input("How many characters for your password? ")
    plength = int(length)
    print(f"Here is your new {plength} character password")
    for c in range(plength):
        password += random.choice(chars)
    return password


print(passgen())
