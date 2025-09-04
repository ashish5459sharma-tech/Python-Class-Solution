# Quesion 1: write a python program to print all the numbers from 1 to 10 using a for loop ?
for i in range(1, 11):
    print(i)

# Solution:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Question 2: Write a Python program to find the sum of all numbers from 1 to 100 using a for loop.
A = 0
for i in range(1, 101):
    A += i
print("Sum =", A)

# Solution :
# Sum = 5050

# Question 3: Write a Python program to print the multiplication table of a given number using a for loop.
A = int(input("Enter a number: "))
for i in range(1, 11):
    print(A,"*", i, "=", A * i)

# Solution :
# Enter a number: 8
# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# 8 * 6 = 48
# 8 * 7 = 56
# 8 * 8 = 64
# 8 * 9 = 72
# 8 * 10 = 80


# Question 4:Write a Python program to count the number of even and odd numbers from a series of numbers using a for loop. Hint: Find even and odd from this list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
numbers = [1,2,3,4,5,6,7,8,9,10]
even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even numbers:", even)
print("Odd numbers:", odd)

# Solution:
# Even numbers: 5
# Odd numbers: 5

# Question 5:Write a Python program to find the factorial of a number using a for loop.
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num+1):
    fact = fact * i

print("Factorial is:", fact)

# Solution:
# Enter a number: 4
# Factorial is: 24

# Question 6:Write a Python program to print the Fibonacci sequence up to a specified number using a for loop.
n = int(input("Enter how many terms: "))
a = 0
b = 1

for i in range(n):
    print(a)
    a,b=b,a+b

# Solution: 
# Enter how many terms: 5
# 0
# 1
# 1
# 2
# 3

# Question 7:Write a Python program to check if a given number is prime or not using a for loop.
n = int(input("Enter the no."))
limit = int(n**.5)+1
if n<0:
    print("negative no.")
else:

    for i in range (2,limit):
     if n%i==0:
            print("not a prime no.")
            break
    else:
     print("prime no.")
    
# Solution:
# Enter the no.97
# prime no.

# Question 8:Write a Python program to find the largest element in a list using a for loop.
numbers = [10, 25, 5, 87, 45]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number is:", largest)

# Solution:
# Largest number is: 87

# Question 9:Write a Python program to reverse a given string using a for loop.
text = "python"
rev = ""

for char in text:
    rev = char + rev

print("Reversed:", rev)

# Solution:
# Reversed: nohtyp

# Question 10:Write a Python program to find the common elements between two lists using a for loop. List1 = [1,2,3] List2 = [4,5,1] # common element is 1
list1 = [1, 2, 3]
list2 = [4, 5, 1]
common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common elements are:", common)

# Solution:
# Common elements are: [1]
