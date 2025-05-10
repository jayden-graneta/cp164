"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Jayden Graneta
ID: 169058740
Email: gran8740@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""
# Imports
from Food_utilities import average_calories
from Food import Food

bun = Food("bun", 2, False, 1)
spring_roll = Food("spring roll", 3, True, 2)
cheese = Food("cheese", 2, True, 3)

food_list = [bun, spring_roll, cheese]

print(average_calories(food_list))
