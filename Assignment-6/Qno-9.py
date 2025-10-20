#9. Write a Python script to check whether a given year is a century year or not.

year=int(input("Enter year here: "))

if year%100==0:
   print(year,"is a century")
else:
   print(year,"is not century")   