#!/usr/bin/env python3
import math

number = float(input("Enter the number: "))

if number < 0:
    result = "Error: number<0."
else:
    result = math.sqrt(number)
with open("output.txt", "w") as file:
    file.write(str(result))
