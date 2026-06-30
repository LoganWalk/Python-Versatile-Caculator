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
final_answer_list = []
zero_check = 0 
dividend = input("Enter your dividend: ") 
divisor = input("Enter your divisor: ")
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
# Gather and store the coeff of the divisor
#-------------------------------------------------------------- 
for i in range(len(divisor_split)):
    if '-' in divisor_split[-2] or '+' in divisor_split[-2]: 
        divisor_coeff = int(divisor_split[-1]) * -1
        
#------------------------------------------------------------------ 
# Do the math and logic for synthetic divison 
#------------------------------------------------------------------ 
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
answer_list.append(coeff_list[0])
for i in range(len(coeff_list)-1):
    multiplied = coeff_list[i] * divisor_coeff
    addition = multiplied + coeff_list[i+1]
    answer_list.append(addition)
    
for idx,val in enumerate(answer_list):
    answer_dict[exp_list[idx]-1] = val

divisor_2 = f"x + {divisor_coeff * -1}"
divisor_cleaned = clean(divisor_2)
    
for key, value in sorted(answer_dict.items(), reverse = True):
    if key > 0: 
        final_answer_list.append(f"{value}x^{key}") 
    elif(key == 0): 
        final_answer_list.append(f"{value}")
    elif(key < 0):
        final_answer_list.append(f"({value})/({divisor_cleaned})")
        

ans_join = clean(" + ".join(final_answer_list))


    



print(coeff_list)
print(divisor_coeff)
print(ans_join)
