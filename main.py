# W. Looby
# random average generator 
# March 24 2025
# This program creates 100 random numbers and then calculates the average

import random

numbers = []

for _ in range(100):
    numbers.append(random.randint(0, 100))

print (numbers)

total_sum = sum(numbers)
count = len(numbers)

average = total_sum / count

print("the average is" ,average,)