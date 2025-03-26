def weightMenu():
    conversionFunc = {
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
        
        if choice in conversionFunc:
            conversionFunc[choice]()
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
        kg = get_positive_float("\nEnter kilograms: ")
        print(f"\nFormula: {kg} kg * 2.20462")
        pounds = kg * 2.20462
        print(f"Result: {kg} kg = {pounds:.2f} pounds")
        
        if not repeatConv():
            break

def pounds_to_kg():
    while True:
        pounds = get_positive_float("\nEnter pounds: ")
        print(f"\nFormula: {pounds} pounds / 2.20462")
        kg = pounds / 2.20462
        print(f"Result: {pounds} pounds = {kg:.2f} kg")
        
        if not repeatConv():
            break

def grams_to_ounces():
    while True:
        grams = get_positive_float("\nEnter grams: ")
        print(f"\nFormula: {grams} grams / 28.3495")
        ounces = grams / 28.3495
        print(f"Result: {grams} grams = {ounces:.2f} ounces")
        
        if not repeatConv():
            break

def ounces_to_grams():
    while True:
        ounces = get_positive_float("\nEnter ounces: ")
        print(f"\nFormula: {ounces} ounces * 28.3495")
        grams = ounces * 28.3495
        print(f"Result: {ounces} ounces = {grams:.2f} grams")
        
        if not repeatConv():
            break

def kg_to_grams():
    while True:
        kg = get_positive_float("\nEnter kilograms: ")
        print(f"\nFormula: {kg} kg * 1000")
        grams = kg * 1000
        print(f"Result: {kg} kg = {grams:.2f} grams")
        
        if not repeatConv():
            break

def grams_to_kg():
    while True:
        grams = get_positive_float("\nEnter grams: ")
        print(f"\nFormula: {grams} grams / 1000")
        kg = grams / 1000
        print(f"Result: {grams} grams = {kg:.2f} kg")
        
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