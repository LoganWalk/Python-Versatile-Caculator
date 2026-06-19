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
    "Algebra", 
    "Trigonometry", 
    "Calculus", 
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
    

    
    "Square/Cube/Rectangle/Rectanglular Prism: Perimeter, Area, Volume, Surface Area",
    "Triangle: Perimeter, Area",
    "Cylinder: Volume, Surface Area",
    "Cone: Volume, Surface Area",
    "Circle/Sphere: Circumference, Area, Volume, Surface Area",
    "Polygon: Perimeter, Area, Volume, Surface Area",
    "Polygon Pyramid: Volume, Surface Area",
    "Trapezoid/Trapezoidal Prism: Perimeter, Area, Volume, Surface Area",
    "Rhombus: Perimeter, Area",
    
    
    "Distance Formula",
    "Midpoint Formula",
    "Slope Formula",
    "Pythgeroeam Therom Formula",
    "Interior Angles of a Polygon Formula",
    "Interior Angle Sum of a Polygon Formula",
    "Herons Formula"
    
    
    
    

    
    
    
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
                    
                    while True:
                        try:
                            print("What are you solving for")
                            print(f"1. Find Side Length\n2. Find Angle\n3. Find sine of a number")
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
                        print(f"1. Opposite\n2. Hypotenuse")
                        while True:
                            try:
                                opposite_or_hypotenuse = int(input(f"Enter 1 or 2 for what you need: "))
                                if(opposite_or_hypotenuse < 1 or opposite_or_hypotenuse > 2):
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
                                
                            
                            
                    # Find Opposite Side        
                    if(opposite_or_hypotenuse == 1):
                        while True:
                            try:
                                hyp = float(input("Enter the length of the hypotenuse: "))
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                            
                        opp = hyp * math.sin(angle_rad)
                        
                        result = opp
                        print(f"Your answer is: {result:.5f}")
                        print("Answer printed.")
                    # Find Hypotenuse
                    elif(adjacent_or_hypotenuse == 2):
                        while True:
                            try:
                                opp = float(input("Enter the length of the opposite side: "))
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                            
                        hyp = opp / math.sin(angle_rad)
                        result = hyp
                        print(f"Your answer is: {result:.5f}")
                        print("Answer printed.")
                                        
                            
                    # Find Angle        
                    elif (angle_or_side == 2):
                        while True:
                            try:
                                opp = float(input("Enter the opposite side or the top number: "))
                                hyp = float(input("Enter the hypotenuse or the bottom number: "))
                                if adj > hyp:
                                    print("Error: The opposite side cannot be larger than the hypotenuse")
                                    continue
                                break
                            except:
                                print("Error:Enter a number")
                                continue
                        angle_rad = math.asin(opp/hyp)
                        angle_deg = math.degrees(angle_rad)
                        result = angle_deg
                        print(f"Your answer is(in degress): {result:.5f}")
                        result = angle_rad
                        print(f"Your asnwer is(in radians): {result:.5f}")
                        print("Answer printed.")
                    # Find Sine of a Number
                    elif(angle_or_side == 3):
                        while True:
                            try:
                                print(f"1. Sine\n2. Inverse of sine")
                                inverse_or_normal = int(input("Enter 1 or 2 : "))
                                if(inverse_or_normal < 1 or inverse_or_normal > 2):
                                    print("Error: Enter a number within the range")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        # Sine
                        if(inverse_or_normal == 1):
                            while True:
                                try:
                                    number = float(input("Enter the number you wanna find the sine of: "))
                                    break
                                except:
                                    print("Error:Enter a number")
                                    continue
                            sine = math.sin(number)
                            print(f"Your answer is(in radians): {sine:.5f}")
                            sine = math.degrees(sine)
                            print(f"Your answer is(in degrees): {sine:.5f}")
                            print("Answer printed.")
                        # Inverse of Cosine
                        elif(inverse_or_normal == 2):
                            while True:
                                try:
                                    number = float(input("Enter the number you wanna find the inverse of sine of(number has to be less than one and cannot be negative ): "))
                                    if(number > 1 or number < 0):
                                        print("Error: Enter a number less than 1 or a number that is not negative")
                                        continue
                                    break
                                except:
                                    print("Error:Enter a number")
                                    continue
                            asine = math.asin(number)
                            print(f"Your answer is(in radians): {asine:.5f}")
                            asine = math.degrees(asine)
                            print(f"Your answer is(in degrees): {asine:.5f}")
                            print("Answer printed.")
                #-------------------------------- 
                # Code for Tangent
                #-------------------------------- 
                elif calc_selection_3 == 3:
                    while True:
                        try:
                            print("What are you solving for")
                            print(f"1. Find Side Length\n2. Find Angle\n3. Find sine of a number")
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
                        print(f"1. Opposite\n2. Adjacent")
                        while True:
                            try:
                                opposite_or_adjacent = int(input(f"Enter 1 or 2 for what you need: "))
                                if(opposite_or_adjacent < 1 or opposite_or_adjacent > 2):
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
                                
                            
                            
                    # Find Opposite Side        
                    if(opposite_or_adjacent == 1):
                        while True:
                            try:
                                adj = float(input("Enter the length of the adjacent side: "))
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                            
                        opp = adj * math.tan(angle_rad)
                        
                        result = opp
                        print(f"Your answer is: {result:.5f}")
                        print("Answer printed.")
                    # Find Adjacent Side
                    elif(opposite_or_adjacent == 2):
                        while True:
                            try:
                                opp = float(input("Enter the length of the opposite side: "))
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                            
                        adj = opp / math.tan(angle_rad)
                        result = adj
                        print(f"Your answer is: {result:.5f}")
                        print("Answer printed.")
                                    
                        
                    # Find Angle        
                    elif (angle_or_side == 2):
                        while True:
                            try:
                                opp = float(input("Enter the opposite side or the top number: "))
                                adj = float(input("Enter the adjacent side or the bottom number: "))
                                break
                            except:
                                print("Error:Enter a number")
                                continue
                        angle_rad = math.atan(opp/adj)
                        angle_deg = math.degrees(angle_rad)
                        result = angle_deg
                        print(f"Your answer is(in degress): {result:.5f}")
                        result = angle_rad
                        print(f"Your asnwer is(in radians): {result:.5f}")
                        print("Answer printed.")
                    # Find Tangent of a Number
                    elif(angle_or_side == 3):
                        while True:
                            try:
                                print(f"1. Tangent\n2. Inverse of tangent")
                                inverse_or_normal = int(input("Enter 1 or 2 : "))
                                if(inverse_or_normal < 1 or inverse_or_normal > 2):
                                    print("Error: Enter a number within the range")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        # Tangent
                        if(inverse_or_normal == 1):
                            while True:
                                try:
                                    number = float(input("Enter the number you wanna find the tangent of: "))
                                    break
                                except:
                                    print("Error:Enter a number")
                                    continue
                            tan = math.tan(number)
                            print(f"Your answer is(in radians): {tan:.5f}")
                            tan = math.degrees(tan)
                            print(f"Your answer is(in degrees): {tan:.5f}")
                            print("Answer printed.")
                        # Inverse of Tangent
                        elif(inverse_or_normal == 2):
                            while True:
                                try:
                                    number = float(input("Enter the number you wanna find the inverse of tangent of: "))
                                    break
                                except:
                                    print("Error: Enter a number")
                                    continue
                            atan = math.atan(number)
                            print(f"Your answer is(in radians): {atan:.5f}")
                            atan = math.degrees(atan)
                            print(f"Your answer is(in degrees): {atan:.5f}")
                            print("Answer printed.") 
                #-------------------------------- 
                # Code for Angle Of A Line
                #-------------------------------- 
                elif calc_selection_3 == 4:
                    while True:
                        try:
                            x1 = float(input("Enter the first x-coordinate: "))
                            y1 = float(input("Enter the first y-coordinate: "))
                            x2 = float(input("Enter the second x-coordinate: "))
                            y2 = float(input("Enter the second y-coordinate: "))
                            
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    dx = x2 - x1
                    dy = y2 - y1

                    angle_rad = math.atan2(dy,dx)
                    angle_deg = math.degrees(angle_rad)

                    angle_deg = angle_deg % 360

                    result = angle_deg
                    print(f"Your answer is(in degrees): {result}")
                    result = angle_rad
                    print(f"Your answer is(in radians): {result}")
                    print("Answer Printed.")
                #-------------------------------- 
                # Code for Vector Dot Product
                #-------------------------------- 
                elif calc_selection_3 == 5:
                    while True:
                        try:
                            dimensions = int(input("Enter the number of dimensions (e.g., 2, 3): "))
                            if dimensions < 0:
                                print("Error: Dimensions must be 1 or greater.")
                                continue
                            if dimensions >= 1:
                                break
                        except: 
                            print("Error:Enter a number")
                            continue
                    while True:
                        try:
                            print("Enter Values for Vector A: ")
                            vector_a = []
                            for i in range(dimensions):
                                val = float(input(f"Component A[{i+1}]: "))
                                vector_a.append(val)
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    while True:
                        try:
                            print("Enter Values for Vector B: ")
                            vector_b = []
                            for i in range(dimensions):
                                val = float(input(f"Component B[{i+1}]: "))
                                vector_b.append(val)
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

                    print("------Answers---------")
                    print(f"Vector A: {vector_a}")
                    print(f"Vector B: {vector_b}")
                    print(f"Dot Product: {dot_product:.5f}")
                    print("Answer Printed.")
                #-------------------------------- 
                # Code for Radians to Degrees
                #-------------------------------- 
                elif calc_selection_3 == 6:
                    while True:
                        try: 
                            radians = float(input("Enter radians to turn into degrees: "))
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    degrees = radians * 57.2958

                    print(f"Your answer in degrees is: {degrees:.5f}")
                    print("Answer Printed.")
                #-------------------------------- 
                # Code for Degrees to Radians
                #-------------------------------- 
                elif calc_selection_3 == 7:
                    while True:
                        try: 
                            degrees = float(input("Enter degrees to turn into radians: "))
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    radians = degrees * 0.0174533

                    print(f"Your answer in degrees is: {radians:.5f}")
                    print("Answer Printed.")
                
                
                
                
            # ==========================================
            # SECTION 3: GEOMETRY FORMULAS
            # ==========================================
            if geometry_selection == 2:
                    


                #-------------------------------- 
                # Code for Square/Cube/Rectangle/Rectangular Prism
                #-------------------------------- 
                if(calc_selection_3 == 1):
                    while True:
                        try: 
                            print(f"1.Perimeter\n2.Area\n3.Volume\n4.Surface Area")
                            select_formula = int(input("Enter the number by what to want to do: "))
                            if(select_formula < 1 or select_formula > 4):
                                print("Error: Enter a number in the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    # Perimeter
                    if(select_formula == 1):
                        while True:
                            try:
                                side_1 = float(input("Enter the first side: "))
                                side_2 = float(input("Enter the second side: "))
                                side_3 = float(input("Enter the third side: "))
                                side_4 = float(input("Enter the fourth side: "))
                                if( side_1 < 0 or side_2 < 0 or side_3 < 0 or side_4 < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        perimeter = side_1 + side_2 + side_3 + side_4
                        result = perimeter
                        print(f"Your answer is: {result}")
                        print("Answer Printed.")
                            
                    # Area
                    elif(select_formula == 2):
                        while True:
                            try:
                                width = float(input("Enter the width of the object: "))
                                length = float(input("Enter the length of the object: "))
                                if(width < 0 or length < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        result = width * length

                        print(f"Your ansswer is: {result}")
                        print("Answer Printed.")
                    # Volume
                    elif(select_formula == 3):
                        while True:
                            try: 
                                height = float(input("Enter the height: "))
                                width = float(input("Enter the width: "))
                                length = float(input("Enter the length: "))
                                if(width < 0 or length < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        volume = height * width * length

                        print(f"Your ansswer is: {volume}")
                        print("Answer Printed.")
                    #Surface Area
                    elif(select_formula == 4):
                        while True:
                            try: 
                                height = float(input("Enter the height: "))
                                width = float(input("Enter the width: "))
                                length = float(input("Enter the length: "))
                                if(width < 0 or length < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        sa = 2((length * width) + (length * height) + (Width * height))

                        print(f"Your ansswer is: {sa}")
                        print("Answer Printed.")

                    
                    
                #-------------------------------- 
                # Code for Triangle
                #-------------------------------- 
                elif(calc_selection_3 == 2):
                    while True:
                        try: 
                            print(f"1.Perimeter\n2.Area")
                            select_formula = int(input("Enter the number by what to want to do: "))
                            if(select_formula < 1 or select_formula > 2):
                                print("Error: Enter a number in the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    # Perimeter
                    if(select_formula == 1):
                        while True:
                            try:
                                side_1 = float(input("Enter the first side: "))
                                side_2 = float(input("Enter the second side: "))
                                side_3 = float(input("Enter the third side: "))
                                if( side_1 < 0 or side_2 < 0 or side_3 < 0 ):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        perimeter = side_1 + side_2 + side_3
                        result = perimeter
                        print(f"Your answer is: {result}")
                        print("Answer Printed.")
                    # Area
                    elif(select_formula == 2):
                        while True:
                            try:
                                width = float(input("Enter the width of the object: "))
                                height = float(input("Enter the height of the object: "))
                                if(width < 0 or height < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        result = width * height / 2

                        print(f"Your ansswer is: {result}")
                        print("Answer Printed.")
                
                
                
                #-------------------------------- 
                # Code for Cylinder
                #-------------------------------- 
                elif(calc_selection_3 == 3):
                    while True:
                        try: 
                            print(f"1.Volume\n2.Surface Area")
                            select_formula = int(input("Enter the number by what to want to do: "))
                            if(select_formula < 1 or select_formula > 2):
                                print("Error: Enter a number in the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    # Volume
                    if(select_formula == 1):
                        while True:
                            try: 
                                radius = float(input("Enter the radius of the cylinder: "))
                                height = float(input("Enter the height of the cylinder: "))
                                if(height < 0 or radius < 0):
                                    print("Error: Cylinder cant have negative radius")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                            continue
                        area = math.pi * radius ** 2
                        volume = area * height
                        print(f"Your answer is: {volume}")
                        print("Answer Printed.")
                    # Surface Area
                    elif(select_formula == 2):
                        while True:
                            try: 
                                radius = float(input("Enter the radius of the cylinder: "))
                                height = float(input("Enter the height of the cylinder: "))
                                if(height < 0 or radius < 0):
                                    print("Error: Cylinder cant have negative radius")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                            continue
                        sa = 2(math.pi * (radius **2)) + 2(math.pi * radius * height)
                        print(f"Your answer is: {sa}")
                        print("Answer Printed.")


                    
                    
                #-------------------------------- 
                # Code for Cone
                #-------------------------------- 
                elif(calc_selection_3 == 4):
                    while True:
                        try: 
                            print(f"1.Volume\n2.Surface Area")
                            select_formula = int(input("Enter the number by what to want to do: "))
                            if(select_formula < 1 or select_formula > 2):
                                print("Error: Enter a number in the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    # Volume
                    if(select_formula == 1):
                        while True:
                            try: 
                                radius = float(input("Enter the radius of the cone: "))
                                height = float(input("Enter the height of the cone: "))
                                if(height < 0 or radius < 0):
                                    print("Error: Cone cant have negative radius")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                            continue
                        area = math.pi * radius ** 2
                        volume = (area * height) * 1/3
                        print(f"Your answer is: {volume}")
                        print("Answer Printed.")
                    # Surface Area
                    if(select_formula == 2):
                        while True:
                            try: 
                                radius = float(input("Enter the radius of the cone: "))
                                slant_height = float(input("Enter the slant height of the cone: "))
                                if(height < 0 or radius < 0):
                                    print("Error: Cone cant have negative radius")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                            continue
                        area = math.pi * radius ** 2
                        sa = area + math.pi * radius * slant_height
                        print(f"Your answer is: {sa}")
                        print("Answer Printed.")
                    
                #-------------------------------- 
                # Code for Circle/Sphere
                #-------------------------------- 
                elif(calc_selection_3 == 5):
                    while True:
                        try: 
                            print(f"1.Circumference\n2.Area\n3.Volume\n4.Surface Area")
                            select_formula = int(input("Enter the number by what to want to do: "))
                            if(select_formula < 1 or select_formula > 4):
                                print("Error: Enter a number in the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    #Cirumfrerence
                    if(select_formula == 1):
                        while True:
                            try:
                                radius = float(input("Enter the radius of your circle: "))
                                if(radius < 0):
                                    print("Error: Circle cant have negative radius")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        
                        circumference = 2 * math.pi * radius

                        print(f"Your answer is: {circumference}")
                        print("Answer Printed.")
                    # Area
                    elif(select_formula == 2):
                        while True:
                            try:
                                radius = float(input("Enter the radius of your circle: "))
                                if(radius < 0):
                                    print("Error: Circle cant have negative radius")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        area = math.pi * radius ** 2

                        print(f"Your answer is: {area}")
                        print("Answer Printed.")
                    # Volume
                    elif(select_formula == 3):
                        while True:
                            try:
                                radius = float(input("Enter the radius of your circle: "))
                                if(radius < 0):
                                    print("Error: Circle cant have negative radius")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        volume = (math.pi * radius ** 3) * 4/3

                        print(f"Your answer is: {volume}")
                        print("Answer Printed.")
                    #Surface Area
                    elif(select_formula == 4):
                        while True:
                            try:
                                radius = float(input("Enter the radius of your circle: "))
                                if(radius < 0):
                                    print("Error: Circle cant have negative radius")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        area = math.pi * radius ** 2
                        sa = 4 * area

                        print(f"Your answer is: {sa}")
                        print("Answer Printed.")
                        
                    
                    
                #-------------------------------- 
                # Code for Polygon
                #-------------------------------- 
                elif(calc_selection_3 == 6):
                    while True:
                        try: 
                            print(f"1.Perimeter\n2.Area\n3.Volume\n4.Surface Area")
                            select_formula = int(input("Enter the number by what to want to do: "))
                            if(select_formula < 1 or select_formula > 4):
                                print("Error: Enter a number in the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    # Perimeter
                    if(select_formula == 1):
                        while True:
                            try:
                                amount_of_sides = int(input("Enter the amount of sides: "))
                                if(amount_of_sides < 0):
                                    print("Error: A polygon cant have negative sides")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        sides = []
                        for index in range(amount_of_sides):
                            side_value = int(input(f"Enter the value of side {index + 1}: "))
                            sides.append(side_value)
                        perimeter = sum(sides)

                        print(f"Your answer is: {perimeter}")
                        print("Answer Printed.")
                    # Area
                    elif(select_formula == 2):
                        while True:
                            try:
                                amount_of_sides = int(input("Enter the amount of sides: "))
                                apothem = float(input("Enter the length of the apothem: "))
                                if(amount_of_sides < 0 or apothem < 0):
                                    print("Error: A polygon cant have negative sides")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        sides = []
                        for index in range(amount_of_sides):
                            side_value = int(input(f"Enter the value of the side {index + 1}: "))
                            sides.append(side_value)
                        perimeter = sum(sides)

                        area = 0.5 * perimeter * apothem
                        print(f"Your answer is: {area}")
                        print("Answer Printed.")
                    # Volume
                    elif(select_formula == 3):
                        while True:
                            try:
                                amount_of_sides = int(input("Enter the amount of sides: "))
                                apothem = float(input("Enter the length of the apothem: "))
                                height = float(input("Enter the height: "))
                                if(amount_of_sides < 0 or apothem < 0):
                                    print("Error: A polygon cant have negative sides")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        sides = []
                        for index in range(amount_of_sides):
                            side_value = int(input(f"Enter the value of the side {index + 1}: "))
                            sides.append(side_value)
                        perimeter = sum(sides)

                        area = 0.5 * perimeter * apothem
                        volume = area * height
                        print(f"Your answer is: {volume}")
                        print("Answer Printed.")
                    # Surface Area
                    elif(select_formula == 4):
                        while True:
                            try:
                                amount_of_sides = int(input("Enter the amount of sides: "))
                                apothem = float(input("Enter the length of the apothem: "))
                                height = float(input("Enter the height: "))
                                if(amount_of_sides < 0 or apothem < 0):
                                    print("Error: A polygon cant have negative sides")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        sides = []
                        for index in range(amount_of_sides):
                            side_value = int(input(f"Enter the value of the side {index + 1}: "))
                            sides.append(side_value)
                        perimeter = sum(sides)

                        area = 0.5 * perimeter * apothem
                        sa = 2 * area + perimeter * height
                        print(f"Your answer is: {sa}")
                        print("Answer Printed.")
                
                
                
                #-------------------------------- 
                # Code for Polygon Pyramid
                #-------------------------------- 
                elif(calc_selection_3 == 7):
                    while True:
                        try: 
                            print(f"1.Volume\n2.Surface Area")
                            select_formula = int(input("Enter the number by what to want to do: "))
                            if(select_formula < 1 or select_formula > 2):
                                print("Error: Enter a number in the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    #volume 
                    if( select_formula == 1):
                        while True:
                            try:
                                amount_of_sides = int(input("Enter the amount of sides: "))
                                apothem = float(input("Enter the length of the apothem: "))
                                height = float(input("Enter the height: "))
                                if(amount_of_sides < 0 or apothem < 0 or height < 0):
                                    print("Error: A polygon cant have negative sides")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue




                        sides = []
                        for index in range(amount_of_sides):
                            side_value = int(input(f"Enter the value of the side {index + 1}: "))
                            sides.append(side_value)
                        perimeter = sum(sides)

                        area = 0.5 * perimeter * apothem

                        volume = (area * height ) * 1/3

                        print(f"Your answer is: {volume}")
                        print("Answer Printed.")
                    # Surface Area 
                    elif( select_formula == 2):
                        while True:
                            try:
                                amount_of_sides = int(input("Enter the amount of sides: "))
                                apothem = float(input("Enter the length of the apothem: "))
                                slant_height = float(input("Enter the slant height: "))
                                if(amount_of_sides < 0 or apothem < 0 or height < 0):
                                    print("Error: A polygon cant have negative sides")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue




                        sides = []
                        for index in range(amount_of_sides):
                            side_value = int(input(f"Enter the value of the side {index + 1}: "))
                            sides.append(side_value)
                        perimeter = sum(sides)

                        area = 0.5 * perimeter * apothem

                        sa = area + 1/2 * perimeter * slant_height

                        print(f"Your answer is: {sa}")
                        print("Answer Printed.")

                    
                    
                #-------------------------------- 
                # Code for Trapezoid/Trapezoidal Prism
                #-------------------------------- 
                elif(calc_selection_3 == 8):
                    while True:
                        try: 
                            print(f"1.Perimeter\n2.Area\n3.Volume\n4.Surface Area")
                            select_formula = int(input("Enter the number by what to want to do: "))
                            if(select_formula < 1 or select_formula > 4):
                                print("Error: Enter a number in the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue

                    # Perimeter
                    if(select_formula == 1):
                        while True:
                            try:
                                side_1 = float(input("Enter the first side: "))
                                side_2 = float(input("Enter the second side: "))
                                side_3 = float(input("Enter the third side: "))
                                side_4 = float(input("Enter the fourth side: "))
                                if( side_1 < 0 or side_2 < 0 or side_3 < 0 or side_4 < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        perimeter = side_1 + side_2 + side_3 + side_4
                        result = perimeter
                        print(f"Your answer is: {result}")
                        print("Answer Printed.")
                            
                    # Area
                    elif(select_formula == 2):
                        while True:
                            try:
                                height = float(input("Enter the height: "))
                                length_1 = float(input("Enter the length of the bottom parallel side: "))
                                length_2 = float(input("Enter the length of the top parallel side: "))
                                if(height < 0 or length_1 < 0 or length_2 < 0):
                                    print("Error: A measurement of a shape cant be less than zero")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        area = (length_1 + length_2)/2 * height
                        print(f"Your answer is: {area}")
                        print("Answer Printed.")
                    # Volume
                    elif(select_formula == 3):
                        while True:
                            try:
                                height = float(input("Enter the height: "))
                                length_1 = float(input("Enter the length of the bottom parallel side: "))
                                length_2 = float(input("Enter the length of the top parallel side: "))
                                length_prism = float(input("Enter the length of the prism: "))
                                if(height < 0 or length_1 < 0 or length_2 < 0 or length_prism < 0):
                                    print("Error: A measurement of a shape cant be less than zero")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        area = (length_1 + length_2)/2 * height
                        volume = area * length_prism
                        print(f"Your answer is: {volume}")
                        print("Answer Printed.")
                    #Surface Area
                    elif(select_formula == 4):
                        while True:
                            try:
                                height = float(input("Enter the height: "))
                                length_1 = float(input("Enter the length of the bottom parallel side: "))
                                length_2 = float(input("Enter the length of the top parallel side: "))
                                length_prism = float(input("Enter the length of the prism: "))
                                side_1 = float(input("Enter the first side: "))
                                side_2 = float(input("Enter the second side: "))
                                side_3 = float(input("Enter the third side: "))
                                side_4 = float(input("Enter the fourth side: "))
                                if( side_1 < 0 or side_2 < 0 or side_3 < 0 or side_4 < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                if(height < 0 or length_1 < 0 or length_2 < 0 or length_prism < 0):
                                    print("Error: A measurement of a shape cant be less than zero")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        perimeter = side_1 + side_2 + side_3 + side_4
                        area = (length_1 + length_2)/2 * height
                        sa = 2 * area + perimeter * length_prism
                        print(f"Your answer is: {sa}")
                        print("Answer Printed.")
                        
                    
                    
                #-------------------------------- 
                # Code for Rhombus
                #-------------------------------- 
                elif(calc_selection_3 == 9):
                    while True:
                        try: 
                            print(f"1.Perimeter\n2.Area\n.3 Volume\n4. Surface Area")
                            select_formula = int(input("Enter the number by what to want to do: "))
                            if(select_formula < 1 or select_formula > 4):
                                print("Error: Enter a number in the range")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    # Perimeter
                    if(select_formula == 1):
                        while True:
                            try:
                                side_1 = float(input("Enter the first side: "))
                                side_2 = float(input("Enter the second side: "))
                                side_3 = float(input("Enter the third side: "))
                                side_4 = float(input("Enter the fourth side: "))
                                if( side_1 < 0 or side_2 < 0 or side_3 < 0 or side_4 < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        perimeter = side_1 + side_2 + side_3 + side_4
                        result = perimeter
                        print(f"Your answer is: {result}")
                        print("Answer Printed.")
                            
                    # Area
                    elif(select_formula == 2):
                        while True:
                            try:
                                width = float(input("Enter the width of the object: "))
                                length = float(input("Enter the length of the object: "))
                                if(width < 0 or length < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        result = width * length

                        print(f"Your ansswer is: {result}")
                        print("Answer Printed.")
                    # Volume
                    elif(select_formula == 3):
                        while True:
                            try:
                                width = float(input("Enter the width of the object: "))
                                length = float(input("Enter the length of the object: "))
                                height = float(input("Enter the height: "))
                                if(width < 0 or length < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        result = width * length * height

                        print(f"Your ansswer is: {result}")
                        print("Answer Printed.")
                    #Surface Area
                    elif(select_formula == 4):
                        while True:
                            try:
                                width = float(input("Enter the width of the object: "))
                                length = float(input("Enter the length of the object: "))
                                height = float(input("Enter the height: "))
                                side_1 = float(input("Enter the first side: "))
                                side_2 = float(input("Enter the second side: "))
                                side_3 = float(input("Enter the third side: "))
                                side_4 = float(input("Enter the fourth side: "))
                                if( side_1 < 0 or side_2 < 0 or side_3 < 0 or side_4 < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                if(width < 0 or length < 0):
                                    print("Error: A side can not be less than 0")
                                    continue
                                break
                            except:
                                print("Error: Enter a number")
                                continue
                        area = width * length 
                        perimeter = side_1 + side_2 + side_3 + side_4
                        sa = 2 * area + perimeter * height

                        print(f"Your ansswer is: {sa}")
                        print("Answer Printed.")
                    
                    
                #-------------------------------- 
                # Code for Distance Formula
                #-------------------------------- 
                elif(calc_selection_3 == 10):
                    while True:
                        try:
                            x1 = float(input("Enter the first x-coordinate: "))
                            y1 = float(input("Enter the first y-coordinate: "))
                            x2 = float(input("Enter the second x-coordinate: "))
                            y2 = float(input("Enter the second y-coordinate: "))
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    distance = math.sqrt((x2 - x1)^2 + (y2-y1)^2)
                    
                    print(f"Your ansswer is: {distance}")
                    print("Answer Printed.")
                        
                        
                    

                
                
                
                #-------------------------------- 
                # Code for Midpoint Formula
                #-------------------------------- 
                elif(calc_selection_3 == 11):
                    while True:
                        try:
                            x1 = float(input("Enter the first x-coordinate: "))
                            y1 = float(input("Enter the first y-coordinate: "))
                            x2 = float(input("Enter the second x-coordinate: "))
                            y2 = float(input("Enter the second y-coordinate: "))
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    x = (x1 + x2)/2
                    y = (y1 + y2)/2
                    
                    print(f"Your answer is:({x},{y})")
                    print("Answer Printed.")
                    
                    
                    
                #-------------------------------- 
                # Code for Slope Formula
                #-------------------------------- 
                elif(calc_selection_3 == 12):
                    while True:
                        try:
                            x1 = float(input("Enter the first x-coordinate: "))
                            y1 = float(input("Enter the first y-coordinate: "))
                            x2 = float(input("Enter the second x-coordinate: "))
                            y2 = float(input("Enter the second y-coordinate: "))
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    slope = (y2 - y1) / (x2 - x1)
                    
                    print(f"Your ansswer is: {slope}")
                    print("Answer Printed.")
                    
                    
                #-------------------------------- 
                # Code for Pythagerom Therom
                #-------------------------------- 
                elif(calc_selection_3 == 13):
                    while True:
                        try:
                            a = float(input("Enter the value of a: "))
                            b = float(input("Enter the value of b: "))
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                        
                    c_squared = a ** 2 + b ** 2
                    c = math.sqrt(c_sqaured)
                    
                    print(f"Your ansswer is: {c}")
                    print("Answer Printed.")
                            
                    
                    
                    
                #----------------------------------------------------------------
                # Code for Interior Angle of a Polygon Formula
                #----------------------------------------------------------------
                elif(calc_selection_3 == 14):
                    while True:
                        try:
                            n = int(input("Enter the number of side of your polygon: "))
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    angle = ((n - 2) * 180) / n
                    
                    print(f"Your ansswer is: {angle}")
                    print("Answer Printed.")
                    
                    
                #----------------------------------------------------------------
                # Code for Interior Angle Sum of a Polygon Formula
                #----------------------------------------------------------------
                elif(calc_selection_3 == 15):
                    while True:
                        try:
                            n = int(input("Enter the number of side of your polygon: "))
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    angle_sum = (n - 2) * 180
                    
                    print(f"Your ansswer is: {angle_sum}")
                    print("Answer Printed.")
                    
                    
                #----------------------------------------------------------------
                # Code for Herons Formula
                #----------------------------------------------------------------
                elif(calc_selection_3 == 16):
                    while True:
                        try:
                            side_1 = float(input("Enter the first side: "))
                            side_2 = float(input("Enter the second side: "))
                            side_3 = float(input("Enter the third side: "))
                            if(side_1 < 0 or side_2 < 0 or side_3 < 0):
                                print("Error: Sides cant be less than 0")
                                continue
                            break
                        except:
                            print("Error: Enter a number")
                            continue
                    semi_perimeter = (side_1 + side_2 + side_3)/2
                    area = math.sqrt(semi_perimeter(semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3))
                    
                    
                    print(f"Your ansswer is: {area}")
                    print("Answer Printed.")
                    

                    
            
    
                        
                        
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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