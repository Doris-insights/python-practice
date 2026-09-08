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
























































