# python-projects

# [Simple Python Calculator-Beginner level](https://github.com/shahi1208/python-projects/blob/main/calculator.py#link-1)

This Python script implements a basic calculator with support for addition, subtraction, multiplication, and division operations. It handles input validation, ensuring the user enters valid operators and numbers. If division by zero is attempted, the program prompts the user to enter a new denominator.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`), with error handling for division by zero

## How It Works

1. **Functions for Operations:**
   - `add(a, b)`: Adds two numbers `a` and `b`.
   - `sub(a, b)`: Subtracts `b` from `a`.
   - `mul(a, b)`: Multiplies `a` by `b`.
   - `div(a, b)`: Divides `a` by `b`, with error handling for division by zero.

2. **Input Validation:**
   - The `oper(op)` function ensures the entered operator is valid by recursively prompting the user until a valid operator (`+`, `-`, `*`, `/`) is entered.

3. **User Interaction:**
   - The calculator starts with a welcome message and prompts the user to press 'Y' to start or 'X' to terminate.
   - After each calculation, it displays the result and prompts the user to continue (`Y`) or terminate (`X`).

4. **Error Handling:**
   - If the user attempts division with zero as the denominator, it prints an error message and prompts for a new value.

5. **Termination:**
   - The program terminates when the user inputs 'X' to exit the calculator.

## Example Usage

```plaintext
Welcome to my calculator. Press Y to start.

Press Y to continue. X to terminate.
X OR Y? Y

enter first value: 10

Available operators- ['+', '-', '*', '/']
enter an operator: +

enter second value: 5

15
Press Y to continue. X to terminate.
X OR Y? Y

enter first value: 12

Available operators- ['+', '-', '*', '/']
enter an operator: /
enter second value: 0

ZeroDivisionError: Denominator cannot be zero
Enter a new value for Denominator: 2

6.0
Press Y to continue. X to terminate.
X OR Y? X

calculator is closed.
```

# Virtual pet game

This Python script implements a virtual pet game where users can create pets, interact with them, and manage multiple pets through a menu-driven interface. Pets have moods that change based on user interactions (feeding, playing, resting). The script utilizes object-oriented programming principles with a Pets class defining pet attributes and behaviors.

## Features
Create new pets with custom attributes (name, type, color, gender).
Interact with pets by choosing actions based on their current mood.
Save and load pets using pickle for persistence between sessions.
## How It Works
### Pets Class:

- Defines attributes (name, type, color, gender) and methods (mood(), action(), change_mood()) for managing pet state and behavior.
### Functions:

- **create_pet()**: Prompts the user to input pet details and returns a new Pets object.                                                          
- **save_pets(pets)** and **load_pets()**: Save and load pet data using pickle for persistence.
### Main Menu:

Displays options to create pets, interact with pets, list all pets, or quit the game.
Handles user input to perform corresponding actions (create new pets, interact with existing pets, list pets, quit).
### Interaction Loop:

- Allows users to choose actions for selected pets, with feedback on pet moods and suggested actions based on mood.
- Updates pet mood based on user-selected actions (Feed, Play, Rest).
### Persistence and Storage:

- Pets data is saved to pets.pkl file for future sessions, ensuring data continuity.
## Example Usage
```plaintext
Welcome to the Virtual Pet Game!

Main Menu:
1. Create a new pet
2. Interact with a pet
3. List all pets
4. Quit
Choose an option: 1

Enter pet's name: Mimi
Enter pet's type (e.g., cat, dog): Cat
Enter pet's color: Orange
Enter pet's gender (m/f): f
New pet created: Mimi is a orange cat. She is currently happy. Please call her mimi.

Main Menu:
1. Create a new pet
2. Interact with a pet
3. List all pets
4. Quit
Choose an option: 2

Choose a pet to interact with:
1. Mimi the cat
Enter the pet number: 1

Mimi is a orange cat. She is currently happy. Please call her mimi.

The pet's current mood is: Happy
Suggested action: Feed
Choose an action (Feed, Play, Rest) or type 'X' to go to main menu: Feed
After performing 'Feed', the pet's mood is now: Tired

Main Menu:
1. Create a new pet
2. Interact with a pet
3. List all pets
4. Quit
Choose an option: 3

List of all pets:
- Mimi is a orange cat. She is currently tired. Please call her mimi.

Main Menu:
1. Create a new pet
2. Interact with a pet
3. List all pets
4. Quit
Choose an option: 4

Thanks for playing! Goodbye!

