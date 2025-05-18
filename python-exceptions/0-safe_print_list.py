#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printedItems = 0

    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            printedItems += 1
        except IndexError:
            break
    print()
    return printedItems
