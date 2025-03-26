def heightMenu():
    conversionFunc = {
        '1': feet_inches_to_cm,
        '2': cm_to_feet_inches,
        '3': feet_inches_to_m,
        '4': m_to_feet_inches,
        '5': cm_to_m,
        '6': m_to_cm
    }
    
    while True:
        print("\n<=== Height Measurement Conversions ===>")
        print("1. Feet & Inches -> Centimeters")
        print("2. Centimeters -> Feet & Inches")
        print("3. Feet & Inches -> Meters")
        print("4. Meters -> Feet & Inches")
        print("5. Centimeters -> Meters")
        print("6. Meters -> Centimeters")
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

def get_positive_float(prompt, is_inches=False):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Invalid input! Height cannot be a negative input.")
                if is_inches:
                    print()  # Add a newline only for inches
            else:
                return value
        except ValueError:
            print("Invalid input! Enter numerical values.")
            if is_inches:
                print()  # Add a newline only for inches

def feet_inches_to_cm():
    while True:
        feet = get_positive_float("\nEnter feet: ")
        inches = get_positive_float("Enter inches: ", is_inches=True)
        print(f"\nFormula: ({feet} feet * 30.48) + ({inches} inches * 2.54)")
        cm = (feet * 30.48) + (inches * 2.54)
        print(f"Result: {feet} feet & {inches} inches = {cm:.2f} cm")
        
        if not repeatConv():
            break

def cm_to_feet_inches():
    while True:
        cm = get_positive_float("\nEnter centimeters: ")
        print(f"\nFormula: {cm} cm / 2.54 = total inches")
        totalInches = cm / 2.54
        feet = int(totalInches // 12)
        inches = totalInches % 12
        print(f"Result: {cm} cm = {feet} feet & {inches:.2f} inches")
        
        if not repeatConv():
            break

def cm_to_m():
    while True:
        cm = get_positive_float("\nEnter centimeters: ")
        print(f"\nFormula: {cm} cm / 100")
        meters = cm / 100
        print(f"Result: {cm} cm = {meters:.2f} meters")
        
        if not repeatConv():
            break

def m_to_cm():
    while True:
        meters = get_positive_float("\nEnter meters: ")
        print(f"\nFormula: {meters} meters * 100")
        cm = meters * 100
        print(f"Result: {meters} meters = {cm:.2f} cm")
        
        if not repeatConv():
            break

def feet_inches_to_m():
    while True:
        feet = get_positive_float("\nEnter feet: ")
        inches = get_positive_float("Enter inches: ", is_inches=True)
        print(f"\nFormula: (({feet} feet * 12) + {inches} inches) * 0.0254")
        meters = ((feet * 12) + inches) * 0.0254
        print(f"Result: {feet} feet & {inches} inches = {meters:.2f} meters")
        
        if not repeatConv():
            break

def m_to_feet_inches():
    while True:
        meters = get_positive_float("\nEnter meters: ")
        print(f"\nFormula: {meters} meters / 0.0254 = total inches")
        totalInches = meters / 0.0254
        feet = int(totalInches // 12)
        inches = totalInches % 12
        print(f"Result: {meters} meters = {feet} feet & {inches:.2f} inches")
        
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