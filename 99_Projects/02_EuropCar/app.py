import config as cfg


def greeting():
    print("Willkommen be EuropCar")
    print("=" * 30)

def get_customer_info():
    
    first_name = input("Ihr Vorname:").strip()
    last_name = input("Ihr Nachname:").strip()

    if cfg.CORRECT_CASE:
        first_name = first_name.title()
        last_name = last_name.upper()

    return first_name, last_name

def get_order_info():
    car_id = int(input("Welche Auto?"))
    count_days= int(input("Wie viel Tage?"))

    return car_id, count_days

def show_cars():

    print("\nAutosliste")
    print("=" * 15)
    for car in cfg.CARS_LIST:
        print(f"{car['id']}. {car['mark']} - {car['bj']} - {car['price']}€")

def find_car(car_id):
    for car in cfg.CARS_LIST:
        if car["id"] == car_id:
            return car

def export_receipt(first_name, last_name, car_id, count_days):
    # Build the receipt Text
    car = find_car(car_id)
    total = count_days * car["price"]
    receipt_text = ""
    receipt_text = f"""
    Quittung für {first_name} {last_name}
    ===============
    {car['id']}. {car["mark"]} 
    Summe: {total}
    """

    # Print 
    if cfg.PRINT_IN_TERMINAL:
        print(receipt_text)

    # Save
    if cfg.SAVE_IN_FILE:
        with open(f"./{cfg.EXPORT_FOLDER}/receipts.txt", mode = "a", encoding= "UTF-8") as file:
            file.write(receipt_text)

def main():
    # 1. Greeting
    greeting()

    # 2. Get User Info
    first_name, last_name = get_customer_info()

    # 3. Show the car list
    show_cars()

    # 4. Get Order Info
    car_id, count_days = get_order_info()
    
    # Receipt
    export_receipt(first_name, last_name, car_id, count_days )


if __name__ == "__main__":
    main()