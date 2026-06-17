a = int(input("Enter: "))
b = int(input("Enter: "))
c = int(input("Enter: "))
answers = []
import cmath
while True:

        equation_1 = (b * -1 + cmath.sqrt(b**2 - 4*a*c))/2 * a
        equation_2 = (b * -1 - cmath.sqrt(b**2 - 4*a*c))/2 * a
        answers.append(equation_1)
        answers.append(equation_2)
            
        break

print(answers)
print("j------>i")

