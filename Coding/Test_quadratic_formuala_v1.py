a = int(input("Enter: "))
b = int(input("Enter: "))
c = int(input("Enter: "))
answers = []
import math
while True:
    try:

        equation_1 = (b * -1 + math.sqrt(b**2 - 4*a*c))/2 * a
        equation_2 = (b * -1 - math.sqrt(b**2 - 4*a*c))/2 * a
        answers.append(equation_1)
        answers.append(equation_2)
        break
    except:
        equation_1 = (b * -1 + math.sqrt(-1*(b**2 - 4*a*c)))/2 * a
        equation_2 = (b * -1 - math.sqrt(-1*(b**2 - 4*a*c)))/2 * a
        answers.append(equation_1)
        answers.append(equation_2)
        break

print(answers)

