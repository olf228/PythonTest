'''
This script reads an console input string as mathematical equation and tries to solve it. The equation should be fixed to
the power of two.
'''
import math

def equationSolver(stringParam):

    # Split the equation string at every blank symbol
    splitted_equation = stringParam.split(" ")

    # Save the coefficients and the mathematical operator, which shall either be a sum or a subtraction
    a = float(splitted_equation[0])
    operator = splitted_equation[2]
    b = float(splitted_equation[3])

    # Try to solve the equation. If there is an error there needs to be an exception handling
    try:
        if operator == "+":
            result = math.sqrt(-b/a)
        elif operator == "-":
            result = math.sqrt(b/a)
        else:
            # If the operator is neither plus or minus there should be thrown the same exception as ZeroDivision
            raise ZeroDivisionError
        print("Solution: " + str(result))

    except ValueError:
        # There is no real solution of the equations with real numbers, but with imaginary numbers
        print("no real solution")

    except ZeroDivisionError:
        # if there are infinite solutions
        if a == 0.0 and b == 0.0:
           print("all real numbers are solutions")

        # if there is no solution or the mathematical operator is neither plus nor minus
        else:
            print("no solution")

# Start the script
equationSolver(str(input()))

# eof
