#!/usr/bin/python3
def islower(c):
    return ord(c) >= 97 and ord(c) <= 122

if (islower(c)):
    print(f"{c} is lower")
else:
    print(f"{c} is upper")
