"""
8. Write a Python program to check the nature of roots of a quadratic equation (real & distinct, real & equal, or imaginary).
"""

a=float(input("Enter a value: "))
b=float(input("Enter b value: "))
c=float(input("Enter c value: "))

d=b**2-4*a*c

if d>0:
   print("Roots are real and distinct.")
elif d==0:
   print("Roots are real and equal.")
else:
   print("Roots are imaginary.")      