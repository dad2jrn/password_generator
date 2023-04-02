import secrets, string

def passgen(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars

    pwd = ''
    for i in range(int(pwd_length)):
    pwd += ''.join(secrets.choice(alphabet))

    return pwd)