import secrets, string

# store string module constants in vars
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

pwd_length = input("Please chose the lenght of your password (recommended lenght is 12 or more).  ")

pwd = ''
for i in range(int(pwd_length)):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)