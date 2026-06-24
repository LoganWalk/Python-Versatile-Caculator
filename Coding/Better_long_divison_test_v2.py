dividend_dict = {}
divisor_dict = {}
coeff_list = []
coeff_list_2 = []
exp_list = []
exp_list_2 = []

dividend = "1 x ^ 4 - 5 x ^ 2 + 1 x ^ 1 + 10"
divisor = "2 x ^ 2 + 3 x ^ 1 - 7"

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
    i = 0
    while i < len(coeff_list):
        try:
            if(i < len(exp_list)):
                coeff_value = coeff_list[i]
                exp_value = exp_list[i]
                dividend_dict[coeff_value] = exp_value
        except:
            coeff_value = coeff_list[i]
            exp_value = 0
            dividend_dict[coeff_value] = exp_value
        i += 1
            
        


    print(dividend_dict)
    for i in range(len(dividend_dict)):
        if(exp_list > 1):
            for i in range(len(exp_list)):
                if(i > 0):
                    zero_exp = dividend_dict.get[i-1] - dividend_dict.get[i]
                    if(zero_exp > 1):
                        for _ in range(zero_exp-1):
                            target_index = i - 1
                            dividend_list = list(dividend_dict.items())
                            dividend_list.insert(target_index,(0,dividend_dict.get[i-1]-1))
                            updated_list = dict(dividend_list)
                        dividend_dict.update(updated_list)

        
        
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
    i = 0
    while i < len(coeff_list_2):
        try:
            if(i < len(exp_list_2)):
                coeff_value_2 = coeff_list_2[i]
                exp_value_2 = exp_list_2[i]
                divisor_dict[coeff_value_2] = exp_value_2
        except:
            coeff_value_2 = coeff_list_2[i]
            exp_value_2 = 0
            divisor_dict[coeff_value_2] = exp_value_2
        i += 1
        
    print(divisor_dict)
    for i in range(len(divisor_dict)):
        if(exp_list_2 > 1):
            for i in range(len(exp_list_2)):
                if(i > 0):
                    zero_exp_2 = divisor_dict.get[i-1] - divisor_dict.get[i]
                    if(zero_exp_2 > 1):
                        for _ in range(zero_exp_2-1):
                            target_index_2 = i - 1
                            divisor_list = list(divisor_dict.items())
                            divisor_list.insert(target_index_2,(0,divisor_dict.get[i-1]-1))
                            updated_list_2 = dict(divisor_list)
                        divisor_dict.update(updated_list_2)



    print(dividend_dict)
    print(divisor_dict)



    
            
            
            

            
        