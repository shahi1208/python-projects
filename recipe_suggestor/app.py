# Skills Utilized: Lists, dictionaries, user input/output, import modules, comprehension, file handling for storing recipes , flask and jinja2.

# load - read
# dump - write


from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)

def pull_recipes(filename="recipes.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_recipe(recipe):
    with open('recipes.json', 'w') as f:
        json.dump(recipe, f, indent=4)

def find_recipes(all_recipes, ingredients):
    best_recipe = []
    max_matched = 0

    for recipe in all_recipes:
        existing_ingredients = set(recipe['Ingredients'])
        match_cnt = len(existing_ingredients.intersection(ingredients))

        if match_cnt >= max_matched and match_cnt != 0:
            max_matched = match_cnt
            best_recipe.append(recipe)
    return best_recipe

def update_recipe(index, new_recipe):
    recipes = pull_recipes()
    if 0 <= index < len(recipes):
        recipes[index] = new_recipe
        add_recipe(recipes)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions']
        new_recipe = {
            "name": name,
            "Ingredients": [i.strip().capitalize() for i in ingredients],
            "Instruction": instructions
        }
        old_recipes = pull_recipes()
        old_recipes.append(new_recipe)
        add_recipe(old_recipes)
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ingredients = request.form['ingredients'].split(',')
        ingredients = [i.strip().capitalize() for i in ingredients]
        existing_recipes = pull_recipes()
        if existing_recipes and ingredients:
            best_recipe = find_recipes(existing_recipes, ingredients)
            if best_recipe:
                return render_template('index.html', recipes=best_recipe,enumerate=enumerate)
            else:
                return render_template('index.html', message='No matching recipes found.')
        else:
            return render_template('index.html', message='No recipes or ingredients found.')
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    recipes = pull_recipes()
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions']
        new_recipe = {
            "name": name,
            "Ingredients": [i.strip() for i in ingredients],
            "Instruction": instructions
        }
        update_recipe(index, new_recipe)
        return redirect(url_for('index'))
    recipe = recipes[index]
    return render_template('edit_recipe.html', recipe=recipe, index=index)

if __name__ == "__main__":
    app.run(debug=True)
