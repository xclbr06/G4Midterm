def weightMenu():
    conversion_functions = {
        '1': kg_to_pounds,
        '2': pounds_to_kg,
        '3': grams_to_ounces,
        '4': ounces_to_grams,
        '5': kg_to_grams,
        '6': grams_to_kg
    }
    
    while True:
        print("\n<=== Weight Measurement Conversions ===>")
        print("1. Kilograms -> Pounds")
        print("2. Pounds -> Kilograms")
        print("3. Grams -> Ounces")
        print("4. Ounces -> Grams")
        print("5. Kilograms -> Grams")
        print("6. Grams -> Kilograms")
        print("7. Back to Main Menu")
        print("8. Exit Program")
        
        choice = input("\nEnter your choice: ")
        
        if choice in conversion_functions:
            conversion_functions[choice]()
        elif choice == '7':
            break
        elif choice == '8':
            print("\nExiting program. Goodbye and Have a Nice Day!")
            exit()
        else:
            print("Invalid input! Please enter a number between 1-8.")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Invalid input! Weight cannot be a negative input.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter numerical values.")

def kg_to_pounds():
    while True:
        kg = get_positive_float("Enter kilograms: ")
        print(f"Formula: {kg} kg * 2.20462")
        pounds = kg * 2.20462
        print(f"{kg} kg = {pounds:.2f} lbs")
        
        if not repeatConv():
            break

def pounds_to_kg():
    while True:
        pounds = get_positive_float("Enter pounds: ")
        print(f"Formula: {pounds} lbs / 2.20462")
        kg = pounds / 2.20462
        print(f"{pounds} lbs = {kg:.2f} kg")
        
        if not repeatConv():
            break

def grams_to_ounces():
    while True:
        grams = get_positive_float("Enter grams: ")
        print(f"Formula: {grams} g * 0.035274")
        ounces = grams * 0.035274
        print(f"{grams} g = {ounces:.2f} oz")
        
        if not repeatConv():
            break

def ounces_to_grams():
    while True:
        ounces = get_positive_float("Enter ounces: ")
        print(f"Formula: {ounces} oz / 0.035274")
        grams = ounces / 0.035274
        print(f"{ounces} oz = {grams:.2f} g")
        
        if not repeatConv():
            break

def kg_to_grams():
    while True:
        kg = get_positive_float("Enter kilograms: ")
        print(f"Formula: {kg} kg * 1000")
        grams = kg * 1000
        print(f"{kg} kg = {grams} g")
        
        if not repeatConv():
            break

def grams_to_kg():
    while True:
        grams = get_positive_float("Enter grams: ")
        print(f"Formula: {grams} g / 1000")
        kg = grams / 1000
        print(f"{grams} g = {kg:.2f} kg")
        
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
            print("Invalid input! Please enter 'y', 'n' or 'e'.")