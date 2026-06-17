def main():
    while True:
        try:
            print(f"When typing your equation all variables that dont and do need to be written like this x ^ 1, x ^ 2, and etc\n----------------------------------")
            print(f"All operators and numbers/variables need to have a space bewteen them\n----------------------------------")
            print(f"All variables need to have some number in front of them with a space bewteen them, if you have a variable that is just x write as 1x\n----------------------------------")
            print(f"Here is how your equation should be typed: 2 x ^ 2 + 1 x ^ 1 + 5 \n----------------------------------")
            dividend = input("Enter the dividend equation(for squares input it as x ^ 2): ")
            divisor = input("Enter the divisor equation(for squares input it as x ^ 2): ")
            break
        except:
            print("Error: Enter a number")
            continue
    
    raw_x_values = []
    raw_coefficients = []
    divison = []
    search_word = "x"
    start_index = 0
    x = 0
    y = 0
    # Gets the coefficents and stores them in a list
    coeff_list = []
    tokens = dividend.split(" ")
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if 'x' in token:
            
            coeff = int(tokens[i-1])
            coeff_list.append(coeff)
        

        

        i += 1
    if 'x' not in tokens[-1]:
            last_number = int(tokens[-1])
            coeff_list.append(last_number)
    print(coeff_list)

    # Gets the powers of the variables and stores them in a list
    
    
main()