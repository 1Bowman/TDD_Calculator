import re


def controller(input_string):
    m = re.match('(\d+(\.\d+)?)(\+|-|\*|/)(\d+(\.\d+)?)', input_string)
    try:
        val1 = m.group(1)
        operator = m.group(3)
        val2 = m.group(4)
    except:
        return 'Incorrect expression'

    if operator == '+':
        return add(val1, val2)
    elif operator == '-':
        return sub(val1, val2)
    elif operator == '*':
        return mul(val1, val2)
    elif operator == '/':
        return div(val1, val2)
    else:
        return 'Incorrect expression'


def add(val1, val2):
    return float(val1) + float(val2)


def sub(val1, val2):
    return float(val1) - float(val2)


def mul(val1, val2):
    return float(val1) * float(val2)

  
def div(val1, val2):
    return float(val1) / float(val2)


def take_user_input():
    return str(input())

if __name__ == "__main__":
    while True:
        userInput = take_user_input()
        controller(userInput)
