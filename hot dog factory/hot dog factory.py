import os
import time
import sys
import random
import json

class Glizzy:
    def __init__(self, name, a1, a2, meat, bun):
        self.name = name
        self.a1 = a1
        self.a2 = a2
        self.meat = meat
        self.bun = bun

    def __str__(self):
        return f"Your hot dog is known as {self.name}, it contains {self.meat}, with {self.a2} and {self.a1} on top all nicely arranged in a {self.bun} hot dog bun"

def create_glizzy():
    name = input("Every great hot dog needs a name, what do you wish to call yours?: \n")
    bun = input("I guess that'll do. Now, what bun would you like your glizzy to occupy: \n")
    meat = input("Nice. Now, the most important part, the substance in which the glizzy is formed from: \n")
    a1 = input("Great, but whats a glizzy without it's dressing, onions maybe?: \n")
    a2 = input("Can't forget the sauce: \n")

    bun = bun.replace("bun", "")

    print("Brilliant, generating your glizzy.. :)")
    percent = 0
    time.sleep(1)
    for i in range(100):
        percent += 1
        time.sleep(0.05)
        print(f"{percent}%")

    print("Hot dog generated!!!!!")
    time.sleep(1)
    return Glizzy(name, a1, a2, meat, bun)

def save_glizzies(glizzies):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "glizzies.json")
    with open(file_path, "w") as file:
        serialized_glizzies = [glizzy.__dict__ for glizzy in glizzies]
        json.dump(serialized_glizzies, file)

def load_glizzies():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "glizzies.json")
    try:
        with open(file_path, "r") as file:
            serialized_glizzies = json.load(file)
            return [Glizzy(**glizzy_data) for glizzy_data in serialized_glizzies]
    except FileNotFoundError:
        return []

def main():
    print("Welcome to the hot dog factory, where you can make your own glizzy")
    glizzies = load_glizzies()

    while True:
        glizzy = create_glizzy()
        print(glizzy)
        glizzies.append(glizzy)
        save_glizzies(glizzies)

        another = input("Build another hot dog? (Y/N): ").lower()
        if another != "y":
            if not glizzies:
                print("No glizzies created. Goodbye!")
            else:
                print("Thanks for the glizzies")
                for i, glizzy in enumerate(glizzies, start=1):
                    print(f"Hot dog #{i}: {glizzy}")
                select_glizzy = random.randint(1, len(glizzies))
                print(f"Hot Dog #{select_glizzy} sounds delicious. I think that one is my favorite!")
            sys.exit()

if __name__ == "__main__":
    main()
