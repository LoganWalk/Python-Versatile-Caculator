global answer_1
global answer_2
global answer_3
global answer_4
global answer_5
global answer_6   
import math
global calc_selection
global calc_selection_2
global calc_selection_3
global section_choice 
global selection 
global geometry_selection
SECTIONS = [
    "Basic Math", 
    "Advanced Math", 
    "Geometry", 
    "Algebra 1", 
    "Trigonometry", 
    "Calculus", 
    "Algebra 2",
    "Statistics"
]

BASIC_MATH_OPTIONS = [
    "Addition", 
    "Subtraction", 
    "Multiplication", 
    "Division", 
    "Absolute Value"
    
]
ADVANCED_MATH_OPTIONS = [
    "Factorial",
    "Square Root",
    "Power of Exponents",
    "Fraction to Decimal",
    "Decimal to Fraction"
]
GEOMETERY_SECTIONS=[
    "Operations",
    "Formulas"
]
GEOMETERY_OPERATIONS = [
    "Cosine",
    "Sine",
    "Tangent",
    "Angle of a Line",
    "Vector Dot Product",
    "Radian to Degree",
    "Degree to Radian"
]
GEOMETERY_FORMULAS = [
    "Square/Rectangle Area",
    "Triangle Area",
    "Polygon Area",
    "Circle Area",
    "Eclipse Area",
    "Sector of Circle Area",
    "Trapezoid Area",
    "Rhombus Area"
]


def section_selection():
    global selection
    print("What section are you looking for?")
    for index, section in enumerate(SECTIONS, start=1):
        print(f"{index}. {section}")
        
    while True:
        try:
            answer_1 = int(input("Enter the number next to the section you need: "))
            if(answer_1 <= 0 or answer_1 > 5):
                print(f"Enter a number in the range")
                continue
        except:
            print("Error: Enter a number")
            continue

        selection = answer_1

        return answer_1


def basic_math_selection():
    if(selection == 1):
        print("What calculation do you need to do?")
            
            
        for index, calc in enumerate(BASIC_MATH_OPTIONS, start=1):
                print(f"{index}. {calc}")
        while True:
                try:    
                    answer_2 = int(input("Enter the number by what calculation you need to do: "))
                    if(answer_2 <= 0 or answer_2 > 8):
                        print(f"Enter a number in the range")
                        continue
                except:
                    print("Error: Enter a number")
                    continue
                        
                return answer_2

def advanced_math_selection():
    if(selection== 2):
        print("What calculation do you need to do?")
        
        
        for index, calc in enumerate(ADVANCED_MATH_OPTIONS, start=1):
            print(f"{index}. {calc}")
        while True:
            try:   
                answer_3 = int(input("Enter the number by what calculation you need to do: "))
                if(answer_3 <= 0 or answer_3 > 5):
                    print(f"Enter a number in the range")
                    continue
            except:
                print("Error: Enter a number")
                continue
            
            return answer_3

def geomertery_operation_formula_selection():
    global geometry_selection
    if (selection == 3):
        for index, calc in enumerate(GEOMETERY_SECTIONS, start=1):
            print(f"{index}. {calc}")
        while True:
            try: 
                answer_4= int(input("Enter the number by what section you need to do: "))
                if(answer_4 <= 0 or answer_4 > 2):
                    print(f"Enter a number in the range")
                    continue
            except:
                print("Error: Enter a number")
                continue
            geometry_selection = answer_4
            break
    if(answer_4 == 1):
        for index, calc in enumerate(GEOMETERY_OPERATIONS, start=1):
            print(f"{index}. {calc}")
        while True:
            try:  

                answer_5= int(input("Enter the number by what section you need to do: "))
                if(answer_5 <= 0 or answer_5 > 7):
                    print(f"Enter a number in the range")
                    continue
            except:
                print("Error: Enter a number")
                continue
            return answer_5
    if(answer_4 == 2):
        for index, calc in enumerate(GEOMETERY_FORMULAS, start=1):
            print(f"{index}. {calc}")
        while True:
            try:  
                answer_6= int(input("Enter the number by what section you need to do: "))
                if(answer_6 <= 0 or answer_6 > 8):
                    print(f"Enter a number in the range")
                    continue
            except:
                print("Error: Enter a number")
                continue
            return answer_6

