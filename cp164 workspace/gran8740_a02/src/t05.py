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
from Food_utilities import food_search
from Food import Food
# Constants

bun = Food("bun", 2, False, 1)
spring_roll = Food("spring roll", 3, True, 2)
cheese = Food("cheese", 2, True, 4)

food_list = [bun, spring_roll, cheese]

foods = food_search(food_list, 2, 4, True)

for food in foods:
    print(food)
