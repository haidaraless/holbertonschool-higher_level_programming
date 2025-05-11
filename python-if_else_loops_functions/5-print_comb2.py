#!/usr/bin/python3
numbers = ["{:02d}".format(i) for i in range(100)]
print(*numbers, sep=", ")