```

# [Terminal Level Cookbook](https://github.com/shahi1208/python-projects/blob/main/recipe.py)

This script allows users to manage recipes in a simple cookbook application. It provides functionality to add new recipes and find existing recipes based on available ingredients. The recipes are stored in a JSON file.

## Features

- **Recipe Management:** Add and retrieve recipes from a JSON file.
- **Ingredient Matching:** Find recipes based on available ingredients.
- **User Interaction:** Simple command-line interface for user input.

## Code Overview

### Importing Required Modules

```python
import json
```

### Display Recipes Function

```python
def display_recipes(best_recipe):
    if len(best_recipe) > 1:
        print('We found multiple recipes for you!\n')
        cnt = 1
        for recipe in best_recipe:
            print(f"Recipe {cnt}: {recipe['name']}\n")
            print("Ingredients:".upper(), recipe['Ingredients'])
            print("\nInstructions:\n".upper())
            print(recipe['Instruction'].capitalize())
            print()
            print(' - ' * 30)
            cnt += 1
    elif best_recipe:
        print("\nBest Recipe:".upper(), best_recipe[0]['name'].capitalize())
        print("\nIngredients:".upper(), best_recipe[0]['Ingredients'])
        print("\nInstructions:\n".upper())
        print(best_recipe[0]['Instruction'].capitalize())
    else:
        print('\nNo matching recipe found')
```

### Adding a Recipe

```python
def add_recipe(recipe):
    with open('recipes.json', 'w') as f:
        json.dump(recipe, f, indent=4)
```

### Pulling Recipes

```python
def pull_recipes(filename="recipes.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
```

### Finding Recipes

```python
def find_recipes(all_recipes, Ingredients):
    best_recipe = []
    max_matched = 0

    for recipe in all_recipes:
        existing_ingredients = set(recipe['Ingredients'])
        match_cnt = len(existing_ingredients.intersection(Ingredients))

        if match_cnt >= max_matched and match_cnt != 0:
            max_matched = match_cnt
            best_recipe.append(recipe)
    return best_recipe
```

### User Entry

```python
def user_entry():
    new_recipe_name = input("What's the recipe name?")
    new_recipe_ingredients = input('Give ingredients list (Use comma to separate):').split(',')
    new_recipe_ingredients = [i.strip() for i in new_recipe_ingredients]
    new_recipe_intructions = input('Give a description on how to cook this recipe:')
    new_recipe = {
        "name": new_recipe_name,
        "Ingredients": new_recipe_ingredients,
        "Instruction": new_recipe_intructions
    }
    return new_recipe
```

### Main Function

```python
def main():
    print('Welcome to the cookbook.')
    print('Click N to add a new recipe. Click O to find an old recipe.')
    print('Press X to exit')
    x = input('N or O?').strip().lower()
    while x in ('n', 'o'):
        if x == 'n':
            old_recipes = pull_recipes()
            new_recipe = user_entry()
            old_recipes.append(new_recipe)
            add_recipe(old_recipes)
            x = input('What do you want to do now? (N or O)').strip().lower()
        elif x == 'o':
            print('\nMention the ingredients you have.')
            ingredients_in_fridge = input('Give ingredients list (Use comma to separate):').strip().split(',')
            ingredients_in_fridge = [i.strip() for i in ingredients_in_fridge]
            existing_recipes = pull_recipes()
            if existing_recipes and ingredients_in_fridge:
                best_recipe = find_recipes(existing_recipes, ingredients_in_fridge)
                display_recipes(best_recipe)
            else:
                print('\nNo recipes or ingredients found')
            x = input('What do you want to do now? (N or O)').strip().lower()

if __name__ == "__main__":
    main()
```

## Usage

1. **Run the script:** `python recipe.py`
2. **Add a new recipe:** Press `N` and follow the prompts.
3. **Find an existing recipe:** Press `O` and enter the ingredients you have.
4. **Exit the script:** Press `X`.

## Example Usage

### Adding a New Recipe

```
Welcome to the cookbook.
Click N to add a new recipe. Click O to find an old recipe.
Press X to exit
N or O? n

What's the recipe name? Spaghetti Bolognese
Give ingredients list (Use comma to separate): spaghetti, ground beef, tomato sauce, onion, garlic, olive oil, salt, pepper
Give a description on how to cook this recipe: Cook the spaghetti. In another pan, cook the ground beef with onion and garlic. Add tomato sauce and simmer. Mix with spaghetti and serve.

What do you want to do now? (N or O) o
```

### Finding a Recipe

```
Mention the ingredients you have.
Give ingredients list (Use comma to separate): spaghetti, tomato sauce, garlic

We found multiple recipes for you!

Recipe 1: Spaghetti Bolognese

INGREDIENTS: ['spaghetti', 'ground beef', 'tomato sauce', 'onion', 'garlic', 'olive oil', 'salt', 'pepper']

INSTRUCTIONS:
Cook the spaghetti. In another pan, cook the ground beef with onion and garlic. Add tomato sauce and simmer. Mix with spaghetti and serve.

 - - - - - - - - - - - - - - - - - - - - - - - - - - 
```

