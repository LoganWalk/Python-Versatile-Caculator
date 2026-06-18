a = int(input("Enter: "))
b = int(input("Enter: "))
c = int(input("Enter: "))
answers = []
positive_answer = []
negative_answer = []
imaginary_answer = []
import cmath

while True:

        equation_1 = (b * -1 + cmath.sqrt(b**2 - 4*a*c))/2 * a
        if equation_1.imag == 0:
            number = float(equation_1.real)
            if(number < 0):
                negative_answer.append(number)
                answers.append(number)
            elif( number > 0):
                positive_answer.append(number)
                answers.append(number)
        else:
            imaginary_answer.append(equation_1)
            answers.append(equation_1)
            
        equation_2 = (b * -1 - cmath.sqrt(b**2 - 4*a*c))/2 * a
        if equation_2.imag == 0:
            number = float(equation_2.real)
            
            
            if(number < 0):
                negative_answer.append(number)
                answers.append(number)
            elif( number > 0):
                positive_answer.append(number)
                answers.append(number)
        else:
            imaginary_answer.append(equation_2)
            answers.append(equation_2)

            
        break
equation_a = str(a) + "x" + "^" + "2"
equation_b = str(b) + "x"
equation_c = str(c)



print("j------>i")
print(f"Equation: {equation_a} + {equation_b} + {equation_c}")
print(f"Negative Answers: {negative_answer}")
print(f"Positive Answers: {positive_answer}")
print(f"Imgainary Answers: {imaginary_answer}")
print(f"{equation_a} + {equation_b} + {equation_c} = {answers}")
print("Answer Printed.")

