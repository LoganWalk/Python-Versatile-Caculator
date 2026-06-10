answer_1 = None
answer_2 = None
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
    "Fraction to Decimal", 
    "Decimal to Fraction"
]



def main():
    
    commit_calculations()






def section_selection():
    print("What section are you looking for?")
    for index, section in enumerate(SECTIONS, start=1):
        print(f"{index}. {section}")
        
    # Convert input to int since menu options are whole numbers
    answer_1 = int(input("Enter the number next to the section you need: "))
    return answer_1


def calculation_selection():
    section_choice = section_selection()
    if(section_choice == 1):
        print("What calculation do you need to do?")
        
        # Loop through the basic math array
        for index, calc in enumerate(BASIC_MATH_OPTIONS, start=1):
            print(f"{index}. {calc}")
            
        answer_2 = int(input("Enter the number by what calculation you need to do: "))
        return answer_2
    
def commit_calculations():
    # Calcualtion for addition
    calc_selection = calculation_selection()
    if(calc_selection == 1):
        count = int(input(f"How many numbers are you adding with: "))
        numbers_list = []
        for i in range(count):
        # Ask for the number (i + 1 makes the prompt say 1, 2, 3 instead of 0, 1, 2)
            num = float(input(f"Enter number {i + 1}(you will enter your first number then it will ask you what you next number is and etc.): "))
        
        # 4. Add the number to your list
            numbers_list.append(num)
        total = sum(numbers_list)
        print(f"Your answer is: {total:.10f}")
        return numbers_list
    
    # Calcualtion for subtraction
    if(calc_selection == 2):
        count = int(input(f"How many numbers are you subtracting with: "))
        numbers_list = []
        for i in range(count):
        # Ask for the number (i + 1 makes the prompt say 1, 2, 3 instead of 0, 1, 2)
            num = float(input(f"Enter number {i + 1}(the order of the numbers will change the answer ex:10-6 =4, 6-10 = -4): "))
        
        # 4. Add the number to your list
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
        # Ask for the number (i + 1 makes the prompt say 1, 2, 3 instead of 0, 1, 2)
            num = float(input(f"Enter number {i + 1}: "))
        
        # 4. Add the number to your list
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
        # Ask for the number
            num = float(input(f"Enter number {i + 1} (the number you want to divide needs to be the first number): "))
        # FIXED: Indented this line so it adds EVERY number to the list, not just the last one
            numbers_list.append(num)

    # 1. Start with the first number in the array (index 0)
        total = numbers_list[0]

    # 2. Loop through the remaining numbers (from index 1 to the end)
        for num in numbers_list[1:]:
        # Safety Check: Prevent the program from crashing if dividing by zero
            if num == 0:
                print("Error: Cannot divide by zero!")
                return None # FIXED: This now ONLY runs if num is actually 0
            
            previous_total = total
            total = total / num

        
            print(f"{previous_total} / {num} = {total:.3f}")
        print(f"Your answer is: {total:.3f}")
        return total 


    if(calc_selection == 5):
        numerator = int(input(f"Enter your numerator here(no decimals): "))
        denominator = int(input(f"Enter your denominator here(no decimals): "))
        
        total = numerator/denominator
        
        print(f"Your answer is: {total:.10f}")
        return total
    if(calc_selection == 6):
        from fractions import Fraction

        decimal_float = input("Enter here the decimal you want to turn into a fraction: ")

        # limit_denominator() cleans up float precision errors
        fraction = Fraction(decimal_float).limit_denominator()

        print(f"Your answer is: {fraction}")

    
        
    




    
       



































main()
