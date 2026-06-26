dividend_dict = {}
divisor_dict = {}
answer_dict = {}
coeff_list = []
coeff_list_2 = []
exp_list = []
exp_list_2 = []
div_list = []

dividend = "1 x ^ 4 - 5 x ^ 2 + 1 x ^ 1 + 10"
divisor = "2 x ^ 2 + 3 x ^ 1 - 7"

dividend_split = dividend.split(" ")
divisor_split = divisor.split(" ")


#--------------------------------------------------------------
# Gather and store coeff's and exp's of dividend 
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
            








        
#--------------------------------------------------------------
# Gather and store coeff's and exp's of dividend 
#--------------------------------------------------------------      
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
            




#------------------------------------------------------------------
# Add the keys and values to the dict's of dividend and divisor
#------------------------------------------------------------------
for idx in range(len(exp_list)):
    dividend_dict[exp_list[idx]] = coeff_list[idx]
for idx in range(len(exp_list_2)):
    divisor_dict[exp_list_2[idx]] = coeff_list_2[idx]


difference = ((len(dividend_dict) - len(divisor_dict)) -1) * -1
leading_coeff = next(iter(dividend_dict.values()))
leading_coeff_2 = next(iter(divisor_dict.values()))

for key,value in dividend_dict.items():
    if value == leading_coeff:
        leading_exp = key
for key,value in divisor_dict.items():
    if value == leading_coeff_2:
        leading_exp_2 = key


import copy
e = 0
while True:
    answer_dict[leading_exp-leading_exp_2] = leading_coeff/leading_coeff_2
    new_copy = enumerate(copy.deepcopy(divisor_dict))
    key = enumerate(new_copy.keys())
    value = enumerate(new_copy.values())
    answer_key = enumerate(answer_dict.keys())
    answer_values = enumerate(answer_dict.values())
    for i in range(len(new_copy)):
        new_copy[i] = [key[i] + answer_key[e]]
        new_copy[i] = value[i] * answer_values[e]
    
    
    if(e == 0):
        new_div = enumerate(copy.deepcopy(dividend_dict))
    elif( e > 0):
        new_div = enumerate(copy.deepcopy(div_list[e]))

    for i in range(len(new_copy)):
        new_div_values = enumerate(new_div.values())
        new_div[i] = new_div_values[i] - new_copy[i]
    for i in range(difference* -1):
        if i * -1 == difference:
            for i in range(difference * -1, start = 1):
                del new_div[i*-1]
            for key,value in (new_div.items()):
                if (i == 0):
                    if(value == 0):
                        del new_div[0]

    div_list.append(new_div)



    



    

    















    e+=1







print(dividend_dict)
print(divisor_dict)



    
            
            
            

            
        