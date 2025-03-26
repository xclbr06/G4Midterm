# CliniCon: A Clinic-Based Unit Measurement Converter

import modules.heightModule as height
import modules.weightModule as weight
import modules.tabletModule as tablet
import modules.liquidModule as liquid
import modules.tempbpModule as temp_bp

def main_menu():
    menuOptions = {
        '1': height.heightMenu,
        '2': weight.weightMenu,
        '3': tablet.tabletMenu,
        '4': liquid.liquidMenu,
        '5': temp_bp.tempbpMenu,
        '6': exit_program
    }
    
    while True:
        print("\n<=== CliniCon: A Clinic-Based Unit Measurement Converter ===>")
        print("1. Height Measurement")
        print("2. Weight Measurement")
        print("3. Tablet Medication Dosages")
        print("4. Liquid Medication Dosages")
        print("5. Temperature and Blood Pressure")
        print("6. Exit Program")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice in menuOptions:
            menuOptions[choice]()
        else:
            print("Invalid input! Please enter a number between 1-6.")

def exit_program():
    print("\nExiting program. Goodbye and Have a Nice Day!")
    exit()

if __name__ == "__main__":
    main_menu()