from scipy.optimize import fsolve

# Definicja funkcji układu równań
def equations(vars):
    x1, x2, x3, x4, x5, x6 = vars
    # Tutaj wprowadź równania zgodnie z twoimi potrzebami
    eq1 = x1 + x2 + x3 - 3
    eq2 = x4 * x5 - x6 - 1
    eq3 = x1 + x2 + x3 - 3
    eq4 = x4 * x5 - x6 - 1
    eq5 = x1 + x2 + x3 - 3
    eq6 = x4 * x5 - x6 - 1
    eq7 = x1 + x2 + x3 - 3
    eq8 = x4 * x5 - x6 - 1
    eq9 = x1 + x2 + x3 - 3
    eq10 = x4 * x5 - x6 - 1
    eq11 = x1 + x2 + x3 - 3
    eq12 = x1 * x2 - x3 - 2

    return [eq1, eq2, eq3, eq4, eq5, eq6]#, eq7, eq8, eq9, eq10, eq11, eq12]

# Początkowe przybliżenia dla zmiennych
initial_guess = [1, 1, 1, 1, 1, 1]

# Rozwiązanie układu równań nieliniowych
solution = fsolve(equations, initial_guess)

print("Rozwiązanie:", solution)