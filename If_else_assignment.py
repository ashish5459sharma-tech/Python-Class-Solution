
# Question 1: 
"""Write a program to calculate the electricity bill
using only if statement? (accept number of unit from user)
according to the following criteria:

Unit Price
First 100 units no charge
Next 100 units Rs 5 per unit
After 200 units Rs 10 per unit
(For example, if input unit is 350 than total bill amount is Rs2000). Lets explain...
For first 100 no charges
Now you have 250 unit remaining
100-200 you need to pay – 100*5 = 500
Now 200-100 you need to pay 150*10 = 1500
Total = 500+1500 = 2000"""
# Solution:
unit = int(input("Enter number of units: "))

if unit <= 100:
    bill = 0
elif unit <= 200:
    bill = (unit - 100) * 5
else:
    bill = (100 * 5) + (unit - 200) * 10

print("Total bill in Rs", bill)

# Output:
# Enter number of units: 204
# Total bill in Rs 540

# Question 2:
"""Write a program to accept percentage from the user and display
the grade according to the following criteria:

Marks Grade
> 90 A
> 80 and <= 90 B
>= 60 and <= 80 C
below 60 D"""
# Solution:
marks = int(input("Enter percentage: "))

if marks > 90:
    print("Grade: A")
elif marks > 80:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# output:
# Enter percentage: 66
# Grade: C

# Question 3:
"""Accept the age of 4 people and display the youngest one?"""
# Solution:
a = int(input("Age1: "))
b = int(input("Age2: "))
c = int(input("Age3: "))
d = int(input("Age4: "))

y = a
if b < y: y = b
if c < y: y = c
if d < y: y = d
print("Youngest =", y)
# Output:
# Age1: 11
# Age2: 4
# Age3: 2
# Age4: 1
# Youngest = 1

# Question 4:
"""A company decided to give bonus to employee
according to following criteria:
Time period of Service Bonus
More than 10 years 10%
>=6 and <=10 8%
Less than 6 years 5%
Ask user for their salary and years of service and print the
net bonus amount?"""
# Solution:
salary = int(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 10:
    bonus = salary * 0.10
elif years >= 6:
    bonus = salary * 0.08
else:
    bonus = salary * 0.05

print("Bonus amount in Rs", bonus)

# Output :
# Enter salary: 10000
# Enter years of service: 11
# Bonus amount in Rs 1000.0

# Question 5:
"""Accept three numbers from the user and
display the second largest number?"""
# Solution:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a > c and a < b):
    second = a
elif (b > a and b < c) or (b > c and b < a):
    second = b
else:
    second = c

print("Second largest number is:", second)

# Output:
# Enter first number: 2
# Enter second number: 5
# Enter third number: 1
# Second largest number is: 2

# Question 6:
"""Accept the marked price from the user and calculate
the Net amount as (Marked Price – Discount) to pay
according to following criteria:

Marked Price Discount
>10000 20%
>7000 and <=10000 15%
<=7000 10%"""
# Solution :
p = int(input("Price: "))
if p > 10000:
    d = p*0.20
elif p > 7000:
    d = p*0.15
else:
    d = p*0.10
print("Net =", p-d)

# Output:
# Price: 100
# Net = 90.0

# Question 7:
"""Accept the marks of English, Math and Science,
Social Studies Subject and display the stream allotted
according to following:

All Subjects more than 80 marks — Science Stream

English >80 and Math, Science above 50 — Commerce Stream

English > 80 and social studies > 80 — Humanities"""
# Solution:
e = int(input("Eng: "))
m = int(input("Math: "))
s = int(input("Sci: "))
ss = int(input("SST: "))

if e>80 and m>80 and s>80 and ss>80:
    print("Science")
elif e>80 and m>50 and s>50:
    print("Commerce")
elif e>80 and ss>80:
    print("Humanities")
else:
    print("No Stream")

# Output:
# Eng: 81
# Math: 55
# Sci: 60
# SST: 90
# Commerce

# Question 8:
"""Write a program to display "Hello" if a number entered
by user is a multiple of five, otherwise print "Bye"?"""
# Solution:
n = int(input("Number: "))
if n%5==0:
    print("Hello")
else:
    print("Bye")

# Output:
# Number: 25
# Hello

# Question 9:
"""Write a program to check whether the last digit of a number
(entered by user) is divisible by 3 or not?"""
# Solution:
n = int(input("Number: "))
if n%3==0:
    print("Divisible")
else:
    print("Not Divisible")

# Output:
# Number: 21
# Divisible

#  Question 10:
"""Write a program to check whether a number entered
is three-digit number or not?"""
# Solution:
n = int(input("Number: "))
if n>=100 and n<=999:
    print("3-digit")
else:
    print("Not 3-digit")

# Output:
# Number: 1
# Not 3-digit
