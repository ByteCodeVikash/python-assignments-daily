"""
12. Write a Python script to accept a complex number from the user and display which part (real or imaginary) is smaller.
"""

z=complex(input("Enter a complex number(e.g.,3+4j): "))

if z.real < z.imag:
   print("Real part is smaller.")
elif z.real > z.imag:
   print("Imaginary part is smaller.")
else:
   print("Both part are equal.")

         