"""
11. Write a Python script to take the month number as input and display the month name (like 1 → January, 2 → February, etc.).
"""

month=int(input("Enter a month number: "))

match month:
   
   case 1:
        print("jan")
   case 2:
        print("Feb")
   case 3:
        print("March")
   case 4:
        print("april")
   case 5:
        print("May")
   case 6:
        print("June")
   case 7:
        print("july")                             
   case 8:
        print("Aug")
   case 9:
        print("Sep")

   case 10:
        print("oct")
   case 11:
        print("nov")
   case 12:
        print("Dec")

   case _ :
        print("Enter valid month number.")                