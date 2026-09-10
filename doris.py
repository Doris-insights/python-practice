print("hello world!") #introduction

# Escape characters or Escape special character

print("Your learning path:\n\t-python basics\n\t-Data Engineering\n\t-AI")

print("""Your learning path:
      \t-python basics
      \t-Data Engineering
      \t-AI""")

#name = input("Enter your name:")
#print("you are",name)

#name = input("Enter your name:")
#country = "Nigeria"
#print(name,"comes from",country) 



j =" "
print(type(j))

#  Types
name = "Doris"
print(type(name))

age = 24
print(type(age))
print("your Age is:" + str(age)) 

#  Math

password = "dori12345"
print(len(password))

if len(password) < 8:
  print("your password is too short!")

# Transformations

price = "234,23"
print(price.replace(",", "."))

phone = "647-566-5364"
print(phone.replace("-", "/"))

phone = "+49 (176) 123-4567"
print(phone.replace("+", "").replace("()", "").replace("-", "").replace("(", "").replace(" ", "").replace(")", ""))

#  join strings

first_name = "Doris"
last_name = "Divine"
last_name = first_name + " " + last_name
print(last_name)

# f-strings

name = "Doris"
age = 24
is_student = False
print(f"My name is {name}, i am {age} years old, and student status is {is_student}.")

print(f"2 + 3 = {2 +3}")


# split()
name = "Doris, 24, Nigeria, tall, beautiful"
print(name.split(","))


# string repetition
print("=" * 20)

# Extraction

# Whitespace cleanup

test = " doris".strip()
print(test)

test = " doris  ".strip()
print(test)

# Numeric data type
x = 5
y = 5.7
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

x = 34.3
print(int(x))

x = "15"
print(type(x))
x = int(x)
print(type(x))
print(x * 3)

x = 34
print(float(x))

# Maths operators
print(4 + 8)
print(4 - 8)
print(4 / 8)
print(4 // 8)
print(9 % 2)
print(2 ** 3)

# Measure Distance

print(2 - 10)
print(abs(2 - 10))

# Rounding Numbers
import math
price = 35.6474357

print(round(price))
print(round(price,2))
print(math.floor(price))
print(math.ceil(price))
print(math.floor(price))

# Ramdom 
import random
print(random.random())
print(random.randint(1,9))

#Validation
x = 7.0
print(x.is_integer())

y = 7.1
print(y.is_integer())

# python challenge
# generate a random integer between 1 and 100, and check if the result is an even number

number = random.randint(1,100)
print("random number:", number)

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")









































