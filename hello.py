print("Hello, world!")
print("this is Miss D")
print("and i am here to talk about my python class.")
print("Well, the class has been going pretty good,")
print("and my tutor has been doing a great job")
print("I hope i dont disappoint him")
print("i love doing this")

# my second assignment

print("hello, world!", end=" ")
print("this is my second assignment", end=" ")
print("lets see if it works")
print("okayyy..... it did work")
print("I am a calm and genuine person who values honesty,", end=" " )
print("kindness, and meaningful connections. I enjoy good conversations.", end=" ")
print("love to laugh, and appreciate the simple things that make life enjoyable.")

# text and numbers

print(3 * 3)
print(1000 + 400)
print("i am", 26, "years old")

# this is a comment
"""
this is my second comment work
trying the multiple line work
lets see if it works 
"""
print("this is Miss D")

# variables
x = 5
y = "Miss D"

print(x)
print(y)


x = 500
y = "people dying weekly"

print(x) ; print(y)

print(type(x)) ; print(type(y))

x = 200
X = "i love working on this python"
print(type(x)) ; print(type(X))
print(x) ; print(X)

# variables name

myVar = "Doris"
print(myVar)

x=y=z = ("micheal")
print(x)
print(y)
print(z)

x,y,z = "Doris", "Divine", "Trobul"
print(x)
print(y)
print(z)

import random

print(random.randrange(1, 10))

d = """I am a calm and genuine person who values honesty, kindness, and meaningful connections.
 I enjoy good conversations.love to laugh, and 
 appreciate the simple things that make life enjoyable."""

print(d)


a = "Hello world"
print(a[2])

for x in "Doris":
   print(x)


# strings length 
a = "Hello world"
print(len(a))


txt = "appreciate the simple things that make life enjoyable"
print("things" in txt)

txt = "appreciate the simple things that make life enjoyable"
print("free" in txt)

txt = "appreciate the simple things that make life enjoyable"
if "things" in txt:
  print("yes 'things' is present")


# slicing strings
a = "Doris Divine"
print(a[2:5])

a = "Doris Divine"
print(a[:5])

a = "Doris Divine"
print(a[2:])

a = "Doris Divine"
print(a[-5:-2])

# Modify Strings 

a = "Doris Divine"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("D", "B"))
print(a.split(","))

# String Concatenation

a = "Doris"
b = "Gift"
c = a+b
print(c)

a = "Doris"
b = "Gift"
c = a + " " + b
print(c)

a = "Doris"
b = "Gift"
c = a+b
print(c.upper())

# formate strings

age = 26
txt = f"My name is Gift, i am {age}"
print(txt)

price = 50000
txt = f"the price of the goods is {price}"
print(txt)


txt = "We are the so-called \"Vikings\" from the north."
print(txt)

print(10>9)
print(10==9)
print(1>10)

a = 500
b =50

print(b>a)
print(b<a)


if b>a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# class assignment

print("this is a class assignment")

a = "Doris"
b = "is an aspiring data engineer"
c = "so look out for her at the top"

print(a)
print(b)
print(c)

print(a,b,c)

# second assignment

c = "so look out for her at the top"

print(c[4:8])

print(len(c))

# upper case

print(b.upper())


# f strings

age = 30
txt = f"i am {age} years old"

print(txt)

# arithemetric 

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# walrus operator 

number=[1,2,3,4,5]
if(count:=len(number))>2:
 
  print(f"list has {count} elements")
 
# ternary operators
num = 30
x="month" if num > 25 else "year"

print(x)

num= 30
x="may" if num==25 else "june" if num==30 else "feb" if num==50 else "month"
print(x)

# comparison operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


x=50
print(55>x<60)

# logical operator
x=5
# and
print(x > 0 and x < 10)
# or
print(x < 5 or x > 10)
# not
print(not(x > 3 and x < 10))

# identity operators

x = ["phone","laptop"]
y = ["phone","laptop"]
z = x

print(x is z)
print(x is y)
print(x==y)

print(x is not y)

#python membership operators

name=["doris","gift","divine"]
print("divine" in name)
print("love" not in name)

# pmo in strings

text="hello doris"
print("d" in text)
print("doris" in text)
print("a" not in text)

