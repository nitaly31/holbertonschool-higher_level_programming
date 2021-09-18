#!/usr/bin/python3
def roman_to_int(roman_string):
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_sum = 0
    if type(roman_string) != str or roman_string is None:
        return r_sum
    if len(roman_string) == 1:
        return r.get(roman_string[0])
    for i in range(len(roman_string) - 1):
        if r.get(roman_string[i]) < r.get(roman_string[i -1]):
            r_sum += r.get(roman_string[i]) * -1
        else:
            r_sum += r.get(roman_string[i])
        if i == len(roman_string) - 2:
            r_sum += r.get(roman_string[i + 1])
    return r_sum
