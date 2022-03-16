import numpy as np
import sympy as sy
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor


np.set_printoptions(precision=20)

def gradient_descent(fx, x, eta, tmax, goal, mingrad):
    grad = gradient(fx)
    for i in range(tmax):
        diff = - eta * evaluate_gradient(grad, x)

        if(np.all(np.abs(diff)) <= goal):
            break

        x = x + diff
        print(x)
    return x

def f(function_to_transform):
    transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))
    return parse_expr(function_to_transform, transformations = transformations)

def gradient(function):
    variables = list(function.free_symbols)
    gradientF = np.array([])
    if(variables[0] == sy.symbols('x')):
        for i in range(len(variables)):
            gradientF = np.append(gradientF, [sy.diff(function,variables[i])])
        return gradientF
    else:
        for i in range(len(variables), 0, -1):
            gradientF = np.append(gradientF, [sy.diff(function,variables[i-1])])
        return gradientF

def evaluate_gradient(gradient, values):
    gradient_evaluated = np.array([])
    for i in range(len(gradient)):
        symbols = gradient[i].free_symbols
        dictSymbols = dict(zip(symbols, values))
        print(dictSymbols)
        gradient_evaluated = np.append(gradient_evaluated, [gradient[i].subs(dictSymbols)])
    
    print(gradient_evaluated)
    
    input()
    return gradient_evaluated

fx = f("(x+2y-7)^2 + (2x+y-5)^2")

x = gradient_descent(fx, np.array([0,0]), 0.1, 1000, 10e-8, 10e-10)

print(x)
