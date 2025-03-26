def liquidMenu():
    conversionFunc = {
        '1': liters_to_gallons,
        '2': gallons_to_liters,
        '3': ounces_to_ml,
        '4': ml_to_ounces
    }
    
    while True:
        print("\n<=== Liquid Measurement Conversions ===>")
        print("1. Liters -> Gallons")
        print("2. Gallons -> Liters")
        print("3. Ounces -> Milliliters")
        print("4. Milliliters -> Ounces")
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
            print("Invalid input! Please enter a number between 1-6.")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Invalid input! Volume cannot be a negative input.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter numerical values.")

def liters_to_gallons():
    while True:
        liters = get_positive_float("\nEnter liters: ")
        print(f"\nFormula: {liters} L / 3.78541")
        gallons = liters / 3.78541
        print(f"Result: {liters} L = {gallons:.2f} gallons")
        
        if not repeatConv():
            break

def gallons_to_liters():
    while True:
        gallons = get_positive_float("\nEnter gallons: ")
        print(f"\nFormula: {gallons} gallons * 3.78541")
        liters = gallons * 3.78541
        print(f"Result: {gallons} gallons = {liters:.2f} L")
        
        if not repeatConv():
            break

def ounces_to_ml():
    while True:
        ounces = get_positive_float("\nEnter ounces: ")
        print(f"\nFormula: {ounces} oz * 29.5735")
        ml = ounces * 29.5735
        print(f"Result: {ounces} oz = {ml:.2f} mL")
        
        if not repeatConv():
            break

def ml_to_ounces():
    while True:
        ml = get_positive_float("\nEnter milliliters: ")
        print(f"\nFormula: {ml} mL / 29.5735")
        ounces = ml / 29.5735
        print(f"Result: {ml} mL = {ounces:.2f} oz")
        
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