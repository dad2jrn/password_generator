import secrets, string
from getlength import pwd_length


def passgen(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd = ""
    for i in range(int(length)):
        pwd += "".join(secrets.choice(alphabet))
    return pwd


if __name__ == "__main__":
    length = pwd_length()
    print(passgen(length))
