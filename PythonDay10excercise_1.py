# Calculator

from PythonDay10calculator_art import logo


def operation(operator, num1, num2):
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        return num1/num2


# def add(n1, n2):
#     return n1+n2


# def substract(n1, n2):
#     return n1-n2


# def multiply(n1, n2):
#     return n1*n2


# def divide(n1, n2):
#     return n1/n2


ope = {
    '+': '+',
    '-': '-',
    '*': '*',
    '/': '/'
}


def calculator():
    print(logo)
    Num_1 = int(input('Enter your first number: '))
    calculate_need = True
    # for oper in ope:
    #     print(oper)
    while calculate_need:
        for oper in ope:
            print(oper)
        oper_symbal = input('Pick an operation from the above :')
        Num_2 = int(input('Enter your second number: '))
        answer = operation(ope[oper_symbal], num1=Num_1, num2=Num_2)
        print(f'{Num_1} {oper_symbal}{Num_2}={answer}')
        next = input(
            "Pick another operation ? Type 'Yes' or Type 'No' to discard :").lower()
        if next == 'yes':
            Num_1 = answer
        else:
            calculate_need = False
            calculator()


calculator()
