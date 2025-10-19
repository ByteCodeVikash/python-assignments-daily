#6. Write a Python script that takes a four-digit number and displays its second digit from the left.

num=int(input("Enter number here: "))

number=(num//100)%10

print(number)

