#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            u = chr(ord(str) - 32)
        print("{}".format(u), end="")
    print()
