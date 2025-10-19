#8. Write a Python program to calculate compound interest. Take principal, rate, and time as inputs.

p=int(input("Enter principal: "))
r=int(input("Enter rate: "))
t=int(input("Enter time: "))

amt=p*(1+r/100)**t

ci=amt-p


print(ci)