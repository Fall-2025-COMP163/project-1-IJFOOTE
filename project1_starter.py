"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Isaiah Foote
Date: [Date]

AI Usage: Used ChatGPT for debugging and code structure clarification.
"""
import os

gold = 0

def calculate_stats(character_class, level):
    if character_class == 'Warrior':
        strength = 10
        magic = 2
        health = 10
    elif character_class == 'Cleric':
        strength = 5
        magic = 8
        health = 8
    elif character_class == 'Mage':
        strength = 3
        magic = 10
        health = 6
    elif character_class == 'Rogue':
        strength = 6
        magic = 7
        health = 3
    else:
        print('Invalid character class: ' + character_class)
        return 0, 0, 0

    if level == 1:
        pass
    elif level == 2:
        strength += 3
        magic += 1
        health += 1
    elif level == 3:
        strength += 2
        magic += 2
        health += 2
    else:
        print("Level too high")

    return strength, magic, health


def create_character(name, character_class, level=1):
    classes = ['warrior','Warrior', 'cleric','Cleric','Mage','mage', 'Rogue','rogue']
    if character_class not in classes:
        print('Invalid character class: ' + character_class)
        return None

    strength, magic, health = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    print('Character class is ' + character_class)
    return character


def save_character(character, filename):
    required_keys = {'name', 'class', 'level', 'strength', 'magic', 'health', 'gold'}

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

    print(f"Character saved to {filename}")
    return True


def load_character(filename):
    if not os.path.isfile(filename):
        print(f"ERROR: File does not exist: {filename}")
        return None

    character_data = {}

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split(':', 1)
        if len(parts) == 2:
            key = parts[0].strip().lower()
            value = parts[1].strip()

            key_mappings = {
                "character name": "name",
                "class": "class",
                "level": "level",
                "strength": "strength",
                "magic": "magic",
                "health": "health",
                "gold": "gold"
            }

            if key in key_mappings:
                mapped_key = key_mappings[key]
                if mapped_key in ['level', 'strength', 'magic', 'health', 'gold']:
                    if value.isdigit():
                        character_data[mapped_key] = int(value)
                else:
                    character_data[mapped_key] = value

    if not character_data:
        print("ERROR: Failed to load character data.")
        return None

    print(f"Character loaded from {filename}")
    return character_data


def display_character(character):
    print("\n=== CHARACTER SHEET ===")
    print(f"Character Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}\n")


def level_up(character):
    print(f"\n{character['name']} leveled up!")
    character['level'] += 1
    character['strength'], character['magic'], character['health'] = calculate_stats(character['class'], character['level'])
    return character


# === MAIN PROGRAM ===
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")

    name = input("Enter character name: ")
    char_class = input("Enter character class (warrior/cleric/mage/rogue): ")

    character = create_character(name, char_class)
    if character:
        display_character(character)

        save_character(character, "my_character.txt")
        print("\n--- Reloading character from file ---")
        loaded_char = load_character("my_character.txt")

        if loaded_char:
            display_character(loaded_char)
