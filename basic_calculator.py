# -*- coding: utf-8 -*-
"""Basic_Calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KhRoYoCiveiuWTczqjNGYlfsUZErx9bj

# **Basic Calculator**

define the functions needed: add,sub,mul,div

print option to the user 

ask for values

call the functions

while loop to continue the program until the user wants to exit
"""

def add(a,b):
  ans = a + b
  print(str(a)+"+"+str(b)+"="+str(ans))
def sub(a,b):
  ans = a - b
  print(str(a)+"-"+str(b)+"="+str(ans))
def mul(a,b):
  ans = a * b
  print(str(a)+"*"+str(b)+"="+str(ans))
def div(a,b):
  ans = a / b
  print(str(a)+"/"+str(b)+"="+str(ans))
while True:
  print("A, Addition")
  print("B, Subtraction")
  print("C, Multiplication")
  print("D, Division")
  print("E, Exit")

  choice = input("Enter your choice:")

  if choice == "a" or choice =="A":
    print("Addition")
    a = int(input("Enter the Value of 1st Number:"))
    b = int(input("Enter the Value of 2nd Number:"))
    add(a,b)
  elif choice == "b" or choice =="B":
    print("Subtraction")
    a = int(input("Enter the Value of 1st Number:"))
    b = int(input("Enter the Value of 2nd Number:"))
    sub(a,b)
  elif choice == "c" or choice =="C":
    print("Multiplication")
    a = int(input("Enter the Value of 1st Number:"))
    b = int(input("Enter the Value of 2nd Number:"))
    mul(a,b)
  elif choice == "d" or choice =="D":
    print("Division")
    a = int(input("Enter the Value of 1st Number:"))
    b = int(input("Enter the Value of 2nd Number:"))
    div(a,b)
  if choice == "e" or choice =="E":
    print("Program Ended")
    break
    quit()