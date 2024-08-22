# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment1C.py

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))/100
bmi = weight / height**2
print("Your bmi is "+ str(round(bmi, 1)))
if bmi < 18.5:
    print("You are classified as underweight")
elif 18.5 <= bmi < 25:
    print("You are classified as normal weight")
elif 25 <= bmi <30:
    print("You are classified as overweight")
elif bmi >= 30:
    print("You are classified as obese")