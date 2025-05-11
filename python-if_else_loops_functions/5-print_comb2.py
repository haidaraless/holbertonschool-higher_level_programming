#!/usr/bin/python3
numbers = [f"0{i}" if i < 10 else f"{i}" for i in range(100)]
print(*numbers, sep=", ")
