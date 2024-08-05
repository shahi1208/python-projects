# Skills Utilized: Lists, dictionaries, user input/output, import modules, comprehension, file handling for storing recipes.

import json

def user_choice():
    return input('\nWhat you wanna do now? (N or O)').strip().lower()

def display_recipes(best_recipe):
    if len(best_recipe) > 1:
        print('We found multiple recipes for you!\n')
        cnt = 1
        for recipe in best_recipe:
            print(f"Recipe {cnt}: {recipe['name']}\n")
            print("Ingredients:".upper(),recipe['Ingredients'])
            print("\nInstructions:\n".upper())
            print(recipe['Instruction'].capitalize())
            print()
            print(' - ' * 30)
            cnt += 1
    elif best_recipe:
        print("\nBest Recipe:".upper(), best_recipe[0]['name'].capitalize())
        print("\nIngredients:".upper(),best_recipe[0]['Ingredients'])
        print("\nInstructions:\n".upper())
        print(best_recipe[0]['Instruction'].capitalize())
    else:
        print('\nNo matching recipe found')

def add_recipe(recipe):
    with open('recipes.json','w') as f:
        json.dump(recipe,f,indent=4)


def pull_recipes(filename="recipes.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def find_recipes(all_recipes,Ingredients):
    best_recipe = []
    max_matched = 0

    for recipe in all_recipes:
        existing_ingredients = set(recipe['Ingredients'])
        match_cnt = len(existing_ingredients.intersection(Ingredients))

        if match_cnt >= max_matched and match_cnt != 0:
            max_matched = match_cnt
            best_recipe.append(recipe)
    return best_recipe

def user_entry():
    new_recipe_name = input("What's the recipe name?")
    new_recipe_ingredients = input('Give ingredients list (Use comma to seperate):').split(',')
    new_recipe_ingredients = [i.strip() for i in new_recipe_ingredients]
    new_recipe_intructions = input('Give a description on how to cook this recipe:')
    new_recipe = {"name":f'{new_recipe_name}',
                "Ingredients":new_recipe_ingredients,
                "Instruction":new_recipe_intructions}
    return new_recipe

def main():
    print('Welcome to be cookbook.')
    print('Click N to add a new recipe. Click O to find old recipe.\nPress X to exit')
    x = user_choice()
    while (x == 'n' or x=='o'):
        if x == 'n':
            old_recipes = pull_recipes()
            new_recipe = user_entry()
            old_recipes.insert(len(old_recipes),new_recipe)
            add_recipe(old_recipes)
            
            x = user_choice()
        elif x == 'o':
            print('\nMention the ingredients you have.')
            ingredients_in_fridge = input('Give ingredients list (Use comma to seperate):').strip().split(',')
            ingredients_in_fridge = [i.strip() for i in ingredients_in_fridge]
            existing_recipes = pull_recipes()
            if existing_recipes and ingredients_in_fridge:
                best_recipe= find_recipes(existing_recipes,ingredients_in_fridge)
                display_recipes(best_recipe)
            else:
                print('\nNo recipes or ingredients found')

            x = user_choice()

if __name__ == "__main__":
    main()
