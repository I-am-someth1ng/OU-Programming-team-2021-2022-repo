"""
    One-liner solution for - https://open.kattis.com/problems/autori
"""
__author__ = "Taras Basiuk"

"""
Solution works as follows:
    1. input().strip() - reads a string of input and strips it of possible white-space characters
    2. .split('-') splits the above string by the '-' character into a list of sub-strings
    3. [x[0] for x in ... - takes the above sub-strings and keeps only the first character from each of them
    4. ''.join( ... - joins the above array of characters into a string
    5. print - outputs the result
"""
print(''.join([x[0] for x in input().strip().split('-')]))
