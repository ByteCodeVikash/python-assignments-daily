"""
10. Write a Python program to show the current date and time using the datetime module. Display output in the format — 16-10-2025 and 10:00 AM.

"""

from datetime import datetime

current=datetime.now()

date=current.strftime("%d-%m-%y")
time=current.strftime("%I:%M %p")


print("Current date:-",date)
print("Current time:-",time)