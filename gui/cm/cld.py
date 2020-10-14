# v0.22

CURRENT_CALCULATOR = ""

GLOBAL_CALCULATOR = ""


def press(value):
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + str(value)


def equals():
    global CURRENT_CALCULATOR
    global GLOBAL_CALCULATOR
    GLOBAL_CALCULATOR = eval(CURRENT_CALCULATOR)
    CURRENT_CALCULATOR = ""


def delete():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR[:-1]


def clear_environment():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = ""


def clear():
    global CURRENT_CALCULATOR
    global GLOBAL_CALCULATOR
    CURRENT_CALCULATOR = GLOBAL_CALCULATOR = ""
