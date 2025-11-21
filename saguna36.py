
import random
import string
import sys

animal_dic = {}

print(
    '\nAnimal register program:'
    '\n1: Enter A or a to add new animal.'
    '\n2: Enter D or d to delete an animal.'
    '\n3: Enter U or u to update an animal.'
    '\n4: Enter L or l to check list of animals.'
    '\n5: Enter E or e to exit the program.'
)

def print_register():
    if not animal_dic:
        print("\nNo animals registered yet.")
        return
    x = PrettyTable(["ID", "Scientific Name", "Common Name"])
    for animal_id, data in animal_dic.items():
        x.add_row([animal_id, data["scientific_name"], data["common_name"]])
    print(x.get_string(title="Animal Register"))

def random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

def add_animal():
    scientific_name = input("\nPlease enter the scientific name: ").title()
    common_name = input("Please enter the common name: ").title()

    if not scientific_name or not common_name:
        print("You must write something!")
        return

    animal_id = random_id()
    animal_dic[animal_id] = {
        'scientific_name': scientific_name,
        'common_name': common_name
    }
    print(f"\nAnimal added successfully with ID: {animal_id}")

def delete_animal():
    animal_id = input("\nEnter the animal ID you want to delete: ").upper()
    if animal_id in animal_dic:
        choice = input("Delete (y/n)? ").lower()
        if choice in ("y", "yes"):
            del animal_dic[animal_id]
            print(f"{animal_id} record has been deleted!")
    else:
        print("ID not found. Check the list using 'L'.")

def update_animal():
    animal_id = input("\nEnter the animal ID you want to update: ").upper()
    if animal_id in animal_dic:
        choice = input(f"Update record {animal_id}? (y/n): ").lower()
        if choice in ("y", "yes"):
            scientific_name = input("Write a new scientific name: ").title()
            common_name = input("Write a new common name: ").title()
            if scientific_name:
                animal_dic[animal_id]['scientific_name'] = scientific_name
            if common_name:
                animal_dic[animal_id]['common_name'] = common_name
            print("Record updated!")
            print_register()
    else:
        print("ID not found. Check the list using 'L'.")

def exit_program():
    sys.exit("Goodbye!")

# Main program loop
while True:
    user_input = input("\nWhat do you want to do? (A, D, U, L, E): ").lower()
    if user_input == "a":
        add_animal()
    elif user_input == "d":
        delete_animal()
    elif user_input == "u":
        update_animal()
    elif user_input == "l":
        print_register()
    elif user_input == "e":
        exit_program()
    elif not user_input:
        print("Please enter something!")
    else:
        print("Invalid input. Try again.")
