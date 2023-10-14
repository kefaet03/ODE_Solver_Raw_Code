import sympy
import sys

x = sympy.symbols('x')                     #variable define
y = sympy.Function('y')(x)                 #corrected

degree = int(input("Enter the order of your ODE: "))             

# Initialize an array to store the coefficients
coefficients = []

for i in range(degree, -1, -1):                                             #coeffeicient taking loop
    if i == 0:
        coeff = input("Enter the f(x) co-efficient of constant : ")
    elif i == 1:
        coeff = input("Enter the f(x) co-efficient of 1st derivative : ")
    else:
        coeff = input(f"Enter the f(x) co-efficient of {i}th derivative : ")
    coefficients.append(sympy.sympify(coeff))

lhs = sum(coeff*y.diff(x, i) for i, coeff in enumerate(reversed(coefficients)))                 #left hand side of equation

rhs_input = input("Enter the right-hand side of the equation: ") 
rhs = sympy.sympify(rhs_input)                                                                  #right hand side of equation          

eq = sympy.Eq(lhs, rhs)                                  # Construct the differential equation

print ("The ODE: ")
sympy.pprint(eq)

print('\n')

gen_soln=sympy.dsolve(eq)   #changed
print("The general solution is: ")
sympy.pprint(gen_soln)

print('\n')

initial_conditions = {}  # Initialize an empty dictionary for initial conditions

val=input("Do you want to have initial condition solution? (Y/n) : ")
if val=='Y':
    i=0
    for i in range(degree):
        while True:
            try:
                x_val=float(input(f"The value of x(for {i}the derivative) : "))
                y_val=float(input(f'Initial condition for y({i})({x_val}) : ')) 
                initial_conditions[y.diff(x,i).subs(x, x_val)] = y_val   #corrected
                break
            except ZeroDivisionError:
                print("A divided by Zero erro ditected")
            except ValueError:
                print("Invalid input")    
else:
    sys.exit()

part_soln=sympy.dsolve(eq,y,ics=initial_conditions)

sympy.pprint(part_soln)