# bitwise operators

print(6&3)
print(6|3)
print(6^3)
print(~3)
print(6<<3)
print(6>>3)

#operator precedence

print((6+3)-(6+3))
print(100+5*3)
print(5+4-7+3)  

# python lists

thislist=["apple","banana","mango"]
print(thislist)

thislist=["apple","banana","mango","apple","mango"]
print(thislist)
print(len(thislist))
print("doris", 26,True,"xcel")

mylist = ["doris", "divine", "xcel"]
print(type(mylist))

thislist = list(("doris", "divine", "xcel"))
print(thislist)

# access list

thislist =["doris", "divine", "xcel"]
print(thislist[2])

thislist =["doris", "divine", "xcel"]
print(thislist[-1])

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
print(thislist[2:5])

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
print(thislist[-4:-1])

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# change item value

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist[1]=["gift"]
print(thislist)

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist[1:3]=["gift","love"]
print(thislist)

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist[1:2]=["gift","love"]
print(thislist)

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist[1:3]=["gift"]
print(thislist)

#insert item
thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist.insert(2, "gift")
print(thislist)

#Add list 
thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist.append("gift")
print(thislist)

thislist =["doris", "divine", "xcel"]
fruit=["apple","banana","mango"]
thislist.extend(fruit)
print(thislist)

thislist =["doris", "divine", "xcel"]
thistuple=("apple","banana","mango")
thislist.extend(thistuple)
print(thislist)

#remove list

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist.remove("divine")
print(thislist)

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist.remove("apple")
print(thislist)

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist.pop(1)
print(thislist)

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist.pop()
print(thislist)

#delete

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
del thislist[0]
print(thislist)

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
del thislist


thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist.clear()
print(thislist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#sort
thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist.sort()
print(thislist)

thislist =[200,40,60,3,100,153]
thislist.sort()
print(thislist)

thislist =["doris", "divine", "xcel","apple","banana","mango","apple","mango"]
thislist.sort(reverse = True)
print(thislist)

thislist =[200,40,60,3,100,153]
thislist.sort(reverse = True)
print(thislist)

#copy list

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#join
list1 = ["love", "gift" , "xcel"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)



list1 = ["divine", "xcel" , "apple"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


#PYTHON TUPLE

mytuple="apple","banana","mango"
print(mytuple)

mytuple=("apple","banana","mango","apple","mango")
print(mytuple)
print(len(mytuple))

thistuple = ("apple",)
print(type(thistuple))

thistuple = ()
print(type(thistuple))

mytuple = ("doris", "divine", "xcel")
print(type(mytuple))

tuple1=("doris", 26,True,"xcel")


thistuple = tuple(("doris", "divine", "xcel"))
print(thistuple)

# access list

thistuple =("doris", "divine", "xcel")
print(thistuple[2])

thistuple =("doris", "divine", "xcel")
print(thistuple[-1])

thistuple =("doris", "divine", "xcel","apple","banana","mango","apple","mango")
print(thistuple[2:5])

thistuple =("doris", "divine", "xcel","apple","banana","mango","apple","mango")
print(thistuple[-4:-1])

thistuple =("doris", "divine", "xcel","apple","banana","mango","apple","mango")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits list")

#UPDATE TUPLE
x = ("doris", "divine", "xcel")
y = list(x)
y[1] = "love"
x = tuple(y)

print(x)


thistuple = ("doris", "divine", "xcel")
y = list(thistuple)
y.append("gift")
thistuple = tuple(y)


thistuple = ("doris", "divine", "xcel")
y = ("love",)
thistuple += y

print(thistuple)



thistuple = ("doris", "divine", "xcel")
y = list(thistuple)
y.remove("doris")
thistuple = tuple(y)


thistuple = ("doris", "divine", "xcel")
del thistuple


#unpack tuple

gender = ("doris", "divine", "xcel")

(female, girl, male) = gender

print(female)
print(girl)
print(male)

gender = ("doris", "divine", "xcel","gift","love")

(female, girl, *male) = gender

print(female)
print(girl)
print(male)


gender = ("doris", "tiana","mercy", "divine", "xcel")

(female, *girl, male) = gender

print(female)
print(girl)
print(male)

#JOIN TUPLE

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


thistuple = ("doris","divine", "xcel","divine", "xcel")
print(thistuple.count("divine"))


# PYTHON SET

thisset={"doris", "divine", "xcel"}
print("xcel" in thisset)


thisset={"doris", "divine", "xcel"}
for x in thisset:
    print(x)

# ADD SET ITEM

thisset ={"doris", "divine", "xcel"}
thisset.add("gift")

print(thisset)


thisset={"doris", "divine", "xcel"}
fruits ={"apple", "banana", "cherry"}

thisset.update(fruits)

print(thisset)

# DATA TYPE

thisset={"doris", "divine", "xcel"}
fruits = ("apple", "banana", "cherry")

thisset.update(fruits)

print(type(thisset))

# REMOVE ITEM FROM SET

thisset={"doris", "divine", "xcel"}
thisset.remove("doris")
print(thisset)

thisset={"doris", "divine", "xcel"}
thisset.discard("doris")
print(thisset)

thisset={"doris", "divine", "xcel"}
thisset.clear()
print(thisset)


#JOIN SET (UNION)

set1={"doris", "divine", "xcel"}
set2={"apple", "banana", "cherry"}

set3=set1.union(set2)
print(set3)

set1={"doris", "divine", "xcel"}
set2={"apple", "banana", "cherry"}

set3=set1 | set2
print(set3)

set1={"doris", "divine", "xcel"}
set2={"apple", "banana", "cherry"}
set3={"love", "tiana","mercy"}
myset=set1.union(set2,set3)

print(myset)

set1={"doris", "divine", "xcel"}
set2={"apple", "banana", "cherry"}
set3={"love", "tiana","mercy"}
myset=set1 | set2 |set3

print(myset)

# INTERSECTION

set1={"doris", "divine", "xcel"}
set2={"xcel", "banana", "cherry"}

set3=set1.intersection(set2)
print(set3)

set1={"doris", "divine", "xcel"}
set2={"xcel", "banana", "cherry"}

set3=set1 & set2
print(set3)

#difference

set1={"doris", "divine", "xcel"}
set2={"xcel", "banana", "cherry"}

set3=set1.difference(set2)
print(set3)

set1={"doris", "divine", "xcel"}
set2={"xcel", "banana", "cherry"}

set3=set1 - set2
print(set3)

# symmetric difference

set1={"doris", "divine", "xcel"}
set2={"xcel", "banana", "cherry"}

set3=set1.symmetric_difference(set2)
print(set3)


set1={"doris", "divine", "xcel"}
set2={"xcel", "banana", "cherry"}

set3=set1 ^ set2
print(set3)



# DICTIONARIES

thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

print(thisdict)

# ACCESS ITEM

thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

x=thisdict["model"]
print(x)


thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

x=thisdict.keys()
print(x)


phone={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

x=phone.keys()
print(x)

phone["color"]= "white"

print(x)

# CHANGE ITEM

thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

thisdict.update({"year": 2026})
print(thisdict)


#ADDING ITEM

thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

thisdict.update({"color":"white"})
print(thisdict)


# REMOVE ITEM

thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

thisdict.pop("year")
print(thisdict)


thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}
thisdict.popitem()
print(thisdict)



#  LOOPING DICTIONARIES

thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

for x in thisdict:
    print(x)


thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

for x in thisdict:
    print(thisdict[x])

thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}
for x,y in thisdict.items():
    print(x,y)

# COPY

thisdict={
   "brand": "Apple",
  "model": "iPhone 15",
  "year": 2023
}

mydict=thisdict.copy()
print(mydict)

mydict=dict(thisdict)
print(mydict)


#NESTED DICTIONARIES

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

# LOOPING

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    for y in obj:
      print(y + ':', obj[y])



# basic if/elif condition 

x = 30
y = 20
if x != y:
    print("x is not equal to y")


x = 30
y = 20
if x < y:
    print("x is less than y")
elif y > x:
    print("y is greater than x")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")


# short if / if..else

x = 20
if x == 20: print("True")


x = 20
y = 30
print("x") if x > y else print("y")



a = 200
b = 33
if b > a :
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")









