"""
10. Write a Python program to find the smallest among three numbers. Print the number only once even if some are equal.
"""

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))

if num1<num2 and num1<num3:
   print(num1,"is a smallest.")
elif num2<num1 and num2<num3:
   print(num2,"is a smallest.")
else:
   print(num3,"is a smallest.")      