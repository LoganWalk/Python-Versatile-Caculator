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
    
    coeff_list = []
    coeff_list_2 = []
    exp_list= []
    exp_list_2 = []
    tokens = dividend.split(" ")
    tokens_2 = divisor.split(" ")
    answer_list_coeff = []
    answer_list_exp = []
    answer_coeff = []
    answer_exp = []
    multiplied_divisor_coeff = []
    multiplied_divisor_exp = []
    subtraction_coeff_list = []
    subtraction_exp_list = []
    coeff_left_list_dividend = []
    exp_left_list_dividend = []
    coeff_left_list_subtracted = []
    exp_left_list_subtracted = []
    differnence_in_size = len(tokens) - len(tokens_2)
    subtracted_left_list = []

    
    # Store the dividend
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if 'x' in token:
        
            coeff = int(tokens[i-1])
            symbol = (tokens[i-2])
            if '-' not in symbol:                   
                coeff_list.append(coeff)
            elif '-' in symbol:
                coeff = coeff * -1                     
                coeff_list.append(coeff)
        if(i + 1 < len(tokens)):
            operator = (tokens[i + 1])
        # Gets the powers of the variables and stores them in a list
        if '^' in operator:
            exp = int(tokens[i + 2])
            exp_list.append(exp)
        
        i += 1
        
    
    # Finds the gaps and puts zero and adds the last numebr to coeff list
    e = 0
    if 'x' not in tokens[-1] :
        if 'x' not in tokens[-1]:
            last_number = int(tokens[-1])
            second_to_last_number = tokens[-2]
            if '-' not in second_to_last_number:
                coeff_list.append(last_number)
            elif '-' in second_to_last_number:
                last_number = last_number * -1
                coeff_list.append(last_number)
    if len(exp_list) > 1:
        for e in range(len(exp_list)):
            fill_in = exp_list[e-1] - exp_list[e]
            e += 1
            if(fill_in > 1):
                for _ in range(fill_in - 1):
                    coeff_list.insert(e-1,0)
                    exp_list.insert(e-1,fill_in)
                    
    # Store the divisor
    i = 0
    while i < len(tokens_2):
        token_2 = tokens_2[i]
        
        if 'x' in token_2:
        
            coeff = int(tokens_2[i-1])
            symbol = (tokens_2[i-2])
            if '-' not in symbol:                   
                coeff_list_2.append(coeff)
            elif '-' in symbol:
                coeff = coeff * -1                     
                coeff_list_2.append(coeff)
        if(i + 1 < len(tokens_2)):
            operator = (tokens_2[i + 1])
        # Gets the powers of the variables and stores them in a list
        if '^' in operator:
            exp = int(tokens_2[i + 2])
            exp_list_2.append(exp)
        
        i += 1
        
    
    # Finds the gaps and puts zero and adds the last numebr to coeff list
    e = 0
    if 'x' not in tokens_2[-1] :
        if 'x' not in tokens_2[-1]:
            last_number = int(tokens_2[-1])
            second_to_last_number = tokens_2[-2]
            if '-' not in second_to_last_number:
                coeff_list_2.append(last_number)
            elif '-' in second_to_last_number:
                last_number = last_number * -1
                coeff_list_2.append(last_number)
    if len(exp_list_2) > 1:
        for e in range(len(exp_list_2)):
            fill_in = exp_list_2[e-1] - exp_list_2[e]
            e += 1
            if(fill_in > 1):
                for _ in range(fill_in - 1):
                    coeff_list_2.insert(e-1,0)
                    exp_list_2.insert(e-1,fill_in)
    
                    
                    
                    
    # Find the first value of the answer
    answer_coeff = coeff_list[0] / coeff_list_2[0]
    answer_list_coeff.append(answer_coeff)
    answer_exp = exp_list[0] / exp_list_2[0]
    answer_list_exp.append(answer_exp)

    # multiply the second coeff by the answer coeff
    
    for i in range(len(coeff_list_2)):
        multiplied_coeff = coeff_list_2[i] * answer_coeff
        multiplied_divisor_coeff.append(multiplied_coeff)
        i += 1
    
    for i in range(len(exp_list_2)):
        multiplied_exp = exp_list_2[i] * answer_exp
        multiplied_divisor_exp.append(multiplied_exp)
        i += 1

    # subtraction time

    for i in range(len(multiplied_divisor_coeff)):
        subtraction_coeff = coeff_list[i] - multiplied_divisor_coeff[i]
        subtraction_coeff_list.append(subtraction_coeff)
        i += 1

    coeffs_left = len(coeff_list) - i
    for i in range(len(multiplied_divisor_exp)):
        subtraction_exp = exp_list[i] - multiplied_divisor_exp[i]
        subtraction_exp_list.append(subtraction_exp)
        i += 1
    exp_left = len(exp_list) - i 
    i = 0
    for i in range(len(subtraction_coeff_list)):
        if(subtraction_coeff_list[0] == 0):
            subtraction_coeff_list.remove(0)
    for i in range(len(subtraction_exp_list)):
        if(subtraction_exp_list[0] == 0):
            subtraction_exp_list.remove(0)


    # find the exp and coeff values of what is left
    i = 0
    for i in range(coeffs_left):
        dividend_left = -1 * (coeffs_left - i )
        value_dividend = coeff_list[dividend_left]
        coeff_left_list_dividend.append(value_dividend)
    i = 0
    for i in range(exp_left):
        try:
            dividend_left = -1 * (exp_left - i ) + 1
            if(dividend_left == 0):
                break
            value_dividend = exp_list[dividend_left]
            exp_left_list_dividend.append(value_dividend)
        except:
            break
    i = 0
    for i in range(coeffs_left):
        value_subtracted = subtraction_coeff_list[i]
        coeff_left_list_subtracted.append(value_subtracted)
    i = 0
    for i in range(exp_left):
        try:
            value_subtracted = subtraction_exp_list[i]
            exp_left_list_subtracted.append(value_subtracted)
        except:
            break

        
    i = 0
    for i in range(len(coeff_left_list_dividend)):
        if(len(exp_left_list_dividend) > i and len(exp_left_list_subtracted) > i ):
            if(exp_left_list_dividend[i] == exp_left_list_subtracted[i]):
                try:
                    subtraction_coeff_list[i] = coeff_left_list_dividend[i] + coeff_left_list_subtracted[i]
                except:
                    break
            elif(exp_left_list_dividend[i] != exp_left_list_subtracted[i]):
                if(exp_left_list_dividend[i] > exp_left_list_subtracted[i]):
                    subtraction_coeff_list.insert(i,coeff_left_list_dividend)
                elif(exp_left_list_dividend[i] < exp_left_list_subtracted[i]):
                    subtraction_coeff_list.insert(i+1,coeff_left_list_dividend)


    

    

        


    print("Dividend")
    print(coeff_list)
    print(exp_list)
    print("")
    print("Divisor")
    print(coeff_list_2)
    print(exp_list_2)
    print("")
    print("First term of answer")
    print(answer_list_coeff)
    print(answer_list_exp)
    print("")
    print("Multiplied values")
    print(multiplied_divisor_coeff)
    print(multiplied_divisor_exp)
    print("")
    print("Subtracted values")
    print(subtraction_coeff_list)
    print(subtraction_exp_list)
    print("")
    print("Values of exp and coeffs left for dividend")
    print(coeff_left_list_dividend)
    print(exp_left_list_dividend)
    print("")
    print("Values of exp and ceoffs left for subtracted value")
    print(coeff_left_list_subtracted)
    print(exp_left_list_subtracted)
    print("")
    print("Combined like coeffs")
    print(subtraction_coeff_list)


    
    

    
    

    



    
    
main()
        
    