def commit_calculations():
    while True:
        section_choice = section_selection()

        # Initialize all tracking variables to None safely
        calc_selection = None
        calc_selection_2 = None
        calc_selection_3 = None

        # 1. Fetch menu decisions based on what category they chose
        if section_choice == 1:
            calc_selection = basic_math_selection()
        elif section_choice == 2:
            calc_selection_2 = advanced_math_selection()
        elif section_choice == 3:
            calc_selection_3 = geomertery_operation_formula_selection()
        
        # ==========================================
        # SECTION 1: BASIC MATH CALCULATIONS
        # ==========================================
        if section_choice == 1:
            if calc_selection == 1:
                while True:
                    try: 
                        count = int(input(f"How many numbers are you adding with: "))
                        break
                    except:
                        print("Error: Enter a number")
                        continue
                numbers_list = []
                for i in range(count):
                    while True:
                        try:
                            num = float(input(f"Enter number {i + 1}(you will enter your first number then it will ask you what you next number is and etc.): "))
                            if isinstance(num,(int,float)):
                                break
                        except:
                            print("Error: Enter a number")       
                            continue           
                    numbers_list.append(num)
                total = sum(numbers_list)
                print(f"Your answer is: {total:.10f}")
                print("Answer printed.") # Do not use 'return'
            elif calc_selection == 2:
                while True:
                    try:
                        count = int(input(f"How many numbers are you subtracting with: "))
                        break
                    except:
                        print("Error: Enter a number")
                        continue
                numbers_list = []
                for i in range(count):
                    while True:
                        try:
                            num = float(input(f"Enter number {i + 1}(the order of the numbers will change the answer ex:10-6 =4, 6-10 = -4): "))
                            if isinstance(num,(int,float)):
                                break
                        except:
                            print("Error: Enter a number")
                            continue
                    
                    numbers_list.append(num)
                total = numbers_list[0]
                for num in numbers_list[1:]:
                    total = total - num
                print(f"Your answer is: {total:.10f}")
                print("Answer printed.")
            elif calc_selection == 3:
                # [Your Multiplication Logic here]
                print("Answer printed.")
            elif calc_selection == 4:
                # [Your Division Logic here]
                print("Answer printed.")
            elif calc_selection == 5:
                # Absolute Value Logic
                num = float(input("Enter number for Absolute Value: "))
                print(f"Your answer is: {abs(num)}")

        # ==========================================
        # SECTION 2: ADVANCED MATH CALCULATIONS 
        # ==========================================
        elif section_choice == 2:
            if calc_selection_2 == 1:
                # Factorial Logic
                num = int(input("Enter a whole number for Factorial: "))
                print(f"Your answer is: {math.factorial(num)}")
                
            elif calc_selection_2 == 2:
                # Square Root Logic
                num = float(input("Enter number for Square Root: "))
                print(f"Your answer is: {math.sqrt(num)}")
                
            elif calc_selection_2 == 3:
                # Power of Exponents Logic
                base = float(input("Enter base number: "))
                exp = float(input("Enter exponent power: "))
                print(f"Your answer is: {base ** exp}")
                
            elif calc_selection_2 == 4:
                # Fraction to Decimal Logic
                top = float(input("Enter numerator (top): "))
                bottom = float(input("Enter denominator (bottom): "))
                print(f"Your answer is: {top / bottom}")
                
            elif calc_selection_2 == 5:
                # Decimal to Fraction Logic
                from fractions import Fraction
                num = float(input("Enter decimal value (e.g. 0.75): "))
                print(f"Your answer fraction is: {Fraction(num).limit_denominator()}")

        # ==========================================
        # SECTION 3: GEOMETRY CALCULATIONS 
        # ==========================================
        elif section_choice == 3:
            # GEOMETRY OPERATIONS menu (If geometry_selection == 1)
            if geometry_selection == 1:
                if calc_selection_3 == 1:
                    # Cosine Logic
                    deg = float(input("Enter angle in degrees: "))
                    print(f"Your answer is: {math.cos(math.radians(deg))}")
                elif calc_selection_3 == 2:
                    # Sine Logic
                    deg = float(input("Enter angle in degrees: "))
                    print(f"Your answer is: {math.sin(math.radians(deg))}")
                # ... Keep adding Elif statements for Tangent, Vectors, Radian/Degree switches ...
                
                
                
        # ==========================================
        # SECTION 3: GEOMETRY FORMULAS
        # ==========================================
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ==========================================
        # RESTART / STOP SYSTEM 
        # ==========================================
        print("\nCalculation complete.")
        user_choice = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
        if user_choice not in ['yes', 'y']:
            print("Goodbye!")
            break  # Exits the master while loop cleanly
        
        
def main():
    commit_calculations()
    
    
    
    
main()