# create a variable and Print them in one sentence
name = "Doris"
age = 24
country = "Nigeria"

print(f"my name is {name}, i am {age}, and i live in {country}.")

# Calculate and print the total price.
price = 1500
quantity = 3
print(price * quantity)

# What data type is each of these?

name = "Doris"
age = 24
price = 1500.50
is_student = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_student))

#The first character
#The last character
#The length of the string
#The word "Python" only
#The word "Programming" only

word = "Python Programming"

print(word[ :1])
print(word[17: ])
print(len(word))
print(word[ :7])
print(word[7: ])

# Use .replace() to change - to nothing.
phone = "080-123-4567"
print(phone.replace("-",""))


x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)

# Check whether this number is greater than 50
number = 75
print( number > 50)

# Create a program that checks whether someone can buy a phone.

money = 2000
phone_price = 2000
if phone_price >= money:
    print("You can buy the phone.")
else:
    print("You cannot buy the phone.")

age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Generate a random integer between 1 and 100.
# Then check whether the number is even or odd.
import random
number = random.randint(1,100)
print("random number:", number)

if number % 2==0:
    print("The number is even")
else:
    print("The number is odd")

"""
Print the entire list
Print "apple"
Add "grape" to the list
Remove "banana"
Print the length of the list 
"""
fruits = ["apple", "banana", "orange", "mango"]

print(fruits)
print(fruits[0])
fruits.insert(2,"grape")
print(fruits)
fruits.remove("banana")
print(fruits)
print(len(fruits))

# loops
numbers = 1, 2, 3, 4, 5, 6
for x in numbers:
 print(x)

fruits = ["apple", "banana", "orange", "mango"]
for x in fruits:
 print(x)

i = 1
while i < 6:
 print(i)
 i += 1

"""
Create a program that asks the user for:

Their name
The price of a product
The quantity they want to buy

Calculate the total.

Then:

If the total is 5000 or more, give them a 10% discount.
Otherwise, there is no discount.
"""

#name = input("Enter your name:")
#price = float(input("Enter the price of the product: "))
#quantity = int(input("Enter the quantity: "))

total = price * quantity

if total >= 5000:
    discount = total * 0.10
else:
    discount = 0

final_price = total - discount

print()
print(f"Customer: {name}")
print(f"Total before discount: {total}")
print(f"Discount: {discount}")
print(f"Final price: {final_price}")

# Second Assessment

name = input("Enter your name:")
age = int(input("your age: "))
city = input("your city: ")

print(f"Hello, {name}!")
print(f"You are {age} years old and you live in {city}.")


a = int(input("your first number: "))
b = int(input("your second number: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)


number = int(input("give me a number: "))
if number % 2 == 0:
   print(f"{number} is even")
else:
   print(f"{number} is odd")


age= int(input("your age: "))

if age is age <= 12:
   print("You are a child.")
elif age <= 19:
   print("You are a teenager")
elif age <= 59:
   print("You are an adult")
else :
   print("You are a senior")
     






















