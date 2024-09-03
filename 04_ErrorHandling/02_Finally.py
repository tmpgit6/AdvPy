class ValueTooSmall(Exception):
    pass 

class ValueTooLarge(Exception):
    pass

number = 7 
while True:
    try:        
            user_input = int(input(">"))

            if user_input < number:
                raise ValueTooSmall 
            elif user_input > number:
                raise ValueTooLarge 
            else:
                print("Good")
                break

    except ValueTooSmall:
        print("Nach Oben") 


    except ValueTooLarge:
        print("Nach Unten")  