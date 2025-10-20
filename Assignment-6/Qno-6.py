#6. Write a Python program to check whether a number entered by the user is a four-digit number or not.

num=int(input("Enter a number: "))

if num>=1000 and num<=9999:
   print("It is four digit number.")
else:
   print("It is not four digit number.")   