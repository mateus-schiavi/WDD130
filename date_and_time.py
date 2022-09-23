import math
from datetime import datetime
respective_dateandtime_ = datetime.now()

width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume_p1 = math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + (2540 * diameter)) / 10000000000
# volume_p2_liters = volume_p1 / 10000000000

print(f'The respective volume is {volume_p1:.2f} liters')

with open('volumes.txt') as volumestxt:
    volumestxt.write(f'Width: {width}. Respective Ratio: {aspect_ratio}. Respective Diameter: {diameter}. \n')
    volumestxt.write(f'The respective volume is {volume_p1:.2f} liters\n')
    volumestxt.write(f"{respective_dateandtime_}\n")
    print('\n')