#Mateus Schiavi
#CSE 111
#01 Prove Mileston

import math

print("Welcome to Tire Volume Calculator")
print("|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|")

def main():
    width = int(input("Enter the width of the tire in mm: "))
    respective_ratio = int(input("Enter the aspect ratio of the tire: "))
    respective_diameter = int(input("Enter the diameter of the wheel in inches: "))

    volume = round(((math.pi * width ** 2 * respective_ratio * (width * aspect_ratio + 2540 * respective_diameter)) / 10000000), 1)

    print(f"The respective volume is {volume} milliliters.")
    repeat()

def repeat():
    answer = input("Would you like to compute another volume (Y/N)? ")
    if answer.upper() == "Y":
        main()
    if answer.upper() == "N":
        print("The program will now end")
        exit()
    else:
        print("Error: Invalid Argument")
        repeat()

main()