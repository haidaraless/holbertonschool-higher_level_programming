#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    keys = sorted(a_dictionary.items(), key=lambda i: i[1], reverse=True)
    return keys[0][0]
