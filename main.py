import secrets, string

# store string module constants in vars
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# wrap string constants into a single var
alphabet = letters + digits + special_chars

print(alphabet)