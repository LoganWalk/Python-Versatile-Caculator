answer_1 = None
answer_2 = None
answer_3 = None
calc_selection_2 = None
section_choice = None
SECTIONS = [
    "Basic Math", 
    "Advanced Math", 
    "Geometry", 
    "Algebra 1", 
    "Trigonometry", 
    "Calculus", 
    "Algebra 2"
]

BASIC_MATH_OPTIONS = [
    "Addition", 
    "Subtraction", 
    "Multiplication", 
    "Division", 
    "Absolute Value"
    
]
ADVANCED_MATH_OPTIONS = [
    "Factoiral",
    "Square Root",
    "Power of Exponents",
    "Fraction to Decimal",
    "Decimal to Fraction"
]



def section_selection():
    print("What section are you looking for?")
    for index, section in enumerate(SECTIONS, start=1):
        print(f"{index}. {section}")
        
    
    answer_1 = int(input("Enter the number next to the section you need: "))
    return answer_1


def calculation_selection():
    section_choice = section_selection()
    if(section_choice == 1):
        print("What calculation do you need to do?")
        
        
        for index, calc in enumerate(BASIC_MATH_OPTIONS, start=1):
            print(f"{index}. {calc}")
            
        answer_2 = int(input("Enter the number by what calculation you need to do: "))
        return answer_2
    if(section_choice == 2):
        print("What calculation do you need to do?")
        
        
        for index, calc in enumerate(ADVANCED_MATH_OPTIONS, start=6):
            print(f"{index}. {calc}")
            
        answer_2 = int(input("Enter the number by what calculation you need to do: "))

        return answer_2
        
    
def commit_calculations():
    #
    # Basic Math Calculations
    #
   calc_selection = calculation_selection()
   # Calculation for Addition
   if(calc_selection == 1):
        count = int(input(f"How many numbers are you adding with: "))
        numbers_list = []
        for i in range(count):
                
            num = float(input(f"Enter number {i + 1}(you will enter your first number then it will ask you what you next number is and etc.): "))
                
                
            numbers_list.append(num)
        total = sum(numbers_list)
        print(f"Your answer is: {total:.10f}")
        return numbers_list
            
    # Calcualtion for subtraction
   if(calc_selection == 2):
        count = int(input(f"How many numbers are you subtracting with: "))
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
        count = int(input(f"How many numbers are you multiplying with: "))
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
        count = int(input(f"How many numbers are you dividing with: "))
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
       num = float(input(f"Enter the number you need to do absolute value on: "))
       result = abs(num)
       print(f"Your answer is: {result}")

        
  
   
    #
    # Advanced Math Calculations
    #
    # Calculation for Factorial
   if(calc_selection == 6):
        number = int(input("Enter the number you want to find the factorial of(NO NEGAiTIVES): "))
        import math
        result = math.factorial(number)
        print(f"Your answer is: {result:.2f}")
    # Calculation for Roots
   if(calc_selection == 7):
        root = int(input("Enter your root(just enter the number ex: square root would be 2,a nd cube root would be 3, and etc., Highest root is 5): "))
        number = float(input("Enter your number/base: "))
        import math
        square_root = math.sqrt(number)
        cube_root = math.cbrt(number)
        fourth_root = math.sqrt(math.sqrt(number))
        fifth_root = math.cbrt(math.sqrt(number))
        if(root == 2):
            print(f"Your answer is: {square_root:.5f}")
        if(root == 3):
            print(f"Your answer is: {cube_root:.5f}")
        if(root == 4):
            print(f"Your answer is: {fourth_root:.5f}")
        if(root == 5):
            print(f"Your answer is: {fifth_root:.5f}")
    #Calculations for Power of Exponent
   if(calc_selection == 9):
       base = float(input("Enter what your base is(enter fractions as decimals): "))
       power = float(input("Enter what you want your base to be to the power of(no fractions): "))

       result = base ** power

       print(f"Your answer is: {result}")
    # Calculation for Fraction to Decimal
   if(calc_selection == 10):
        numerator = int(input(f"Enter your numerator here(no decimals): "))
        denominator = int(input(f"Enter your denominator here(no decimals): "))
                
        total = numerator/denominator
                
        print(f"Your answer is: {total:.10f}")
        return total
    # Calculation for Deciaml to Fraction
   if(calc_selection == 11):
        from fractions import Fraction

        decimal_float = input("Enter here the decimal you want to turn into a fraction: ")

        fraction = Fraction(decimal_float).limit_denominator()

        print(f"Your answer is: {fraction}")















def main():
    commit_calculations()
        

main()