import os
import time
import sys
import random
import json

# Define a Burger class with attributes: name, a1, a2, meat, and bun
class Burger:
    def __init__(self, name, a1, a2, meat, bun):
        self.name = name
        self.a1 = a1
        self.a2 = a2
        self.meat = meat
        self.bun = bun

    def __str__(self):
        return f"Your burger is called {self.name}, it contains {self.meat}, {self.a1}, {self.a2}, all nicely arranged in a {self.bun} bun"

# Function to create a custom burger
def create_burger():
    name = input("First things first, please name your burger: \n")
    bun = input("Perfect, now we will need a bun to put all of your yummy ingredients in: \n")
    meat = input("Interesting choice. Next thing, the meat, pick yours today: \n")
    a1 = input("Oh, that sounds nice. Now put anything else you would like inside your burger, perhaps cheese?: \n")
    a2 = input("Go on, one more thing: \n")

    bun = bun.replace("bun", "")  # Remove the word "bun" from the input

    print("Brilliant, generating your burger..")
    percent = 0
    time.sleep(1)
    for i in range(100):
        percent += 1
        time.sleep(0.05)
        print(f"{percent}%")

    print("Burger generated!!!!!")
    time.sleep(1)
    return Burger(name, a1, a2, meat, bun)  # Create a Burger object with user inputs

# Function to save saved_burgers to a JSON file
def save_burgers(saved_burgers):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "burgers.json")  # Path to the JSON file
    with open(file_path, "w") as file:
        serialized_burgers = [burger.__dict__ for burger in saved_burgers]  # Serialize burger objects
        json.dump(serialized_burgers, file)  # Write serialized data to the file

# Function to load saved_burgers from the JSON file
def load_burgers():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "burgers.json")  # Path to the JSON file
    try:
        with open(file_path, "r") as file:
            serialized_burgers = json.load(file)  # Deserialize data from the file
            return [Burger(**burger_data) for burger_data in serialized_burgers]  # Create Burger objects
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

# Main function
def main():
    print("Welcome to the burger factory, where you can make your own burger")
    saved_burgers = load_burgers()  # Load existing saved_burgers from the file

    while True:
        burger = create_burger()  # Create a new burger
        print(burger)  # Print details of the created burger
        saved_burgers.append(burger)  # Add the burger to the list
        save_burgers(saved_burgers)  # Save the updated list of saved_burgers

        another = input("Build another burger? (Y/N): ").lower()
        if another == "n":
            print("Thanks for the burgers")
            for i, burger in enumerate(saved_burgers, start=1):
                print(f"Burger {i}: {burger}")  # Print saved saved_burgers
            select_burger = random.randint(1, len(saved_burgers))
            print(f"Burger {select_burger} sounds delicious. I think that one is my favorite!")
            sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  # Run the main function when the script is executed directly
