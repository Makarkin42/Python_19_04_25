import sympy

def solve(equ):
    if "=" in equ:
        parts = equ.split("=")
        equ = f"{parts[0]} - ({parts[1]})"
    x = sympy.Symbol("x")
    result = sympy.solve(sympy.sympify(equ),x)
    return result

if __name__ == "__main__":
    ask = input("Введите уравнение...\n")
    result = solve(ask)
    print(result)