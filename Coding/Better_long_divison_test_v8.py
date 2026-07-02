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
dividend_list = []
new_copy_dict_list = []
new_copy_list = []
list_of_div = []
zero_check = 0 
import re

dividend_input = input("Enter your dividend (e.g., 3x^4-5): ")
divisor_input = input("Enter your divisor (e.g., x-2): ")

# Remove any spaces the user typed to start with a clean string
div_clean = dividend_input.replace(" ", "")
dis_clean = divisor_input.replace(" ", "")

# Regex pattern captures: numbers (\d+), words/variables ([a-zA-Z]+), or symbols ([+-^])
token_pattern = r'\d+|[a-zA-Z]+|[+-^]'

dividend_split = re.findall(token_pattern, div_clean)
divisor_split = re.findall(token_pattern, dis_clean)

print("Dividend fully split:", dividend_split)
print("Divisor fully split:", divisor_split)

from fractions import Fraction 

#-------------------------------------------------------------- 
# Gather and store coeff's and exp's of dividend 
#-------------------------------------------------------------- 
for i in range(len(dividend_split)): 
    if 'x' in dividend_split[i]: 
        if i == 0:
            coeff = 1
            coeff_list.append(coeff) 
        elif '-' == dividend_split[i - 1]: 
            coeff = -1
            coeff_list.append(coeff)
        elif '+' == dividend_split[i-1]:
            coeff = 1
            coeff_list.append(coeff)
        elif dividend_split[i-1].isdigit():
            if '-' == dividend_split[i - 2]:
                coeff = -1 * int(dividend_split[i - 1]) 
                coeff_list.append(coeff) 
            elif '-' != dividend_split[i-2]: 
                coeff = int(dividend_split[i-1]) 
                coeff_list.append(coeff) 
            
            
        if '^' == dividend_split[i+1]: 
            exp = int(dividend_split[i + 2]) 
            exp_list.append(exp)
        else:
            exp_list.append(1)

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
    i = 1
    while i < len(exp_list):
        zero_exp = exp_list[i - 1] - exp_list[i]
        if zero_exp > 1:
            # Calculate the exact missing exponent value safely
            missing_exponent = exp_list[i - 1] - 1
            exp_list.insert(i, missing_exponent)
            coeff_list.insert(i, 0)
        else:
            i += 1

#-------------------------------------------------------------- 
# Gather and store coeff's and exp's of divisor
#-------------------------------------------------------------- 
for i in range(len(divisor_split)): 
    if 'x' in divisor_split[i]: 
        if i == 0:
            coeff_2 = 1
            coeff_list_2.append(coeff_2) 
        elif '-' == divisor_split[i - 1]: 
            coeff_2 = -1
            coeff_list_2.append(coeff_2) 
        elif '+' == divisor_split[i-1]:
            coeff_2 = 1
            coeff_list_2.append(coeff_2)
        elif divisor_split[i-1].isdigit():
            if '-' == divisor_split[i - 2]:
                coeff_2 = -1 * int(divisor_split[i - 1]) 
                coeff_list_2.append(coeff_2) 
            elif '-' != divisor_split[i-2]: 
                coeff_2 = int(divisor_split[i-1]) 
                coeff_list_2.append(coeff_2) 
            
            
        if '^' == divisor_split[i+1]: 
            exp_2 = int(divisor_split[i + 2]) 
            exp_list_2.append(exp_2)
        else:
            exp_list_2.append(1)

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
    i = 1
    while i < len(exp_list_2):
        zero_exp_2 = exp_list_2[i - 1] - exp_list_2[i]
        if zero_exp_2 > 1:
            # Calculate the exact missing exponent value safely
            missing_exponent_2 = exp_list_2[i - 1] - 1
            exp_list_2.insert(i, missing_exponent_2)
            coeff_list_2.insert(i, 0)
        else:
            i += 1

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
    answer_key = ans_exp
    answer_value = ans_val
    
    for key, value in divisor_dict.items(): 
        new_exponent = key + answer_key 
        new_copy[new_exponent] = value * answer_value 
    new_copy_dict_list.append(new_copy)
    
        
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

