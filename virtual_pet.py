# Skills Utilized: Classes and objects, conditionals, loops, user input/output, storage.

import random
import os
import pickle

class Pets:
    moods = ('Hungry', 'Happy', 'Tired')
    solutions = ('Feed', 'Play', 'Rest')

    def __init__(self, name:str='mimi', type:str='cat', color:str='orange', gender:str='f') -> None:
        self.name = name
        self.type = type
        self.color = color
        self.gender = gender
        self.current_mood = random.choice(self.moods)
        self.pronoun = ['she','her'] if self.gender == 'f' else ['he','him']

    def mood(self):
        return self.current_mood

    def action(self, mood):
        if mood in self.moods:
            index = self.moods.index(mood)
            return self.solutions[index]
        return 'You gotta find your own bud!'

    def change_mood(self, action):
        if action in self.solutions:
            action_index = self.solutions.index(action)
            if action_index == 0:
                self.current_mood = 'Happy'
            elif action_index == 1:
                self.current_mood = 'Tired'
            elif action_index == 2:
                self.current_mood = 'Hungry'
        return self.current_mood

    def __str__(self) -> str:

        return f"{self.name} is a {self.color} {self.type}. {self.pronoun[0]} is currently {self.current_mood.lower()}. Please call {self.pronoun[1].lower()} {self.name}."
    


def create_pet():
    name = input("Enter pet's name: ")
    type = input("Enter pet's type (e.g., cat, dog): ")
    color = input("Enter pet's color: ")
    gender = input("Enter pet's gender (m/f): ")
    return Pets(name, type, color, gender)

def save_pets(pets):
    with open('pets.pkl', 'wb') as file:
        pickle.dump(pets, file)

def load_pets():
    if os.path.exists('pets.pkl'):
        with open('pets.pkl', 'rb') as file:
            return pickle.load(file)
    return []

def main():
    pets = load_pets()
    print("Welcome to the Virtual Pet Game!")

    while True:
        print("\nMain Menu:")
        print("1. Create a new pet")
        print("2. Interact with a pet")
        print("3. List all pets")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            new_pet = create_pet()
            pets.append(new_pet)
            save_pets(pets)
            print(f"New pet created: {new_pet}")

        elif choice == '2':
            if not pets:
                print("No pets available. Create a pet first.")
                continue

            print("\nChoose a pet to interact with:")
            for idx, pet in enumerate(pets):
                print(f"{idx + 1}. {pet.name} the {pet.type}")

            pet_choice = int(input("Enter the pet number: ")) - 1

            if 0 <= pet_choice < len(pets):
                pet = pets[pet_choice]
                print(pet)

                while True:
                    current_mood = pet.mood()
                    print(f"\nThe pet's current mood is: {current_mood}")
                    action_suggested = pet.action(current_mood)
                    print(f"Suggested action: {action_suggested}")

                    action_taken = input("Choose an action (Feed, Play, Rest) or type 'X' to go to main menu: ").capitalize()
                    if action_taken == 'X':
                        break
                    if action_taken != action_suggested:
                        print(f"{pet.name} is Unhappy with you! {pet.pronoun[0]} wanted to {action_suggested}.")
                    elif action_taken in pet.solutions:
                        changed_mood = pet.change_mood(action_taken)
                        print(f"After performing '{action_taken}', the pet's mood is now: {changed_mood}")
                    else:
                        print("Invalid action. Please try again.")

            else:
                print("Invalid pet number. Please try again.")

        elif choice == '3':
            if not pets:
                print("No pets available.")
            else:
                print("List of all pets:")
                for pet in pets:
                    print(pet)

        elif choice == '4':
            print("Thanks for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()