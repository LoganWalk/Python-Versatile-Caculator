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
        
        
        
        if '^' in dividend_split[i+1]:
            exp = int(dividend_split[i + 2])
            exp_list.append(exp)

if 'x' not in dividend_split[-1]:
    last_number = int(dividend_split[-1])
    second_to_last_number = dividend_split[-2]
    if '-' not in second_to_last_number:
        coeff_list.append(last_number)
        exp_list.append(0)
    elif '-' in second_to_last_number:
        last_number = last_number * -1
        coeff_list.append(last_number)
        exp_list.append(0)

if(len(exp_list) > 1):
    for i in range(len(exp_list)):
        if(i > 0):
            zero_exp = exp_list[i - 1] - exp_list[i]
            if(zero_exp > 1):
                i += 1
                for _  in range(zero_exp - 1):
                    target_index =  i-1
                    exp_list.insert(target_index, zero_exp + 1)
                    coeff_list.insert(target_index,0)
            








        
        
for i in range(len(divisor_split)):
    
    if 'x' in divisor_split[i]:
        if '-' in divisor_split[i - 2]:
            coeff_2 = -1 * int(divisor_split[i - 1])
            coeff_list_2.append(coeff_2)
        elif '-' not in divisor_split[i-2]:
            coeff_2 = int(divisor_split[i-1])
            coeff_list_2.append(coeff_2)
        
        
        if '^' in divisor_split[i+1]:
            exp_2 = int(divisor_split[i + 2])
            exp_list_2.append(exp_2)
if 'x' not in divisor_split[-1]:
    last_number = int(divisor_split[-1])
    second_to_last_number = divisor_split[-2]
    if '-' not in second_to_last_number:
        coeff_list_2.append(last_number)
        exp_list_2.append(0)
    elif '-' in second_to_last_number:
        last_number = last_number * -1
        coeff_list_2.append(last_number)
        exp_list_2.append(0)

if(len(exp_list_2) > 1):
    for i in range(len(exp_list_2)):
        if(i > 0):
            zero_exp_2 = exp_list_2[i - 1] - exp_list_2[i]
            if(zero_exp_2 > 1):
                i += 1
                for _  in range(zero_exp_2 - 1):
                    target_index_2 =  i-1
                    exp_list_2.insert(target_index_2, zero_exp_2 + 1)
                    coeff_list_2.insert(target_index_2,0)
            



# Fill missing placeholders (e.g., x^3) safely


for idx in range(len(exp_list)):
    dividend_dict[exp_list[idx]] = coeff_list[idx]
for idx in range(len(exp_list_2)):
    divisor_dict[exp_list_2[idx]] = coeff_list_2[idx]



print(dividend_dict)
print(divisor_dict)



    
            
            
            

            
        