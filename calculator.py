import re


def view():
    while True:
        input_string = take_user_input()
        pattern = re.search('\d*(\.\d+)?', input_string)
        if pattern:
            print(pattern)
        else:
            print("Incorrect expression")


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
    view()
