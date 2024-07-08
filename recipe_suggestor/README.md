## Introduction

Recipe Suggestor is a web application built with Flask that allows users to add, search, and edit recipes. It suggests recipes based on the ingredients the user has and allows them to manage their recipe collection with ease.

## Features

- Add new recipes
- Search for recipes based on available ingredients
- Edit existing recipes

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/recipe-suggestor.git
    cd recipe-suggestor
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install flask
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Project Structure

recipe-suggestor/                                                                                                                                                                                                                                 
│                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
|── static/                                                                                                                                                                                                                                                            
│ └── styles.css                                                                                                                                                                                                                                                             
│                                                                                                                                                                                                                                                                                       
├── templates/                                                                                                                                                                                                                                                                                   
│ ├── add_recipe.html                                                                                                                                                                                                                                                                                      
│ ├── edit_recipe.html                                                                                                                                                                                                                                                                                             
│ └── index.html                                                                                                                                                                                                                                                                                                          
│                                                                                                                                                                                                                                                                                                                              
├── app.py                                                                                                                                                                                                                                                                                                                             
└── recipes.json                                                                                                                                                                                                                                                                                                                                 
