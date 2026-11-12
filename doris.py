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

# BOOLEAN FUNCTION 

email = ""
phone = "0900873990"
username = "" 
# allows registration
#if any field is filled
print(any([email, phone, username]))

email = "doris@gmail"
phone = "0900873990"
username = "gift" 
# allows registration
#only if all field is filled
print(all([email, phone, username]))

email = "doris@gmail"
phone = "0900873990"
username = "" 
# allows registration
#only if all field is filled
print(all([email, phone, username]))

print(isinstance(123, int))
print("doris".endswith("s"))

# COMPARISON OPERATORS

print(10 == 10)
print("a" > "f")
print("a" == "A")

age = 20
print(18 <= age <= 30)

print(2 - 1 != 2)

#LOGICAL OPERATORS

print(3 > 1 and 5 > 1)
print(3 > 1 or 1 > 5 )
print(3 > 5 or 1 > 5 )
print(not (3 > 1 or  1 > 5 ))

# Allow access only if the user is logged in
# or they are a guest
# but they must not be banned

is_logged_in = True
is_guest = False
is_banned = False

print(is_logged_in or is_guest and not is_banned)

is_logged_in = True
is_guest = False
is_banned = True

print(is_logged_in or is_guest and not is_banned)


is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)

# MEMBERSHIP OPERATORS
name = ["doris", "divine", "xcel"]
print("doris" in name)
print("xcel" not in name)
print("gift" in name)
print("gift" not in name)

def about_me():
    print("working as a data engineer")
    print("with a fintech company")
    print("as a jnr data engineer")
    print("and i am married")

print("Doris is my name")
about_me()

#building full name
def full_name(first_name,last_name,country):
    first =first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "from", country)

full_name("DoRIS", "DIvine", "Nigeria")

def gift_me():
     print("i want a new laptop")
     print("and a note pad along side")
    
gift_me()

def greet_customer():
     print("Welcome to my shop")

greet_customer()


def calculate_total(price, quantity):
     print(price * quantity)

calculate_total( 3000, 2)

# *args AND **kwargs

def total_num(*args):
    print(sum(args))

total_num(50,30,50,100)

def new_name(*args):
    print(args)
    print(type(args))

    new_name("doris", "faith", "gift", "love")

def create_user(**kwargs):
    print(kwargs)

create_user(first_name="Doris",
            last_name="gift",
            age=27,
            country="Nigeria")

# RETURNS

def clean_name(name):
    lo_cleaned= name.strip().lower()
    up_cleaned= name.strip().upper()
    return lo_cleaned, up_cleaned

cln_name = clean_name(" Doris  ")
print(cln_name)



def clean_name(name):
    lo_cleaned= name.strip().lower()
    up_cleaned= name.strip().upper()
    return lo_cleaned, up_cleaned

cln_name, dit_name = clean_name(" Doris  ")
print(cln_name)
print(dit_name )

 # Assessment
def total_sales(sales1, sales2):
    daily_total= sales1 + sales2
    return daily_total

the_total=total_sales(5000, 7500)
print(the_total)


def calculate_profit(revenue, expenses):
    profit= revenue - expenses
    return profit

p_total=calculate_profit(25000, 8000)
print(p_total)

# CHATGBT Assessment

def greet():
    print("Hello, welcome to python")
greet()

def name():
    print("Doris")
name()

def add_number(a,b):
    print( a + b)
add_number( 30,50)


def even_or_odd(number):
    if number %2==0:
        print("even number")
    else:
        print("odd number")

even_or_odd(10)
even_or_odd(5)       


def greet_user(name):
    print("Hello", name +  ", welcome")

greet_user("Doris")


def calculate_age(birth_year):
    current_year=(2026)
    age=current_year - birth_year
    print("your age is:", age)

calculate_age(1999)


#Create a function called full_name(first_name, last_name) that returns the person's full name.

def full_name(first_name, last_name):
    return first_name + " " + last_name

result=full_name("Doris", "gift")
print(result)

# Create a function called discount(price, percentage) that calculates and returns the discounted price.

def discount(price, percentage):
    discount_amount= price * percentage / 100
    final_price= price - discount_amount
    return final_price
result=discount(30000, 10)
print("discounted price:", result)

#Create a function called largest_number(numbers) that accepts
#  a list of numbers and returns the largest number.

def largest_number(numbers):
    largest= max(numbers)
    return largest
result=largest_number([10, 25, 5, 40, 15])
print("The largest number is:", result)


# CONTROL FLOW

# check if any file name appear more than once
file_list = [
    "report.csv",
    "data.xlsx",
    "summary.docx",
    "report.csv",
    "data.csv"
]
for file in file_list:
    if file_list.count(file)>1:
        print("duplicate found")
        break
else:
    print("All files are unique")




















