#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) != True or roman_string == None:
        return 0
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_int = 0
    for i in range(len(roman_string)):
        if i > 0 and r[roman_string[i]] > r[roman_string[i - 1]]:
            r_int += r[roman_string[i]] - 2 * r[roman_string[i - 1]]
        else:
            r_int += r[roman_string[i]]
    return r_int
