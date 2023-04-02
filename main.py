import secrets, string
from getlength import pwd_length


def passgen(length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd = ""
    while True:
        for i in range(int(length)):
            pwd += "".join(secrets.choice(alphabet))
        # Loop until we meet defined password contraints
        if (
            any(char in special_chars for char in pwd)
            and sum(char in digits for char in pwd) >= 2
        ):
            break
    return pwd


if __name__ == "__main__":
    length = pwd_length()
    print(passgen(length))
