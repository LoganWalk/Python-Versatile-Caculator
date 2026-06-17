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
    
    x_values = []
    coefficents = []
    divison = []
    search_word = "x"
    start_index = 0
    while True:
        
        x_index = dividend.find(search_word, start_index)
        if x_index == -1:
            break
        
        x_char = dividend[x_index + 4] 
        co_char = dividend[x_index - 2]
        
        
        x_value = int(x_char)
        co_value = int(co_char)
        
        coefficents.append(co_value)
        x_values.append(x_value)
        if(len(x_values) == 1):
            co = dividend[x_index + 4]
        
        # FIX: Both values are now integers, so subtraction works perfectly
        if len(x_values) > 1:
            if x_values[0] - x_values[1] == 2:
                coefficents.insert(1, 0)
                coefficents.append(co)
                
        start_index = x_index + 1
                

    
    
    print(coefficents)
    print(divison)
    
main()