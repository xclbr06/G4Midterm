def tempbpMenu():
    conversionFunc = {
        '1': celsius_to_fahrenheit,
        '2': fahrenheit_to_celsius,
        '3': mmhg_to_pascal,
        '4': pascal_to_mmhg
    }
    
    while True:
        print("\n<=== Temperature and Blood Pressure Conversions ===>")
        print("1. Celsius -> Fahrenheit")
        print("2. Fahrenheit -> Celsius")
        print("3. Millimeters of Mercury -> Pascal")
        print("4. Pascal -> Millimeters of Mercury")
        print("5. Back to Main Menu")
        print("6. Exit Program")
        
        choice = input("\nEnter your choice: ")
        
        if choice in conversionFunc:
            conversionFunc[choice]()
        elif choice == '5':
            break
        elif choice == '6':
            print("\nExiting program. Goodbye and Have a Nice Day!")
            exit()
        else:
            print("Invalid input! Please enter a number between 1-6.\n")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Invalid input! Value cannot be a negative input.\n")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter numerical values.\n")

def celsius_to_fahrenheit():
    while True:
        celsius = get_positive_float("Enter Celsius: ")
        print(f"Formula: ({celsius} °C * 9/5) + 32")
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} °C = {fahrenheit:.2f} °F")
        
        if not repeatConv():
            break

def fahrenheit_to_celsius():
    while True:
        fahrenheit = get_positive_float("Enter Fahrenheit: ")
        print(f"Formula: ({fahrenheit} °F - 32) * 5/9")
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} °F = {celsius:.2f} °C")
        
        if not repeatConv():
            break

def mmhg_to_pascal():
    while True:
        mmhg = get_positive_float("Enter mmHg: ")
        print(f"Formula: {mmhg} mmHg * 133.322")
        pascal = mmhg * 133.322
        print(f"{mmhg} mmHg = {pascal:.2f} Pa")
        
        if not repeatConv():
            break

def pascal_to_mmhg():
    while True:
        pascal = get_positive_float("Enter Pascal: ")
        print(f"Formula: {pascal} Pa / 133.322")
        mmhg = pascal / 133.322
        print(f"{pascal} Pa = {mmhg:.2f} mmHg")
        
        if not repeatConv():
            break

def repeatConv():
    while True:
        choice = input(
            "\nInput 'y' if you want to convert again with the same conversion."
            "\nInput 'n' and you will be redirected back to the conversion list."
            "\nInput 'e' to exit the program. (y/n/e):"
        ).lower()
        
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        elif choice == 'e':
            print("\nExiting program. Goodbye and Have a Nice Day!")
            exit()
        else:
            print("Invalid input! Please enter 'y', 'n' or 'e'.\n")