#Mateus Schiavi
#CSE 111
#01 Prove Mileston

import math

print("Welcome to Tire Volume Calculator")
print(":::::::::::::::::::::::::::::::::")

def main():
    wwidth = int(input("Enter the respective width of the tire in mm: "))
    main_ratio = int(input("Enter the respective ratio of the tire: "))
    main_diameter = int(input("Enter the respective diameter of the wheel in inches: "))
    
    volume = round((math.pi * width ** 2 * main_ratio * (width * main_ratio + 2540 * main_diameter) / 10000000), 1)
    
    print(f"The respective volume is {volume} millimeters.")
    repeat()
    
def repeat():
    answer = input("Would you like to compute another volume (Y/N)?")
    if answer.upper() == "Y":
        main()
    if answer.upper() == "N":
        print("The program will end now")
        exit()
    else:
        print("Error: Invalid Input")
        repeat()
main()
    