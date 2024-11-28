#Job5
def calcule(num1, operator, num2):
    if operator == "*":
        return num1 * num2
    elif operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Modulo par zéro"
    else:
        return "Erreur : Opérateur non valide"
print("5 + 3 =", calcule(5, "+", 3))
print("10 - 7 =", calcule(10, "-", 7))
print("4 * 6 =", calcule(4, "*", 6))
print("8 / 2 =", calcule(8, "/", 2))
print("9 % 4 =", calcule(9, "%", 4))
print("10 / 0 =", calcule(10, "/", 0))
print("12 % 0 =", calcule(12, "%", 0))