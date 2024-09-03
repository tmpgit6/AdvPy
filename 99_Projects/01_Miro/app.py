import json 
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


def greeting():
    print("Willkommen bei Miro Restaurant")
    print("=" * 30)

def load_menu():
    with open("./menu.json", mode ="r", encoding="UTF-8") as file:
        menu = json.load(file) 

    return menu


def show_menu(menu):
    valid_ids = []

    for category in menu:
        print(category)
        print("=" * 10)

        for dish in menu[category]:        
            print(f"{dish["id"]}. {dish["title"]}\t{dish["price"]}€")
            valid_ids.append(dish["id"])

        return valid_ids

def get_users_wishes(valid_ids):
    user_wishes = []
    print("\nWas möchten Sie bestellen:")

    while True:
        user_input = int(input(">")) 

        # exit point
        if user_input == 0:
            break 

        # check valid dish id
        if user_input not in valid_ids:    
            print("Das bieten wir nicht an")
            continue

        user_wishes.append(user_input)

    user_wishes.sort()

    return user_wishes

def print_receipt(user_wishes, menu):
    print("\nQuittung")
    print("=" * 10)
      
    total = 0 

    for user_wish_id in user_wishes:
        for category in menu:
            for dish in menu[category]:
                if user_wish_id == dish["id"]:
                    print(f"{dish["id"]}. {dish["title"]}\t{dish["price"]}€")
                    total += dish["price"]
                
    total = round(total, 2)

    print(f"\nSumme: {total}€")

    print("\n\nVielen Dank für Ihren Besuch !")

def main():
    
    # Greeting
    greeting()

    # Load Menu
    menu = load_menu()

    # Show Menu 
    valid_ids = show_menu(menu)

    # User wishes
    user_wishes = get_users_wishes(valid_ids)

    # Receipt 
    print_receipt(user_wishes, menu)
   

if __name__ == "__main__":
    main()