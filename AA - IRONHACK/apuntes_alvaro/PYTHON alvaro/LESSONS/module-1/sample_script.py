"""
sample_cript.py
---------
This is a sample Python script.
Python is an interpreted high-level general-purpose programming language. 
Its design philosophy emphasizes code readability with its use of significant indentation. 
Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
"""
import pandas as pd
import random

def random_num_generator(amount_of_numbers, min_num, max_num):
    return [random.randint(min_num, max_num) for num in range(amount_of_numbers)]

a = int(input('Enter a minimum value for set of numbers (0-9):'))
b = int(input('Enter a maximum value for set of numbers (0-9):'))
c = int(input('Enter the amount of number you want to generate:'))

result = random_num_generator(c, a, b)

print(f'This is your list of random numbers: {result}')
print(f'==>Total amount of number generated: {len(result)}')