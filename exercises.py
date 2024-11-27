# example 1

def manage_students():

    students = ['Ali', 'Abdulla', 'Ahmed', 'Diana']
    
    first_student = students[1]
    
    last_student = students[-1]
    
    return first_student, last_student

first_student, last_student = manage_students()
print('Exercise 1:', 'First_student:', first_student, 'Last_student:', last_student)

# example 2

def combine_foods():
    
    foods = ('Pizza', 'Burger', 'Pasta', 'Salad')
    
    meal = ''
    
    for food in foods:
        meal += food + ' '
    
    return meal

print('Exercise 2:', combine_foods())

# example 3

def slice_foods():

    foods = ('Pizza', 'Burger', 'Pasta', 'Salad')

    last_two_foods = foods[-2:]

    return last_two_foods

print('Exercise 3:', slice_foods())

# example 4

def hometown_info():

    home_town = {
        'city': 'Manama',
        'state': 'Capital Governorate',
        'population': 1000000000000
    }
    
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"

    return home_town_message

print('Exercise 4:', hometown_info())

# example 5

def list_home_town_items():

    home_town = {
        'city': 'Manama',
        'state': 'Capital Governorate',
        'population': 1000000000000
    }
    
    home_town_items = []
    
    for key, value in home_town.items():

        home_town_items.append(f"{key} = {value}")

    return home_town_items

print('Exercise 5:', list_home_town_items())
