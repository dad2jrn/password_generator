from word import getword
from leet import leet
from constraints import append


if __name__ == "__main__":
    length = input("How long of a word?  ")
    pwd = getword(length)
    print(f"For readability the original word is: {pwd}\n\n")
    modify_pwd = leet(pwd)
    final_pwd = append(modify_pwd)
    print(final_pwd)
