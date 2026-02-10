#libraries are collections of pre-written code that can be imported and used in your own programs. They provide a way to reuse code and save time by not having to write everything from scratch.
#In Python, you can create your own libraries by organizing your code into modules and packages. A module is a single file containing Python code, while a package is a collection of modules organized in a directory.
#To create a library, you can follow these steps:
#1. Create a directory for your library and add an __init__.py file to make it a package.
#2. Create modules (Python files) within the package to organize your code.
#3. Write your functions, classes, or variables in the modules.
#4. Import your library in other Python files to use the functionality you have created.
#Example:
#Directory structure:
#my_library/
#    __init__.py
#    math_utils.py
#    string_utils.py
#math_utils.py

import math
import statistics
import random
import os
import numpy as np
import openai

def add(a, b):
    return a + b

numbers = [1, 2, 2, 3, 4, 5, 4]
print("Mean: ", statistics.mean(numbers))
print("Median: ", statistics.median(numbers))
print("Mode: ", statistics.mode(numbers))
print("Random number between 1 and 10: ", random.randint(1, 10))
print("Current working directory: ", os.getcwd())