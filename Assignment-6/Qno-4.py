"""
4. Write a Python script to print the smaller number between two numbers. Print the number only once even if both are equal.
"""

num1=int(input("Enter number here: "))
num2=int(input("Enter number here: "))

if num1>num2:
   print(num2,"is smaller.")
elif num2>num1:
   print(num1,"is smaller")
else:
   print(num1,"both a equal")      