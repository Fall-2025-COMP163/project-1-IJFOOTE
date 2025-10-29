"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Isaiah Foote]
Date: [Date]

AI Usage: [Document any AI assistance used]
"""
import os
gold = 0

def create_character(name, character_class):
    classes = ['warrior','cleric','mage','rogue']
    if character_class not in classes:
        print('Invalid character class: ' + character_class)
    else:
        print('Character class is ' + character_class)
        character = {
            "name": name,
            "class": character_class,
            "level": level,
            "strength": strength,
            "magic": magic,
            "health": health,
            "gold": gold
        }
    return character
strenght = 0
magic = 0
health = 0


def calculate_stats(character_class, level):
    if character_class == 'warrior':
        strength = 10
        magic = 2
        health = 10
    elif character_class == 'cleric':
        strength = 5
        magic = 8
        health = 8
    elif character_class == 'mage':
        strength = 3
        magic = 10
        health = 6
    elif character_class == 'rogue':
        strength = 6
        magic = 7
        health = 3
    else:
        print('Invalid character class: ' + character_class)

    if level == 1:
        strength += 0
        magic += 0
        health += 0
    elif level == 2:
        strength += 3
        magic += 1
        health += 1
    elif level == 1:
        strength += 2
        magic += 2
        health += 2
    else:
        print("level too high")
    return strength, magic, health


def save_character(character, filename):
    required_values = {'name', 'class', 'level', 'strength', 'magic', 'health', 'gold'}
    if not isinstance(character, dict):
        print(f"ERROR: Character data must be a dictionary, got {type(character).__name__}.")
        return False

    for key in required_keys:
        if key not in character:
            print(f"ERROR: Character data is missing the required key: '{key}'.")
            return False

    dir_path = os.path.dirname(filename)
    if dir_path != "" and not os.path.exists(dir_path):
        print(f"ERROR: Directory does not exist: {dir_path}")
        return False

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")

    return True

def load_character(filename):
    if not os.path.isfile(filename):
        print(f"ERROR: File does not exist: {filename}")
    return None

def display_character(character):
    pass


def level_up(character):

    pass


    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
