"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    name = input('Name: ')
    print('Origin')
    print(Food.origins())
    origin = int(input(':'))
    vegetarian = input('Vegetarian (Y/N):')
    if vegetarian.isupper() == 'Y':
        vegetarian = True
    elif vegetarian.isupper() == 'N':
        vegetarian = False
    calories = int(input('Calories:'))
    print('\n')
    food = Food(name, origin, bool(vegetarian), calories)

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    line = line.strip().split("|")

    food = Food(line[0], int(line[1]), eval(line[2]), int(line[3]))

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """

    foods = []
    line = file_variable.readline()

    while line != "":
        food = read_food(line)
        foods.append(food)
        line = file_variable.readline()

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for x in foods:
        line = f'{x.name}|{x.origin}|{x.is_vegetarian}|{x.calories}\n'
        file_variable.write(line)

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies = []
    for x in foods:
        if x.is_vegetarian == True:
            veggies.append(x)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    origins = []

    for x in foods:
        if x.origin == origin:
            origins.append(x)

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    sum = 0
    counter = 0

    for x in foods:
        sum += x.calories
        counter += 1

        avg = sum // counter

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    sum = 0
    counter = 0

    for x in foods:
        if x.origin == origin:
            sum += x.calories
            counter += 1

    avg = sum // counter

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    foods.sort()

    print("Food                                Origin       Vegetarian Calories")
    print("----------------------------------- ------------ ---------- --------")
    for item in foods:
        print(
            f"{item.name:<36s}{Food.ORIGIN[item.origin]:<13s}{str(item.is_vegetarian):>10}{item.calories:>9}")

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []

    for i in foods:
        if i.origin == origin:
            if max_cals >= i.calories or max_cals == 0:
                if is_veg == i.is_vegetarian:
                    result.append(i)

    return result
