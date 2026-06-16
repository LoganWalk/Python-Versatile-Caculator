def main():
    while True:
        try:
            print("When typing your equation you must have a space bewteen operators and numbers like this x^2 + x + 5")
            dividend = input("Enter the dividend equation(for squares input it as x^2): ")
            divisor = input("Enter the divisor equation(for squares input it as x^2): ")
            break
        except:
            print("Error: Enter a number")
            continue
    split_dividend = dividend.split(" ")
    split_divisor = divisor.split(" ")
        
    print(split_dividend)
    print(split_divisor)
main()