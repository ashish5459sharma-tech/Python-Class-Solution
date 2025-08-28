# how do you concatenate two strings in python?
A = "hy"
B = "pyhton"
C = A+B
print(C)
# Output: hypython

# difference between the +operator and the join method() for concarenate strings ?
# + operator
a = "hy"
b = "python"
c = a + b
print(c)  
# Output: hypython

# join method()
A = ["aman","sahil"]
B = "".join(A)
print(B)
# Output: amansahil


# access individual characters in a string ?
text = "Python"
print(text[0])  
print(text[3]) 
# Output: p
# Output: h


  

# what method is used to find the length of a string in python?
string = "Python"
print(len(string))
# Output: 6


# how can you convert a string to uppercase in python ?
Text = "python"
print(Text.upper()) 
# Output: PYTHON


# how can you convert a string to lowercase in python ?
TEXT = "python"
print(TEXT.lower()) 
# Output: python


# what method is used to replace substring within a string ?
A = "I like Java"
B = A.replace("Java", "Python")
print(B) 
# Output: I like python


# how can you split a string into a list of substrings based on a delimiter ?
A = "Hello World Python"
result = A.split()
print(result) 
# Output:['Hello','World','Python']


# how do you check if a string starts with a particular substring ?
A = "Python Programming"
print(A.startswith("Python"))
# Output: True
      
# how do you check if a string ends with a particular substring ?   
A = "Python Programming"
print(A.endswith("Python"))
# Output: False


# how can you remove leading and trailling whitespace from a string?
text = "   Python   "
A = text.strip()
print(A)
# Output: Python


# What method is used to find the index of the first occurance of a substring with in a string ?
text = "Hello Python World"
index = text.find("Python")
print(index) 
# # Output: 6
  

# how can you count the number of occurances of a substring with in a string ?
text = "banana"
print(text.count("a")) 
# Output: 3


# how can you check if the string contains only alphabatic characters ?
text1 = "Python"
print(text1.isalpha()) 
# Output: True


# how can you check if the string contains only numeric characters ?
text1 = "1234"
print(text1.isnumeric()) 
# Output: True


# how can you check if a string is a palindrome ?

# how can you reverse a string in python ?
A = "Python"
reverse = A[::-1]
print(reverse)  
# Output: nohtyP


# how do you format a string with placeholders for variable value ?
name = "Ashish"
age = 22
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Ashish and i am 22 years old.


# how do you access a substring of a string using slicing ?
text = "PythonProgramming"
print(text[0:6])    
print(text[6:])    
print(text[:6])
# Output: Python
# Output: Programming
# Output: Python


# how can you remove soecific characters from a string in python ?
text = "hello"
A = text.replace("l", "")
print(A)
# Output: heo

















