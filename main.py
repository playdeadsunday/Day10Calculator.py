import calculator_art
import os
def clear(): return os.system('cls')


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 == 0:
        return "Division by zero error."
    return n1 / n2


def calculator():
    print(calculator_art.logo)
    num1 = float(input("Whats the first number?: "))

    operations = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : div,
    }

    for key in operations:
        print(key)

    should_continue = True

    while should_continue:
        op = input("What operation do want to conduct? ")

        num2 = float(input("Whats the next number?: "))

        function = operations[op]

        result = function(num1, num2)
        if op == "/" and num2 == 0:
            print(f"{result}")
            break
        else:
            print(f"{num1} {op} {num2} = {result}")

        is_continue = input(f"Type 'y to continue calculating with {result}, or type 'n' to exit: ").lower()
        if is_continue == 'y':
            num1 = result
        else:
            should_continue = False
            clear()
            calculator()


calculator()