for key in list(answer_dict.keys()):
    if answer_dict[key] == 0:
        del answer_dict[key]
for key in list(divisor_dict.keys()):
    if divisor_dict[key] == 0:
        del divisor_dict[key]
# --- SORTED DATA BUILDING ---
for key,value in sorted(answer_dict.items(), reverse=True): 
    if key > 0: 
        answer_list.append(f"{value}x^{key}") 
    elif(key == 0): 
        answer_list.append(f"{value}") 

# FIXED: Ensure checks run smoothly even if dictionary values contain negative fractions
if final_remainder_dict: 
    for key,value in sorted(final_remainder_dict.items(), reverse=True): 
        if key > 0: 
            remainder_list.append(f"{value}x^{key}") 
        elif(key == 0): 
            remainder_list.append(f"{value}") 

for key,value in sorted(divisor_dict.items(), reverse=True): 
    if key > 0: 
        divisor_list.append(f"{value}x^{key}") 
    elif(key == 0): 
        divisor_list.append(f"{value}") 

for key,value in sorted(dividend_dict.items(), reverse=True): 
    if key > 0: 
        dividend_list.append(f"{value}x^{key}") 
    elif(key == 0): 
        dividend_list.append(f"{value}") 

def clean(text):
    import re
    # 1. Fix spacing for negative numbers
    text = text.replace(" + -", " - ")
    # 2. Strip exponent 1 cleanly (e.g., x^1 -> x)
    text = text.replace("x^1", "x")
    # 3. Strip leading 1 from 1x or 1x^ only if it's not part of another number (like 371)
    text = re.sub(r'\b1x', 'x', text)
    text = text.replace("(1x", "(x")
    return text


final_answer_join = clean(" + ".join(answer_list))
dividend_join = clean(" + ".join(dividend_list))
div_join = clean(" + ".join(divisor_list))
spacer = " " * len(div_join)

if remainder_list:
    rem_join = clean(" + ".join(remainder_list))
    print(f"{spacer}   {final_answer_join} + ({rem_join})/({div_join})")
else:
    print(f"{spacer}   {final_answer_join}")

print(f"{spacer}   _{'_' * len(dividend_join)}")
print(f"{div_join} | {dividend_join}")

# Tracks dynamic padding changes per long division tier
current_padding = 0

for i in range(len(div_list)):
    new_copy_list = []
    for key, value in sorted(new_copy_dict_list[i].items(), reverse=True):
        if value != 0:
            new_copy_list.append(f"{value}x^{key}" if key > 0 else f"{value}")
    new_copy_list_join = clean(" + ".join(new_copy_list))
    
    list_of_div = []
    for key, value in sorted(div_list[i].items(), reverse=True):
        if value != 0:
            list_of_div.append(f"{value}x^{key}" if key > 0 else f"{value}")
    div_list_join = clean(" + ".join(list_of_div))
    if not list_of_div:
        div_list_join = "0"
        
    # Matches terminal text directly below the terms of the dividend
    step_indent = " " * current_padding
    print(f"{spacer}   {step_indent}-({new_copy_list_join})")
    print(f"{spacer}   {step_indent} {'-' * len(new_copy_list_join)}")
    
    # Calculate exactly where the next line should start based on leading characters dropped
    if i < len(div_list) - 1:
        next_copy_list = []
        for key, value in sorted(new_copy_dict_list[i+1].items(), reverse=True):
            if value != 0:
                next_copy_list.append(f"{value}x^{key}" if key > 0 else f"{value}")
        next_copy_join = clean(" + ".join(next_copy_list))
        
        # Shift padding right to perfectly capture the size change between operations
        current_padding += (len(new_copy_list_join) - len(next_copy_join))
        
    print(f"{spacer}   {step_indent}  {div_list_join}")









    
    





    
            
            
            

            
        