"""
3. Write a Python script to swap values of three variables in cyclic order.
(For example: a→b, b→c, c→a)
"""

a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))

a,b,c=b,c,a

print("a value: ",a)
print("b value: ",b)
print("c value: ",c)