import math

def equationSolver(stringParam):

    inputString = str(stringParam)
    print("InputString: " + inputString)
    splitted_equation = inputString.split(" ")
    print("SplittedString: " + str(splitted_equation))

    a = float(splitted_equation[0])
    operator = splitted_equation[2]
    b = float(splitted_equation[3])

    try:
        if operator == "+":

    else:
        try:
            result = math.sqrt(b/a)
