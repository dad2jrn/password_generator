def leet(pwd):
    # print(f"Original word is: {pwd} and has been modified to meet password contraints.\n\n")
    for char in pwd:
        if char == "a":
            pwd = pwd.replace("a", "4")
        # elif char == "b":
        #     pwd = pwd.replace("b", "8")
        elif char == "e":
            pwd = pwd.replace("e", "3")
        elif char == "l":
            pwd = pwd.replace("l", "1")
        elif char == "o":
            pwd = pwd.replace("o", "0")
        elif char == "s":
            pwd = pwd.replace("s", "5")
        elif char == "t":
            pwd = pwd.replace("t", "7")
        else:
            pass
    return pwd
