from cm import cld as cld
import tkinter as tk

# The size if the frame
FRAME_SIZE = "320x510"
# The height of buttons
BUTTON_HEIGHT = 5
# The width of buttons
BUTTON_WIDTH = BUTTON_HEIGHT * 2


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Bobby")
        tk.Tk.iconbitmap(self, default='ressources/square-root.ico')
        tk.Tk.geometry(self, FRAME_SIZE)
        self.add_label()
        self.add_operator()
        self.add_number()

    def add_label(self):
        test = tk.Label(self, bg="white", height=BUTTON_HEIGHT, width="40").grid(column=0, row=0, columnspan=4)
        self.show_equation = tk.Label(self, text="", bg="white", justify="right", anchor="e", height=BUTTON_HEIGHT, width=33)
        self.show_equation.grid(column="0", row="0", columnspan="3", sticky='e')
        self.show_result = tk.Label(self, text="=", bg="white", justify="right", anchor="e", height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        self.show_result.grid(column="3", row="0", sticky="e")

    def add_operator(self):
        ce = tk.Button(self, text="CE", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=self.clear_environment)
        ce.grid(column="0", row="1")
        c = tk.Button(self, text="C", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=self.clear)
        c.grid(column="1", row="1")
        dela = tk.Button(self, text="del", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        dela.grid(column="2", row="1")
        plus = tk.Button(self, text="+", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        plus.grid(column="3", row="4")
        minus = tk.Button(self, text="-", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        minus.grid(column="3", row="3")
        multiply = tk.Button(self, text="*", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        multiply.grid(column="3", row="2")
        division = tk.Button(self, text="/", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        division.grid(column="3", row="1")
        coma = tk.Button(self, text=",", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        coma.grid(column="2", row="5")
        absolute = tk.Button(self, text="+/-", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        absolute.grid(column="0", row="5")
        equal = tk.Button(self, text="=", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=self.equals)
        equal.grid(column="3", row="5")

    def add_number(self):
        seven = tk.Button(self, text="7", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.seven(), self.update()])
        seven.grid(column="0", row="2")
        eight = tk.Button(self, text="8", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.eight(), self.update()])
        eight.grid(column="1", row="2")
        nine = tk.Button(self, text="9", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.nine(), self.update()])
        nine.grid(column="2", row="2")
        four = tk.Button(self, text="4", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.four(), self.update()])
        four.grid(column="0", row="3")
        five = tk.Button(self, text="5", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.five(), self.update()])
        five.grid(column="1", row="3")
        six = tk.Button(self, text="6", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.six(), self.update()])
        six.grid(column="2", row="3")
        one = tk.Button(self, text="1", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.one(), self.update()])
        one.grid(column="0", row="4")
        two = tk.Button(self, text="2", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.two(), self.update()])
        two.grid(column="1", row="4")
        three = tk.Button(self, text="3", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.three(), self.update()])
        three.grid(column="2", row="4")
        zero = tk.Button(self, text="0", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: [cld.zero(), self.update()])
        zero.grid(column="1", row="5")

    def update(self):
        self.show_equation["text"] = cld.CURRENT_CALCULATOR

    def equals(self):
        self.show_result["text"] = "= " + self.show_equation["text"]

    def clear_environment(self):
        self.show_equation["text"] = ""
        cld.clear_environment()

    def clear(self):
        self.show_result["text"] = "= "
        self.show_equation["text"] = ""
        cld.clear()


root = Application()
root.mainloop()
