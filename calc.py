#!/usr/bin/python3
# A program which calculates the add, sub, mul and div of two numbers
# Usage: ./pro_calc.py <operation> <num1> <num2>

import sys
import operator

def calcula(operacion, num1, num2):

    operaciones = {'add': operator.add, 'sub': operator.sub, 'div': operator.truediv, 'mul': operator.mul}
    try:
        print(operaciones[operacion](num1,num2))
    except ZeroDivisionError:
        print("You can't divide by zero!")

if __name__ == "__main__":

    if len(sys.argv) == 4:
        operacion = sys.argv[1]
        try:
            num1 = float(sys.argv[2])
            num2 = float(sys.argv[3])
        except ValueError:
            print("You only can operate with numbers!")
            sys.exit()
        try:
            calcula(operacion, num1, num2)
        except KeyError:
            print("Be careful with the arguments!\nUsage: ./pro_calc.py <operation> <num1> <num2>")
    else:
        print("Error. Usage: ./pro_calc.py <operation> <num1> <num2>")
