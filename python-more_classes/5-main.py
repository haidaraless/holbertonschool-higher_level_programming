#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

rec = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(rec.area(), rec.perimeter()))

del rec

try:
    print(rec)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
