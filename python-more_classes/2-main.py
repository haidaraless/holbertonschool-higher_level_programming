#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

rec = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(rec.area(), rec.perimeter()))

print("--")

rec.width = 10
rec.height = 3
print("Area: {} - Perimeter: {}".format(rec.area(), rec.perimeter()))
