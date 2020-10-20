# v1

from gui.cm import cld as cld
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
        tk.Tk.iconbitmap(self, default='resources/square-root.ico')
        tk.Tk.geometry(self, FRAME_SIZE)
        self.show = None
        self.add_label()
        self.add_operator()
        self.add_number()

    def add_label(self):
        self.show = tk.Label(self, text="", bg="white", height=BUTTON_HEIGHT, width="45")
        self.show.grid(column=0, row=0, columnspan=4)

    def add_operator(self):
        c = tk.Button(self, text="C", justify="center", height=BUTTON_HEIGHT, width=22, command=self.clear)
        c.grid(column="0", row="1", columnspan="2")
        deletion = tk.Button(self, text="del", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                             command=self.delete)
        deletion.grid(column="2", row="1")
        plus = tk.Button(self, text="+", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                         command=lambda: [cld.press_operator("+"), self.update()])
        plus.grid(column="3", row="4")
        minus = tk.Button(self, text="-", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                          command=lambda: [cld.press_operator("-"), self.update()])
        minus.grid(column="3", row="3")
        multiply = tk.Button(self, text="*", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                             command=lambda: [cld.press_operator("*"), self.update()])
        multiply.grid(column="3", row="2")
        division = tk.Button(self, text="/", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                             command=lambda: [cld.press_operator("/"), self.update()])
        division.grid(column="3", row="1")
        coma = tk.Button(self, text=",", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                         command=lambda: [cld.press_point("."), self.update()])
        coma.grid(column="0", row="5")
        equal = tk.Button(self, text="=", justify="center", height=BUTTON_HEIGHT, width=22,
                          command=lambda: [cld.equals(), self.update()])
        equal.grid(column="2", row="5", columnspan="2")

    def add_number(self):
        seven = tk.Button(self, text="7", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                          command=lambda: [cld.press_number(7), self.update()])
        seven.grid(column="0", row="2")
        eight = tk.Button(self, text="8", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                          command=lambda: [cld.press_number(8), self.update()])
        eight.grid(column="1", row="2")
        nine = tk.Button(self, text="9", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                         command=lambda: [cld.press_number(9), self.update()])
        nine.grid(column="2", row="2")
        four = tk.Button(self, text="4", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                         command=lambda: [cld.press_number(4), self.update()])
        four.grid(column="0", row="3")
        five = tk.Button(self, text="5", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                         command=lambda: [cld.press_number(5), self.update()])
        five.grid(column="1", row="3")
        six = tk.Button(self, text="6", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                        command=lambda: [cld.press_number(6), self.update()])
        six.grid(column="2", row="3")
        one = tk.Button(self, text="1", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                        command=lambda: [cld.press_number(1), self.update()])
        one.grid(column="0", row="4")
        two = tk.Button(self, text="2", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                        command=lambda: [cld.press_number(2), self.update()])
        two.grid(column="1", row="4")
        three = tk.Button(self, text="3", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                          command=lambda: [cld.press_number(3), self.update()])
        three.grid(column="2", row="4")
        zero = tk.Button(self, text="0", justify="center", height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                         command=lambda: [cld.press_number(0), self.update()])
        zero.grid(column="1", row="5")

    def update(self):
        self.show["text"] = cld.CALCULATOR

    def delete(self):
        cld.delete()
        self.show["text"] = cld.CALCULATOR

    def clear(self):
        cld.clear()
        self.show["text"] = cld.CALCULATOR


root = Application()
root.mainloop()
