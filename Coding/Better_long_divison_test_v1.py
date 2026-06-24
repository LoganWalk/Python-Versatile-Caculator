dividend_dict = {}
divisor_dict = {}
coeff_list = []
coeff_list_2 = []
exp_list = []
exp_list_2 = []

dividend = input("Enter your dividend here: ")
divisor = input("Enter your divisor here: ")

dividend_split = dividend.split(" ")
divisor_split = divisor.split(" ")


#--------------------------------------------------------------
# Gather and store coeff's and exp's of dividend and divisor
#--------------------------------------------------------------
for i in range(len(dividend_split)):
    
    if 'x' in dividend_split[i]:
        
        if '-' in dividend_split[i - 2]:
            coeff = -1 * int(dividend_split[i - 1])
            coeff_list.append(coeff)
        elif '-' not in dividend_split[i-2]:
            coeff = int(dividend_split[i-1])
            coeff_list.append(coeff)
        
        
        
        if '^' in dividend_split[i+2]:
            exp = int(dividend_split[i + 2])
            exp_list.append(exp)
            
        if 'x' not in dividend_split[-1]:
            last_number = int(dividend_split[-1])
            second_to_last_number = dividend_split[-2]
            if '-' not in second_to_last_number:
                coeff_list.append(last_number)
            elif '-' in second_to_last_number:
                last_number = last_number * -1
                coeff_list.append(last_number)
    for i in range(len(dividend_split)):
        dividend_dict[coeff_list[i]] = exp_list[i]
        
        
for i in range(len(divisor_split)):
    
    if 'x' in divisor_split[i]:
        
        if '-' in divisor_split[i - 2]:
            coeff_2 = -1 * int(divisor_split[i - 1])
            coeff_list_2.append(coeff_2)
        elif '-' not in divisor_split[i-2]:
            coeff_2 = int(divisor_split[i-1])
            coeff_list_2.append(coeff_2)
        
        
        if '^' in divisor_split[i+2]:
            exp_2 = int(divisor_split[i + 2])
            exp_list_2.append(exp_2)
        
        if 'x' not in divisor_split[-1]:
            last_number = int(divisor_split[-1])
            second_to_last_number = divisor_split[-2]
            if '-' not in second_to_last_number:
                coeff_list_2.append(last_number)
            elif '-' in second_to_last_number:
                last_number = last_number * -1
                coeff_list_2.append(last_number)
    for i in range(len(divisor_split)):
            divisor_dict[coeff_list_2[i]] = exp_list_2[i]
            
            
            

            
        