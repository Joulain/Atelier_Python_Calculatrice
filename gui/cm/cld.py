# v1

CALCULATOR = ""


def press_number(value):
    global CALCULATOR
    if type(CALCULATOR) is int or type(CALCULATOR) is float:
        CALCULATOR = ""
    CALCULATOR = CALCULATOR + str(value)


def press_operator(operator):
    global CALCULATOR
    if type(CALCULATOR) is int:
        CALCULATOR = str(CALCULATOR)
    CALCULATOR = CALCULATOR + f' {str(operator)} '


def press_point(point):
    global CALCULATOR
    temp = CALCULATOR.split(" ")
    if len(temp[-1]) == 0:
        CALCULATOR = CALCULATOR + f'0{str(point)}'
    elif "." not in temp[-1]:
        CALCULATOR = CALCULATOR + str(point)


def equals():
    global CALCULATOR
    CALCULATOR = eval(CALCULATOR)


def delete():
    global CALCULATOR
    CALCULATOR = str(CALCULATOR)
    CALCULATOR = CALCULATOR[:-1]


def clear():
    global CALCULATOR
    CALCULATOR = ""
