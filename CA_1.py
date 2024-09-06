#minimizing the function  f(x,y)=x**2 + y**2 + 3*x + 4*y + 5

from scipy.optimize import minimize

# Define the multivariable function
def objective(vars):
    x, y = vars
    return x**2 + y**2 + 3*x + 4*y + 5

# Initial guess
initial_guess = [0, 0]
# Minimize the function
result = minimize(objective, initial_guess)
print("Minimum found at (x, y):", result.x)
print("Minimum value of the function:", result.fun)
