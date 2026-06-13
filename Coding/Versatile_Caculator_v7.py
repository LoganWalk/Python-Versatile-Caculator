answer_1 = None
answer_2 = None
answer_3 = None
answer_4 = None
answer_5 = None
answer_6 = None
calc_selection_2 = None
section_choice = None
selection = None
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
    "Formulas",
    "Operations"
]
GEOMETERY_OPERATIONS = [
    "Cosine",
    "Tangent",
    "Sine",
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
                if(answer_1 <= 0 or answer_1 > 8):
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
            return answer_4
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
    #
    # Basic Math Calculations
    #
   section_selection()
   calc_selection = basic_math_selection()
   calc_selection_2 = advanced_math_selection()


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


















    #
    #Geometery Formulas
    #















def main():
    commit_calculations()
        

main()