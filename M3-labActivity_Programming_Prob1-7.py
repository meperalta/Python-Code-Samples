#Eden Peralta
#03.04.2022
#Module 3: Lab Activity - Programming

#What the program does
#Testing IDLE
#Rerun IDLE to check if working properly
#IDLE is good to go!Let's start

#Problem 1 
print("Hello World")

#Problem 2
name = input("Please enter your name")
print("Hello Eden, How are you today")

#Problem 3
#if statement

if(name == "eden"):
    print("Good!")
else:
    print("Good" + name)
print("ok, good")
    
           
#if statement is the creation of a reference from a variable to a value.
#When we see the value that is referring to, the evaluation of variable example name by itself results in the same response.
#if statement is conditional if conditions is true the result will be true, if not it will prompt to error


#Problem 4
import math
radius = float(input("Enter the radius of the circle : "))
area = math.pi * radius * radius
print("Area of the Circle is :{0}".format(area))

#Problem 5
#Receive Input
miles_driven = float(input("\nEnter number of miles driven: "))
gallons_of_gas_used = float(input("Enter gallons of gas used: "))

#Process (Calculate stuff)
mpg = miles_driven / gallons_of_gas_used

#Output Info
print("Miles per gallon =", mpg, end="\n\n")

#Miles per Gallon = 7.0


#Problem 6
#How to Convert Fahreheit to Celsius
#Equation: Celsius = (Fahrenheit - 32) * 5/9

fer = float(input("Enter Farenheit Temperature:"))
cel = (fer - 32) * 5/9
print("Celsius Temperature: {0}".format(cel))

#Problem 7
def get_day_name(day_number):
    if day_number == 0:
        return "Sunday"
    elif day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
print(get_day_name(3))

start_day_number = 3
number_of_nights = 10

print("start_day_numer = 3 + number_of_nights = 10")



    
