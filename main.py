import secrets, string

# store string module constants in vars
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# wrap string constants into a single var
alphabet = letters + digits + special_chars

pwd_length = input("Please chose the lenght of your password (recommended lenght is 12 or more).  ")

