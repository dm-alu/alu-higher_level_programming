#!/usr/bin/python3
def uppercase(str):
    for c in str:
        n = ord(c)
        if 97 <= n <= 122:
            n -= 32
        print("{}".format(chr(n)), end="")
    print("")
