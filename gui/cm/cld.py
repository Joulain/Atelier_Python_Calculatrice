PREVIOUS_CALCULATOR = ""

CURRENT_CALCULATOR = ""

GLOBAL_CALCULATOR = ""

CURRENT_OPERATOR = ""


def one():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "1"


def two():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "2"


def three():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "3"


def four():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "4"


def five():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "5"


def six():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "6"


def seven():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "7"


def eight():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "8"


def nine():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "9"


def zero():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = CURRENT_CALCULATOR + "0"


def equals():
    global CURRENT_CALCULATOR
    print(CURRENT_CALCULATOR)


def clear_environment():
    global CURRENT_CALCULATOR
    CURRENT_CALCULATOR = ""


def clear():
    global CURRENT_CALCULATOR
    global GLOBAL_CALCULATOR
    CURRENT_CALCULATOR = GLOBAL_CALCULATOR = ""


def addition():
    global CURRENT_CALCULATOR
    global CURRENT_OPERATOR
    global GLOBAL_CALCULATOR
    global PREVIOUS_CALCULATOR

    if len(PREVIOUS_CALCULATOR) == 0:
        PREVIOUS_CALCULATOR = CURRENT_CALCULATOR
        CURRENT_CALCULATOR = ""
        CURRENT_OPERATOR = "+"
    else:
        PREVIOUS_CALCULATOR = PREVIOUS_CALCULATOR + CURRENT_CALCULATOR

