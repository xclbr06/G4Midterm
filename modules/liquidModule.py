def liquidMenu():
    conversion_functions = {
        '1': tablespoons_to_teaspoons,
        '2': teaspoons_to_tablespoons,
        '3': ounces_to_ml,
        '4': ml_to_ounces,
        '5': teaspoons_to_ounces,
        '6': ounces_to_teaspoons
    }
    
    while True:
        print("\n<=== Liquid Medication Dosage Conversions ===>")
        print("1. Tablespoons -> Teaspoons")
        print("2. Teaspoons -> Tablespoons")
        print("3. Ounces -> Milliliters")
        print("4. Milliliters -> Ounces")
        print("5. Teaspoons -> Ounces")
        print("6. Ounces -> Teaspoons")
        print("7. Back to Main Menu")
        print("8. Exit")
        
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
                print("Invalid input! Dosage cannot be a negative input.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter numerical values.")

def tablespoons_to_teaspoons():
    while True:
        tbsp = get_positive_float("Enter tablespoons: ")
        print(f"Formula: {tbsp} tbsp * 3")
        tsp = tbsp * 3
        print(f"{tbsp} tbsp = {tsp:.2f} tsp")
        
        if not repeatConv():
            break

def teaspoons_to_tablespoons():
    while True:
        tsp = get_positive_float("Enter teaspoons: ")
        print(f"Formula: {tsp} tsp / 3")
        tbsp = tsp / 3
        print(f"{tsp} tsp = {tbsp:.2f} tbsp")
        
        if not repeatConv():
            break

def ounces_to_ml():
    while True:
        ounces = get_positive_float("Enter ounces: ")
        print(f"Formula: {ounces} oz * 29.5735")
        ml = ounces * 29.5735
        print(f"{ounces} oz = {ml:.2f} mL")
        
        if not repeatConv():
            break

def ml_to_ounces():
    while True:
        ml = get_positive_float("Enter milliliters: ")
        print(f"Formula: {ml} mL / 29.5735")
        ounces = ml / 29.5735
        print(f"{ml} mL = {ounces:.2f} oz")
        
        if not repeatConv():
            break

def teaspoons_to_ounces():
    while True:
        tsp = get_positive_float("Enter teaspoons: ")
        print(f"Formula: {tsp} tsp * 0.166667")
        ounces = tsp * 0.166667
        print(f"{tsp} tsp = {ounces:.2f} oz")
        
        if not repeatConv():
            break

def ounces_to_teaspoons():
    while True:
        ounces = get_positive_float("Enter ounces: ")
        print(f"Formula: {ounces} oz / 0.166667")
        tsp = ounces / 0.166667
        print(f"{ounces} oz = {tsp:.2f} tsp")
        
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