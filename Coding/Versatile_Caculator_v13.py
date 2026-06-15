global answer_1
global answer_2
global answer_3
global answer_4
global answer_5
global answer_6   

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
    "Degree to Radian",
    "Radian to Degree",
    "Vector Dot Product"
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
            if(answer_1 <= 0 or answer_1 > 8):
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


    # 1. Get the primary section selection first
    section_choice = section_selection()

    # Initialize your selection variables to None safely
    calc_selection = None
    calc_selection_2 = None
    calc_selection_3 = None

    # 2. ONLY call the menu that the user actually chose
    if section_choice == 1:
        calc_selection = basic_math_selection()
    elif section_choice == 2:
        calc_selection_2 = advanced_math_selection()
    elif section_choice == 3:
        calc_selection_3 = geomertery_operation_formula_selection()
    #
    # Basic Math Calculations
    #
    # Calculation for Addition
    if(calc_selection == 1):
        while True:
            try: 
                count = int(input(f"How many numbers are you adding with: "))
            except:
                print("Error: Enter a number")
                continue
            numbers_list = []
            for i in range(count):
                
                num = float(input(f"Enter number {i + 1}(you will enter your first number then it will ask you what you next number is and etc.): "))
                
                numbers_list.append(num)
            total = sum(numbers_list)
            print(f"Your answer is: {total:.10f}")
            return numbers_list
            
    # Calcualtion for subtraction
    if(calc_selection == 2):
        while True:
            try:
                count = int(input(f"How many numbers are you subtracting with: "))
            except:
                print("Error: Enter a number")
                continue
            numbers_list = []
            for i in range(count):
                
                num = float(input(f"Enter number {i + 1}(the order of the numbers will change the answer ex:10-6 =4, 6-10 = -4): "))
                
                numbers_list.append(num)
            total = numbers_list[0]
            for num in numbers_list[1:]:
                total = total - num
            print(f"Your answer is: {total:.10f}")
            return total
            
    # Calcualtion for multiplication
    if(calc_selection == 3):
        while True:
            try:
                count = int(input(f"How many numbers are you multiplying with: "))
            except:
                print("Error: Enter a number")
                continue
            numbers_list = []
            for i in range(count):
                
                num = float(input(f"Enter number {i + 1}: "))
                
                
                numbers_list.append(num)
            total = 1
            for num in numbers_list:
                previous_total = total
                total = total * num
                print(f"{previous_total} * {num} = {total:.3f}")
            print(f"Your answer is: {total:.3f}")
            return total
            
    # Calcualtion for division
    if(calc_selection == 4):
        while True:
            try:
                count = int(input(f"How many numbers are you dividing with: "))
            except:
                print("Error: Enter a number")
                continue
            numbers_list = []
            
            for i in range(count):
            
                num = float(input(f"Enter number {i + 1} (the number you want to divide needs to be the first number): "))
                
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
            return total 
    # Calculation for Absolute Value
    if(calc_selection == 5):
        while True:
            try:
                num = float(input(f"Enter the number you need to do absolute value on: "))
            except:
                print("Error: Enter a number")
                continue
                
            result = abs(num)
            print(f"Your answer is: {result}")

        


    #
    # Advanced Math Calculations
    #
    # Calculation for Factorial
    if(calc_selection_2 == 1):
        while True:
            try:
                number = int(input("Enter the number you want to find the factorial of(NO NEGAITIVES, and NO ZERO): "))
                if(number <= 0 ):
                    print("Errot: Enter a number greater than zero")
            except:
                print("Error: Enter a number")
                continue

            import math
            result = math.factorial(number)
            print(f"Your answer is: {result}")
    # Calculation for Roots
    if(calc_selection_2 == 2):
        while True:
            try:
                root = int(input("Enter your root(just enter the number ex: square root would be 2,a nd cube root would be 3, and etc., Highest root is 10): "))
                if(root < 2 or root > 10):
                    print("Error:Enter numebr greater or equal to 2 and a number less than or equal to 10")
                    continue
            except:
                print("Error: You have to enter a number")
                continue
            
            number = float(input("Enter your number/base: "))
            import math
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
            break
                
            

        
    #Calculations for Power of Exponent
    if(calc_selection_2 == 3):
        while True:
            try:
                base = float(input("Enter what your base is(enter fractions as decimals): "))
            except:
                print("Error: Enter a number or decimal")
                continue
            while True:
                try:
                    power = float(input("Enter what you want your base to be to the power of(no fractions): "))
                except:
                    print("Error: Enter a number or decimal")
                    continue 
                

                result = pow(base,power)

                print(f"Your answer is: {result}")
                return
        
    # Calculation for Fraction to Decimal
    if(calc_selection_2 == 4):
        while True:
            try:
                numerator = int(input(f"Enter your numerator here(no decimals): "))
            except:
                print("Error: Enter a number")
                continue
            while True:
                try:
                    denominator = int(input(f"Enter your denominator here(no decimals): "))
                except: 
                    print("Error: Enter a number")
                    continue

                total = numerator/denominator
                
                print(f"Your answer is: {total:.10f}")
                return total
    # Calculation for Deciaml to Fraction
    if(calc_selection_2 == 5):
        while True:

            from fractions import Fraction
            try:
                decimal_float = float(input("Enter here the decimal you want to turn into a fraction: "))
            except:
                print("Error: Enter a number or decimal")
                continue
        

            fraction = Fraction(decimal_float).limit_denominator()

            print(f"Your answer is: {fraction}")
            break
    #
    #Geomertery Operations
    #
    #Calculation for Cosine operations
    if(geometry_selection == 1 and calc_selection_3 == 1 ):
        import math
        while True:
            try:
                print("What are you solving for")
                print(f"1. Find Side Length\n2. Find Angle\n3. Find cosine of a number")
                angle_or_side = int(input(f"Enter 1 or 2 or 3 for what you need: "))
                if(angle_or_side < 1 or angle_or_side > 3):
                    print("Error: Enter a number within the range")
                    continue
            except:
                print("Error: Enter a number")
                continue
        
            if(angle_or_side == 1 ):
                print("What side are you solving for")
                print(f"1. Adjacent\n2. Hypotenuse")
                while True:
                    try:
                        adjacent_or_hypotenuse = int(input(f"Enter 1 or 2 for what you need: "))
                        if(adjacent_or_hypotenuse < 1 or adjacent_or_hypotenuse > 2):
                            print("Error: Enter a number within the range")
                            continue
                    except:
                        print("Error: Enter a number")
                        continue
                    while True:
                        try:
                            angle_deg = float(input("Enter the angle in degrees: "))
                        except:
                            print("Error: Enter a number")
                            continue
                        
                        angle_rad = math.radians(angle_deg)
                        
                        
                        
                        
                        if(adjacent_or_hypotenuse == 1):
                                while True:
                                    try:
                                        hyp = float(input("Enter the length of the hypotenuse: "))
                                    except:
                                        print("Error: Enter a number")
                                        continue
                                    
                                    adj = hyp * math.cos(angle_rad)
                                
                                    result = adj
                                    print(f"Your answer is: {result}")
                                    break
                        elif(adjacent_or_hypotenuse == 2):
                                while True:
                                    try:
                                        adj = float(input("Enter the length of the adjacent side: "))
                                    except:
                                        print("Error: Enter a number")
                                        continue
                                    
                                    hyp = adj / math.cos(angle_rad)
                                    result = hyp
                                    print(f"Your answer is: {result}")
                                    break
                        break
                    break
            elif (angle_or_side == 2):
                while True:
                    try:
                        adj = float(input("Enter the adjacent side or the top number: "))
                        hyp = float(input("Enter the hypotenuse or the bottom number: "))
                        if adj > hyp:
                            print("Error: The adjacent side cannot be larger than the hypotenuse")
                            continue
                    except:
                        print("Error:Enter a number")
                        continue
                    angle_rad = math.acos(adj/hyp)
                    angle_deg = math.degrees(angle_rad)
                    result = angle_deg
                    print(f"Your answer is(in degress): {result}")
                    result = angle_rad
                    print(f"Your asnwer is(in radians): {result}")
                    break
            elif(angle_or_side == 3):
                while True:
                    try:
                        print(f"1. Cosine\n2. Inverse of cosine")
                        inverse_or_normal = int(input("Enter 1 or 2 : "))
                        if(inverse_or_normal < 1 or inverse_or_normal > 2):
                            print("Error: Enter a number within the range")
                            continue
                    except:
                        print("Error: Enter a number")
                        continue
                    if(inverse_or_normal == 1):
                        while True:
                            try:
                                number = float(input("Enter the number you wanna find the cosine of: "))
                            except:
                                print("Error:Enter a number")
                                continue
                            cosine = math.cos(number)
                            print(f"Your answer is(in radians): {cosine}")
                            cosine = math.degrees(cosine)
                            print(f"Your answer is(in degrees): {cosine}")
                            break
                    if(inverse_or_normal == 2):
                        while True:
                            try:
                                number = float(input("Enter the number you wanna find the inverse of cosine of(number has to be less than one and cannot be negative ): "))
                                if(number > 1 or number < 0):
                                    print("Error: Enter a number less than 1 or a number that is not negative")
                                    continue
                            except:
                                print("Error:Enter a number")
                                continue
                            acosine = math.acos(number)
                            print(f"Your answer is(in radians): {acosine}")
                            acosine = math.degrees(acosine)
                            print(f"Your answer is(in degrees): {acosine}")
                            break
                    break
            break
        

    #Calculation for Sine operations
    if(geometry_selection == 1 and calc_selection_3 == 2 ):
            import math
            while True:
                try:
                    print("What are you solving for")
                    print(f"1. Find Side Length\n2. Find Angle\n3. Find sine of a number")
                    angle_or_side = int(input(f"Enter 1 or 2 or 3 for what you need: "))
                    if(angle_or_side < 1 or angle_or_side > 3):
                        print("Error: Enter a number within the range")
                        continue
                except:
                    print("Error: Enter a number")
                    continue
            
                if(angle_or_side == 1 ):
                    print("What side are you solving for")
                    print(f"1. Opposite\n2. Hypotenuse")
                    while True:
                        try:
                            opposite_or_hypotenuse = int(input(f"Enter 1 or 2 for what you need: "))
                            if(opposite_or_hypotenuse < 1 or opposite_or_hypotenuse > 2):
                                print("Error: Enter a number within the range")
                                continue
                        except:
                            print("Error: Enter a number")
                            continue
                        while True:
                            try:
                                angle_deg = float(input("Enter the angle in degrees: "))
                            except:
                                print("Error: Enter a number")
                                continue
                            
                            angle_rad = math.radians(angle_deg)
                            
                            
                            
                            
                            if(opposite_or_hypotenuse == 1):
                                    while True:
                                        try:
                                            hyp = float(input("Enter the length of the hypotenuse: "))
                                        except:
                                            print("Error: Enter a number")
                                            continue
                                        
                                        opp = hyp * math.cos(angle_rad)
                                    
                                        result = opp
                                        print(f"Your answer is: {result}")
                                        break
                            elif(opposite_or_hypotenuse == 2):
                                    while True:
                                        try:
                                            opp = float(input("Enter the length of the opposite side: "))
                                        except:
                                            print("Error: Enter a number")
                                            continue
                                        
                                        hyp = opp / math.sin(angle_rad)
                                        result = hyp
                                        print(f"Your answer is: {result}")
                                        break
                            break
                        break
                elif (angle_or_side == 2):
                    while True:
                        try:
                            opp = float(input("Enter the opposite side or the top number: "))
                            hyp = float(input("Enter the hypotenuse or the bottom number: "))
                            if opp > hyp:
                                print("Error: The opposite side cannot be larger than the hypotenuse")
                                continue
                        except:
                            print("Error:Enter a number")
                            continue
                        angle_rad = math.asin(opp/hyp)
                        angle_deg = math.degrees(angle_rad)
                        result = angle_deg
                        print(f"Your answer is(in degrees): {result}")
                        result = angle_rad
                        print(f"Your answer is(in radians): {result}")
                        break
                elif(angle_or_side == 3):
                    while True:
                        try:
                            print(f"1. Sine\n2. Inverse of sine")
                            inverse_or_normal = int(input("Enter 1 or 2: "))
                            if(inverse_or_normal < 1 or inverse_or_normal > 2):
                                print("Error: Enter a number within the range")
                                continue
                        except:
                            print("Error: Enter a number")
                            continue
                        if(inverse_or_normal == 1):
                            while True:
                                try:
                                    number = float(input("Enter the number you wanna find the sine of: "))
                                except:
                                    print("Error:Enter a number")
                                    continue
                                sine = math.sin(number)
                                print(f"Your answer is(in radians): {sine}")
                                sine = math.degrees(sine)
                                print(f"Your answer is(in degrees): {sine}")
                                break
                        if(inverse_or_normal == 2):
                            while True:
                                try:
                                    number = float(input("Enter the number you wanna find the inverse of sine of(number has to be less than adn cannot be negative): "))
                                    if(number > 1 or number < 0):
                                        print("Error: Enter a number that is less than one or not negative")
                                        continue
                                except:
                                    print("Error:Enter a number")
                                    continue
                                asine = math.asin(number)
                                print(f"Your answer is(in radians): {asine}")
                                asine = math.degrees(asine)
                                print(f"Your answer is(in degrees): {asine}")
                                break
                        break
                    break
    # Calculation for Tangent
    if(geometry_selection == 1 and calc_selection_3 == 3 ):
                import math
                while True:
                    try:
                        print("What are you solving for")
                        print(f"1. Find Side Length\n2. Find Angle\n3. Find tangent of a number")
                        angle_or_side = int(input(f"Enter 1 or 2 or 3 for what you need: "))
                        if(angle_or_side < 1 or angle_or_side > 3):
                            print("Error: Enter a number within the range")
                            continue
                    except:
                        print("Error: Enter a number")
                        continue
                
                    if(angle_or_side == 1 ):
                        print("What side are you solving for")
                        print(f"1. Opposite\n2. Adjacent")
                        while True:
                            try:
                                opposite_or_adjacent = int(input(f"Enter 1 or 2 for what you need: "))
                                if(opposite_or_adjacent < 1 or opposite_or_adjacent > 2):
                                    print("Error: Enter a number within the range")
                                    continue
                            except:
                                print("Error: Enter a number")
                                continue
                            while True:
                                try:
                                    angle_deg = float(input("Enter the angle in degrees: "))
                                except:
                                    print("Error: Enter a number")
                                    continue
                                
                                angle_rad = math.radians(angle_deg)
                                
                                
                                
                                
                                if(opposite_or_adjacent == 1):
                                        while True:
                                            try:
                                                adj = float(input("Enter the length of the adjacent side: "))
                                            except:
                                                print("Error: Enter a number")
                                                continue
                                            
                                            opp = adj * math.tan(angle_rad)
                                        
                                            result = opp
                                            print(f"Your answer is: {result}")
                                            break
                                elif(opposite_or_adjacent == 2):
                                        while True:
                                            try:
                                                opp = float(input("Enter the length of the opposite side: "))
                                            except:
                                                print("Error: Enter a number")
                                                continue
                                            
                                            adj = opp / math.tan(angle_rad)
                                            result = adj
                                            print(f"Your answer is: {result}")
                                            break
                                break
                            break
                    elif (angle_or_side == 2):
                        while True:
                            try:
                                opp = float(input("Enter the opposite side or the top number: "))
                                adj = float(input("Enter the adjacent side or the bottom number: "))
                            except:
                                print("Error:Enter a number")
                                continue
                            angle_rad = math.atan(opp/adj)
                            angle_deg = math.degrees(angle_rad)
                            result = angle_deg
                            print(f"Your answer is(in degrees): {result}")
                            result = angle_rad
                            print(f"Your answer is(in radians): {result}")
                            break
                    elif(angle_or_side == 3):
                        while True:
                            try:
                                print(f"1. Tangent\n2. Inverse of tangent")
                                inverse_or_normal = int(input("Enter 1 or 2: "))
                                if(inverse_or_normal < 1 or inverse_or_normal > 2):
                                    print("Error: Enter a number within the range")
                                    continue
                            except:
                                print("Error: Enter a number")
                                continue
                            if(inverse_or_normal == 1):
                                while True:
                                    try:
                                        number = float(input("Enter the number you wanna find the tangent of: "))
                                    except:
                                        print("Error:Enter a number")
                                        continue
                                    tan = math.tan(number)
                                    print(f"Your answer is(in radians): {tan}")
                                    tan = math.degrees(tan)
                                    print(f"Your answer is(in degrees): {tan}")
                                    break
                            if(inverse_or_normal == 2):
                                while True:
                                    try:
                                        number = float(input("Enter the number you wanna find the inverse of tangent of: "))
                                    except:
                                        print("Error:Enter a number")
                                        continue
                                    atan = math.atan(number)
                                    print(f"Your answer is(in radians): {atan}")
                                    atan = math.degrees(atan)
                                    print(f"Your answer is(in degrees): {atan}")
                                    break
                            break
                        break
    if(geometry_selection == 1 and calc_selection_3 == 4):
        import math
        while True:
            try:
                x1 = float(input("Enter the first x: "))
                y1 = float(input("Enter the first y: "))
                x2 = float(input("Enter the second x: "))
                y2 = float(input("Enter the second y: "))
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
            break


            
                             
                   
                        
                        
                        
                        
                        
        

        
        
        
        
                     
                            
                        
                
            
            
       
        

















    #
    #Geometery Formulas
    #















def main():
    commit_calculations()
        

main()