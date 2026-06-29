dividend_dict = {} 
divisor_dict = {} 
answer_dict = {} 
r_ans_dict = {} 
final_remainder_dict = {} 
coeff_list = [] 
coeff_list_2 = [] 
exp_list = [] 
exp_list_2 = [] 
div_list = [] 
answer_list = [] 
remainder_list = [] 
divisor_list = [] 
zero_check = 0 
dividend = "1 x ^ 4 - 5 x ^ 2 + 1 x ^ 1 + 10" 
divisor = "2 x ^ 2 + 3 x ^ 1 - 7" 
dividend_split = dividend.split(" ") 
divisor_split = divisor.split(" ") 

from fractions import Fraction 

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
                for _ in range(zero_exp - 1): 
                    target_index = i-1 
                    exp_list.insert(target_index, zero_exp + 1) 
                    coeff_list.insert(target_index,0) 

#-------------------------------------------------------------- 
# Gather and store coeff's and exp's of divisor
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
                for _ in range(zero_exp_2 - 1): 
                    target_index_2 = i-1 
                    exp_list_2.insert(target_index_2, zero_exp_2 + 1) 
                    coeff_list_2.insert(target_index_2,0) 

#------------------------------------------------------------------ 
# Add the keys and values to the dict's of dividend and divisor 
#------------------------------------------------------------------ 
for idx in range(len(exp_list)): 
    dividend_dict[exp_list[idx]] = Fraction(coeff_list[idx]) 
for idx in range(len(exp_list_2)): 
    divisor_dict[exp_list_2[idx]] = Fraction(coeff_list_2[idx]) 

difference = ((len(dividend_dict) - len(divisor_dict)) -1) * -1 
leading_exp_2 = max(divisor_dict.keys()) 

#------------------------------------------------------------ 
# Math and logic for long divison 
#------------------------------------------------------------ 
import copy 
e = 0 
while True: 
    if(e == 0): 
        new_div = copy.deepcopy(dividend_dict) 
    elif(e > 0): 
        new_div = copy.deepcopy(div_list[e-1]) 
        
    zero_keys = [k for k, v in new_div.items() if v == 0] 
    for k in zero_keys: 
        del new_div[k] 
        
    if not new_div: 
        zero_check = 1 
        break 
        
    leading_exp = max(new_div.keys()) 
    leading_coeff = new_div[leading_exp] 
    leading_coeff_2 = divisor_dict[leading_exp_2] 
    
    if leading_exp < leading_exp_2: 
        r_ans_dict |= new_div 
        break 
        
    ans_val = Fraction(leading_coeff, leading_coeff_2) 
    ans_exp = leading_exp - leading_exp_2 
    answer_dict[ans_exp] = ans_val 
    
    new_copy = {} 
    answer_key = list(answer_dict)[e] 
    answer_value = list(answer_dict.values())[e] 
    
    for key, value in divisor_dict.items(): 
        new_exponent = key + answer_key 
        new_copy[new_exponent] = value * answer_value 
        
    for key,value in new_copy.items(): 
        if key in new_div: 
            new_div[key] = new_div[key] - value 
        else: 
            new_div[key] = 0 - value 
            
    # FIXED: Broken structural index deletion loops removed from here
            
    div_list.append(new_div) 
    e+=1 

if r_ans_dict: 
    for exp, coeff in r_ans_dict.items(): 
        if exp in final_remainder_dict: 
            final_remainder_dict[exp] += coeff 
        else: 
            final_remainder_dict[exp] = coeff 
    final_remainder_dict = {k: v for k, v in final_remainder_dict.items() if v != 0} 
elif zero_check == 1: 
    final_remainder_dict = None 

for key,value in answer_dict.items(): 
    answer_dict[key] = value 
if final_remainder_dict is not None: 
    for key,value in final_remainder_dict.items(): 
        final_remainder_dict[key] = value 

for key,value in answer_dict.items(): 
    if key > 0: 
        coeff_x_exp = f"{value}x^{key}" 
        answer_list.append(coeff_x_exp) 
    elif(key == 0): 
        coeff_x_exp =f"{value}" 
        answer_list.append(coeff_x_exp) 

if(final_remainder_dict): 
    for key,value in final_remainder_dict.items(): 
        if key > 0: 
            coeff_x_exp = f"{value}x^{key}" 
            remainder_list.append(coeff_x_exp) 
        elif(key == 0): 
            coeff_x_exp =f"{value}" 
            remainder_list.append(coeff_x_exp) 

for key,value in divisor_dict.items(): 
    if key > 0: 
        coeff_x_exp = f"{value}x^{key}" 
        divisor_list.append(coeff_x_exp) 
    elif(key == 0): 
        coeff_x_exp =f"{value}" 
        divisor_list.append(coeff_x_exp) 

final_answer_join = " + ".join(answer_list) 
if remainder_list: 
    rem_join = " + ".join(remainder_list) 
    div_join = " + ".join(divisor_list) 
    final_answer = f"{final_answer_join} + {rem_join} / {div_join}" 
else: 
    final_answer = final_answer_join 
    
    
    
# 1. Clean up consecutive signs (+ - becomes - )
final_answer = final_answer.replace(" + -", " - ")

# 2. Clean up redundant coefficients (1x^2 becomes x^2)
final_answer = final_answer.replace(" 1x^", " x^")
final_answer = final_answer.replace("(1x^", "(x^")

# 3. Clean up linear terms (x^1 becomes x)
final_answer = final_answer.replace("x^1", "x")

# 4. Clean up spacing bugs around minus signs if necessary
final_answer = final_answer.replace(" - ", " - ")



print(final_answer)



    
            
            
            

            
        