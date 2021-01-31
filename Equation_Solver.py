'''
This script reads an console input string as mathematical equation and tries to solve it. The equation should be fixed to
the power of two.
'''
import math

def equationSolver(stringParam):

    inputString = str(stringParam)
    print("InputString: " + inputString)

    # Split the equation string at every blank symbol and output it
    splitted_equation = inputString.split(" ")
    print("SplittedString: " + str(splitted_equation))

    # Save the coefficients and the mathematical operator, which shall either be a sum or a subtraction
    a = float(splitted_equation[0])
    operator = splitted_equation[2]
    b = float(splitted_equation[3])

    try:
        if operator == "+":
            result = math.sqrt(-b/a)
        else:
            result = math.sqrt(b/a)

        print(inputString + " solved for x equals: " + str(result))
    except:
        print("Error")


equationSolver(str(input()))