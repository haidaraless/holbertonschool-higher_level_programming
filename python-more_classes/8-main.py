#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

rec_1 = Rectangle(8, 4)
rec_2 = Rectangle(2, 3)

if rec_1 is Rectangle.bigger_or_equal(rec_1, rec_2):
    print("rec_1 is bigger or equal to rec_2")
else:
    print("rec_2 is bigger than rec_1")


rec_2.width = 10
rec_2.height = 5
if rec_1 is Rectangle.bigger_or_equal(rec_1, rec_2):
    print("rec_1 is bigger or equal to rec_2")
else:
    print("rec_2 is bigger than rec_1")
