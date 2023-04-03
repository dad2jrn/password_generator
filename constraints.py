import secrets, string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars


def append(pwd):
    while True:
        for i in range(2):
            pwd += "".join(secrets.choice(alphabet))

        if (
            any(char in special_chars for char in pwd)
            and sum(char in digits for char in pwd) >= 3
        ):
            break
    return pwd
