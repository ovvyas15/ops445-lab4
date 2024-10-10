#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    return s[:5]  # Returns the first five characters

def last_seven(s):
    return s[-7:]  # Returns the last seven characters

def middle_number(num):
    num_str = str(num)
    return num_str[1:3]  # Returns the second and third characters in the number

def first_three_last_three(s1, s2):
    return s1[:3] + s2[-3:]  # Combines first three of s1 and last three of s2

if __name__ == '__main__':
    print(first_five(str1))  # Output: Hello
    print(first_five(str2))  # Output: Senec
    print(last_seven(str1))  # Output: World!!
    print(last_seven(str2))  # Output: College
    print(middle_number(num1))  # Output: 50
    print(middle_number(num2))  # Output: .5
    print(first_three_last_three(str1, str2))  # Output: Helege
    print(first_three_last_three(str2, str1))  # Output: Send!!
