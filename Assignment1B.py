# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment1B.py
p = float(input("Enter the loan amount: "))
r = float(input("Enter the annual interest rate (in%): "))/1200
n = int(input("Enter the loan term (in years): "))*12
var1 = (1+r)**n
var2 = p*r*var1
var3 = (1+r)**n
var4 = var3 - 1
payment = round(var2/var4, 2)
print("Your monthly payment is: " + str(payment))
