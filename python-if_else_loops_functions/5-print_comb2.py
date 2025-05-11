#!/usr/bin/python3
for i in range(100):
    print(f"0{i}" if i < 10 else f"{i}", end=", ")
print("")
