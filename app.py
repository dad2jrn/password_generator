import random, requests as req, json
from word import getword

print("///////////  Password Generator  ////////////\n\n")




def passgen():
    myword = getword()
    print(myword)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()_-+={[}]|:;'<,>.?/"
    password = ''
    length = input("How many characters for your password? ")
    totallength = int(length)
    print(f"Here is your new {totallength} character password")
    rlength = len(myword)
    for c in range(rlength):
        password += random.choice(chars)
    return myword + password


print(passgen())
