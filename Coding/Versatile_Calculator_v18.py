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
            #--------------------------
            # Code for Addition
            #--------------------------
            if calc_selection == 1:
                while True:
                    try: 
                        count = int(input(f"How many numbers are you adding with: "))
                        if count < 0:
                                print("Error: Enter a valid number")
                                continue
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
                print("Answer printed.")
            #--------------------------
            # Code for Subtraction
            #--------------------------
            elif calc_selection == 2:
                while True:
                    try:
                        count = int(input(f"How many numbers are you subtracting with: "))
                        if count < 0:
                                print("Error: Enter a valid number")
                                continue
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
            #--------------------------
            # Code for Multiplication
            #--------------------------
            elif calc_selection == 3:
                while True:
                    try:
                        count = int(input(f"How many numbers are you multiplying with: "))
                        if count < 0:
                                print("Error: Enter a valid number")
                                continue
                        break
                    except:
                        print("Error: Enter a number")
                        continue
                numbers_list = []
                for i in range(count):
                    while True:
                        try:
                            num = float(input(f"Enter number {i + 1}: "))
                            if isinstance(num,(int,float)):
                                break
                        except:
                            print("Error: Enter a number")
                            continue



                        
                        
                    numbers_list.append(num)
                total = 1
                for num in numbers_list:
                    previous_total = total
                    total = total * num
                    print(f"{previous_total} * {num} = {total:.3f}")
                print(f"Your answer is: {total:.3f}")
                print("Answer printed.")
            #--------------------------
            # Code for Division
            #--------------------------
            elif calc_selection == 4:
                while True:
                    try:
                        count = int(input(f"How many numbers are you dividing with: "))
                        if count < 0:
                                print("Error: Enter a valid number")
                                continue
                        break
                    except:
                        print("Error: Enter a number")
                    continue
                numbers_list = []
                
                for i in range(count):
                    while True:
                        try:
                
                            num = float(input(f"Enter number {i + 1} (the number you want to divide needs to be the first number): "))
                            if isinstance(num,(int,float)):
                                break
                        except:
                            print("Error: Enter a number")
                            continue
                    
                    numbers_list.append(num)

                total = numbers_list[0]

                
                for num in numbers_list[1:]:
                    if num == 0:
                        print("Error: Cannot divide by zero!")
                        return None 
                        
                    previous_total = total
                    total = total / num

                    
                    print(f"{previous_total} / {num} = {total:.3f}")
                print(f"Your answer is: {total:.3f}")

                print("Answer printed.")
            #--------------------------
            # Code for Absolute Value
            #--------------------------
            elif calc_selection == 5:
                while True:
                    try:
                        num = float(input("Enter number for Absolute Value: "))
                        break
                    except:
                        print("Error: Enter a number")
                        
                print(f"Your answer is: {abs(num)}")
                print("Answer printed.")

        # ==========================================
        # SECTION 2: ADVANCED MATH CALCULATIONS 
        # ==========================================
        elif section_choice == 2:
            #--------------------------
            # Code for Factorial
            #--------------------------
            if calc_selection_2 == 1:
                while True:
                    try:
                        num = int(input("Enter a whole number for Factorial: "))
                        if num < 0:
                            print("Error: Enter a number greater than zero")
                            continue
                        break
                    except:
                        print("Error: Enter a number")
                print(f"Your answer is: {math.factorial(num)}")
                print("Answer printed.")
            #--------------------------
            # Code for Square Root
            #--------------------------    
            elif calc_selection_2 == 2:
                while True:
                    try:
                        root = int(input("Enter your root(just enter the number ex: square root would be 2,and cube root would be 3, and etc., Highest root is 10): "))
                        if(root < 2 or root > 10):
                            print("Error:Enter numebr greater or equal to 2 and a number less than or equal to 10")
                            continue
                        break
                    except:
                        print("Error: You have to enter a number")
                        continue
                while True:
                    try:
                        number = float(input("Enter your number/base: "))
                        if(number < 0):
                            print("Error: Enter a number greater than zero")
                            continue
                        break
                    except:
                        print("Error: Enter a number")
                        continue

                
                square_root = math.sqrt(number)
                cube_root = math.cbrt(number)
                fourth_root = math.sqrt(math.sqrt(number))

                fifth_root = math.cbrt(math.sqrt(number))
                sixth_root = math.sqrt(math.sqrt(math.sqrt(number)))
                seventh_root = math.cbrt(math.sqrt(math.sqrt(number)))
                eight_root = math.sqrt(math.sqrt(math.sqrt(math.sqrt(math.sqrt(number)))))
                nineth_root = math.cbrt(math.cbrt(math.cbrt(number)))
                tenth_root = math.cbrt(math.cbrt(math.sqrt(math.sqrt(number))))
                if(root == 2):
                    print(f"Your answer is: {square_root:.5f}")
                if(root == 3):
                    print(f"Your answer is: {cube_root:.5f}")
                if(root == 4):
                    print(f"Your answer is: {fourth_root:.5f}")
                if(root == 5):
                    print(f"Your answer is: {fifth_root:.5f}")
                if(root == 6):
                    print(f"Your answer is: {sixth_root:.5f}")
                if(root == 7):
                    print(f"Your answer is: {seventh_root:.5f}")
                if(root == 8):
                    print(f"Your answer is: {eight_root:.5f}")
                if(root == 9):
                    print(f"Your answer is: {nineth_root:.5f}")
                if(root == 10):
                    print(f"Your answer is: {tenth_root:.5f}")
                
                print("Answer printed.")
            #------------------------------
            # Code for Power of Exponents
            #------------------------------    
            elif calc_selection_2 == 3:
                while True:
                    try:
                        base = float(input("Enter base number: "))
                        break
                    except:
                        print("Error: Enter a number")
                        continue
                while True:
                    try:
                        exp = float(input("Enter exponent power(): "))
                        break
                    except:
                        print("Error: Enter a number")
                        continue
                print(f"Your answer is: {base ** exp:.3f}")
                print("Answer printed.")
            #--------------------------------
            # Code for Fraction to Decimal
            #--------------------------------      
            elif calc_selection_2 == 4:
                while True:
                    try:
                        numerator = int(input(f"Enter your numerator here(no decimals): "))
                        break
                    except:
                        print("Error: Enter a number")
                        continue
                while True:
                    try:
                        denominator = int(input(f"Enter your denominator here(no decimals): "))
                        break
                    except: 
                        print("Error: Enter a number")
                        continue

                total = numerator/denominator
                print(f"Your answer is: {total:.10f}")
                print("Answer printed.")
            #-------------------------------- 
            # Code for Deciaml to Fractions
            #-------------------------------- 
            elif calc_selection_2 == 5:
                while True:

                    from fractions import Fraction
                    try:
                        decimal_float = float(input("Enter here the decimal you want to turn into a fraction: "))
                        break
                    except:
                        print("Error: Enter a number or decimal")
                        continue
            

                fraction = Fraction(decimal_float).limit_denominator()
            
                

                print(f"Your answer is: {fraction}")
                print("Answer printed.")

        # ==========================================
        # SECTION 3: GEOMETRY OPERATIONS
        # ==========================================
        elif section_choice == 3:
            # GEOMETRY OPERATIONS menu (If geometry_selection == 1)
            if geometry_selection == 1:
                #-------------------------------- 
                # Code for Cosine
                #-------------------------------- 
                if calc_selection_3 == 1:
                    while True:
                        try:
                            print("What are you solving for")
                            print(f"1. Find Side Length\n2. Find Angle\n3. Find cosine of a number")
                            angle_or_side = int(input(f"Enter 1 or 2 or 3 for what you need: "))
                            if(angle_or_side < 1 or angle_or_side > 3):
                                print("Error: Enter a number within the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    # Find Side Length         
                    if(angle_or_side == 1 ):
                        print("What side are you solving for")
                        print(f"1. Adjacent\n2. Hypotenuse")
                        while True:
                            try:
                                adjacent_or_hypotenuse = int(input(f"Enter 1 or 2 for what you need: "))
                                if(adjacent_or_hypotenuse < 1 or adjacent_or_hypotenuse > 2):
                                    print("Error: Enter a number within the range")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        while True:
                            try:
                                angle_deg = float(input("Enter the angle in degrees: "))
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                                
                        angle_rad = math.radians(angle_deg)
                                
                            
                            
                    # Find Adjacent Side        
                    if(adjacent_or_hypotenuse == 1):
                        while True:
                            try:
                                hyp = float(input("Enter the length of the hypotenuse: "))
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                            
                        adj = hyp * math.cos(angle_rad)
                        
                        result = adj
                        print(f"Your answer is: {result:.5f}")
                        print("Answer printed.")
                    # Find Hypotenuse
                    elif(adjacent_or_hypotenuse == 2):
                        while True:
                            try:
                                adj = float(input("Enter the length of the adjacent side: "))
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                            
                        hyp = adj / math.cos(angle_rad)
                        result = hyp
                        print(f"Your answer is: {result:.5f}")
                        print("Answer printed.")
                                        
                            
                # Find Angle        
                elif (angle_or_side == 2):
                    while True:
                        try:
                            adj = float(input("Enter the adjacent side or the top number: "))
                            hyp = float(input("Enter the hypotenuse or the bottom number: "))
                            if adj > hyp:
                                print("Error: The adjacent side cannot be larger than the hypotenuse")
                                continue
                            break
                        except:
                            print("Error:Enter a number")
                            continue
                    angle_rad = math.acos(adj/hyp)
                    angle_deg = math.degrees(angle_rad)
                    result = angle_deg
                    print(f"Your answer is(in degress): {result:.5f}")
                    result = angle_rad
                    print(f"Your asnwer is(in radians): {result:.5f}")
                    print("Answer printed.")
                # Find Cosine of a Number
                elif(angle_or_side == 3):
                    while True:
                        try:
                            print(f"1. Cosine\n2. Inverse of cosine")
                            inverse_or_normal = int(input("Enter 1 or 2 : "))
                            if(inverse_or_normal < 1 or inverse_or_normal > 2):
                                print("Error: Enter a number within the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    # Cosine
                    if(inverse_or_normal == 1):
                        while True:
                            try:
                                number = float(input("Enter the number you wanna find the cosine of: "))
                                break
                            except:
                                print("Error:Enter a number")
                                continue
                        cosine = math.cos(number)
                        print(f"Your answer is(in radians): {cosine:.5f}")
                        cosine = math.degrees(cosine)
                        print(f"Your answer is(in degrees): {cosine:.5f}")
                        print("Answer printed.")
                    # Inverse of Cosine
                    elif(inverse_or_normal == 2):
                        while True:
                            try:
                                number = float(input("Enter the number you wanna find the inverse of cosine of(number has to be less than one and cannot be negative ): "))
                                if(number > 1 or number < 0):
                                    print("Error: Enter a number less than 1 or a number that is not negative")
                                    continue
                                break
                            except:
                                print("Error:Enter a number")
                                continue
                        acosine = math.acos(number)
                        print(f"Your answer is(in radians): {acosine:.5f}")
                        acosine = math.degrees(acosine)
                        print(f"Your answer is(in degrees): {acosine:.5f}")
                        print("Answer printed.")
                #-------------------------------- 
                # Code for Sine
                #-------------------------------- 
                elif calc_selection_3 == 2:
                    print("Hello")
                    
                
                
                
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