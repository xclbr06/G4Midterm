def tabletMenu():
    conversion_functions = {
        '1': grams_to_mg,
        '2': mg_to_grams,
        '3': mg_to_mc,
        '4': mc_to_mg,
        '5': grams_to_mc,
        '6': mc_to_grams
    }
    
    while True:
        print("\n<=== Tablet Medication Dosage Conversions ===>")
        print("1. Grams -> Milligrams")
        print("2. Milligrams -> Grams")
        print("3. Milligrams -> Micrograms")
        print("4. Micrograms -> Milligrams")
        print("5. Grams -> Micrograms")
        print("6. Micrograms -> Grams")
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
                print("Invalid input! Dosage cannot be a negative input.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter numerical values.")

def grams_to_mg():
    while True:
        grams = get_positive_float("\nEnter grams: ")
        print(f"\nFormula: {grams} g * 1000")
        mg = grams * 1000
        print(f"Result: {grams} g = {mg} mg")
        
        if not repeatConv():
            break

def mg_to_grams():
    while True:
        mg = get_positive_float("\nEnter milligrams: ")
        print(f"\nFormula: {mg} mg / 1000")
        grams = mg / 1000
        print(f"Result: {mg} mg = {grams:.2f} g")
        
        if not repeatConv():
            break

def mg_to_mc():
    while True:
        mg = get_positive_float("\nEnter milligrams: ")
        print(f"\nFormula: {mg} mg * 1000")
        mcg = mg * 1000
        print(f"Result: {mg} mg = {mcg} mcg")
        
        if not repeatConv():
            break

def mc_to_mg():
    while True:
        mcg = get_positive_float("\nEnter micrograms: ")
        print(f"\nFormula: {mcg} mcg / 1000")
        mg = mcg / 1000
        print(f"Result: {mcg} mcg = {mg:.2f} mg")
        
        if not repeatConv():
            break

def grams_to_mc():
    while True:
        grams = get_positive_float("\nEnter grams: ")
        print(f"\nFormula: {grams} g * 1000000")
        mcg = grams * 1000000
        print(f"Result: {grams} g = {mcg} mcg")
        
        if not repeatConv():
            break

def mc_to_grams():
    while True:
        mcg = get_positive_float("\nEnter micrograms: ")
        print(f"\nFormula: {mcg} mcg / 1000000")
        grams = mcg / 1000000
        print(f"Result: {mcg} mcg = {grams:.2f} g")
        
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