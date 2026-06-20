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
    answer_list = []

    
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