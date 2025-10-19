"""
2. Write a Python script to get the second last digit of a given number.
(For example: if user enters 7539 → output should be 3)
"""

num=int(input("Enter number here: "))

number=(num//10)%10

print(number)