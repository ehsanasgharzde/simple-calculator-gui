from tkinter import *


WIDTH = 8
HEIGHT = 4
X = 5
Y = 2

class GUI(Frame):
    """
    Tkinter GUI.
    """

    def __init__(self, master):
        """
        Initializes the frame.
        """

        Frame.__init__(self, master)
        self.entry = Entry(master, font=("Arial", 25))
        self.entry.grid(row=0, column=0, columnspan=4)

        self.entry.focus_set()
        self.entry.configure(
            state="disabled",
            disabledbackground="grey95",
            disabledforeground="black")
        self.widgets(master)
        self.bindder(master)
        self.grid()

    def adder(self, char):
        """
        Concatenates a character passed from a button press (or key type)
        to a string.
        """
        self.entry.configure(state="normal")

        if self.entry.get() == "Invalid Input":
            self.entry.delete(0,END)

        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def backspace(self):
        """
        Allows user to backspace their entry.
        """
        self.entry.configure(state="normal")

        if self.entry.get() != "Invalid Input":
            text = self.entry.get()[:-1]

            self.entry.delete(0,END)
            self.entry.insert(0,text)
        else:
            self.entry.delete(0, END)

        self.entry.configure(state="disabled")

    def clear(self):
        """
        Allows user to clear the full entry.
        """
        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def calculate(self):
        """
        Changes the operation symbols to their mathematical representation used in
        the eval() method.
        """
        self.entry.configure(state="normal")
        equation = self.entry.get()
        equation = equation.replace("×", "*")
        equation = equation.replace("÷", "/")

        try:
            answer = eval(equation)
        except Exception:
            self.entry.delete(0,END)
            self.entry.insert(0, "Invalid Input")
        else:
            self.entry.delete(0,END)
            if len(str(answer)) > 20:
                self.entry.insert(0, "{:.10e}".format(answer))
            else:
                self.entry.insert(0, answer)

        self.entry.configure(state="disabled")

    def bindder(self, master):
        """
        Binds keys to their appropriate input
        """
        master.bind("<Return>", lambda event, button=self.equalBtn: self.calculate())
        master.bind("<BackSpace>", lambda event, button=self.clearBtn: self.backspace())
        master.bind("9", lambda event, char="9", button=self.nineBtn: self.adder(char))
        master.bind("8", lambda event, char="8", button=self.eightBtn: self.adder(char))
        master.bind("7", lambda event, char="7", button=self.sevenBtn: self.adder(char))
        master.bind("6", lambda event, char="6", button=self.sixBtn: self.adder(char))
        master.bind("5", lambda event, char="5", button=self.fiveBtn: self.adder(char))
        master.bind("4", lambda event, char="4", button=self.fourBtn: self.adder(char))
        master.bind("3", lambda event, char="3", button=self.threeBtn: self.adder(char))
        master.bind("2", lambda event, char="2", button=self.twoBtn: self.adder(char))
        master.bind("1", lambda event, char="1", button=self.onebtn: self.adder(char))
        master.bind("0", lambda event, char="0", button=self.zeroBtn: self.adder(char))
        master.bind("*", lambda event, char="×", button=self.multiplyBtn: self.adder(char))
        master.bind("/", lambda event, char="÷", button=self.divideBtn: self.adder(char))
        master.bind("%", lambda event, char="%", button=self.modBtn: self.adder(char))
        master.bind(".", lambda event, char=".", button=self.declearBtn: self.adder(char))
        master.bind("-", lambda event, char="-", button=self.subtractBtn: self.adder(char))
        master.bind("+", lambda event, char="+", button=self.addBtn: self.adder(char))
        master.bind("(", lambda event, char="(", button=self.lparBtn: self.adder(char))
        master.bind(")", lambda event, char=")", button=self.rparBtn: self.adder(char))
        master.bind("c", lambda event, button=self.aclearBtn: self.clear())

    def widgets(self, master):
        """
        Creates the widgets to be used in the grid.
        """
        self.aclearBtn = Button(master, text="Ce", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.clear())
        self.aclearBtn.grid(row=1, column=0, padx=X, pady=Y)

        self.clearBtn = Button(master, text="←", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.backspace())
        self.clearBtn.grid(row=1, column=1, padx=X, pady=Y)

        self.lparBtn = Button(master, text="(", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder("("))
        self.lparBtn.grid(row=1, column=2, padx=X, pady=Y)

        self.rparBtn = Button(master, text=")", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(")"))
        self.rparBtn.grid(row=1, column=3, padx=X, pady=Y)

        self.sevenBtn = Button(master, text="7", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(7))
        self.sevenBtn.grid(row=2, column=0, padx=X, pady=Y)

        self.eightBtn = Button(master, text="8", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(8))
        self.eightBtn.grid(row=2, column=1, padx=X, pady=Y)

        self.nineBtn = Button(master, text="9", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(9))
        self.nineBtn.grid(row=2, column=2, padx=X, pady=Y)

        self.modBtn = Button(master, text="%", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder("%"))
        self.modBtn.grid(row=2, column=3, padx=X, pady=Y)

        self.fourBtn = Button(master, text="4", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(4))
        self.fourBtn.grid(row=3, column=0, padx=X, pady=Y)

        self.fiveBtn = Button(master, text="5", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(5))
        self.fiveBtn.grid(row=3, column=1, padx=X, pady=Y)

        self.sixBtn = Button(master, text="6", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(6))
        self.sixBtn.grid(row=3, column=2, padx=X, pady=Y)

        self.divideBtn = Button(master, text="÷", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder("÷"))
        self.divideBtn.grid(row=3, column=3, padx=X, pady=Y)

        self.onebtn = Button(master, text="1", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(1))
        self.onebtn.grid(row=4, column=0, padx=X, pady=Y)

        self.twoBtn = Button(master, text="2", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(2))
        self.twoBtn.grid(row=4, column=1, padx=X, pady=Y)

        self.threeBtn = Button(master, text="3", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(3))
        self.threeBtn.grid(row=4, column=2, padx=X, pady=Y)

        self.multiplyBtn = Button(master, text="×", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder("×"))
        self.multiplyBtn.grid(row=4, column=3, padx=X, pady=Y)

        self.declearBtn = Button(master, text=".", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder("."))
        self.declearBtn.grid(row=5, column=0, padx=X, pady=Y)

        self.zeroBtn = Button(master, text="0", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder(0))
        self.zeroBtn.grid(row=5, column=1, padx=X, pady=Y)

        self.subtractBtn = Button(master, text="-", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder("-"))
        self.subtractBtn.grid(row=5, column=2, padx=X, pady=Y)

        self.addBtn = Button(master, text="+", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.adder("+"))
        self.addBtn.grid(row=5, column=3, padx=X, pady=Y)

        self.empty1Btn = Button(master, text="", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0)
        self.empty1Btn.grid(row=6, column=0, padx=X, pady=Y)

        self.empty2Btn = Button(master, text="", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0)
        self.empty2Btn.grid(row=6, column=1, padx=X, pady=Y)

        self.empty3Btn = Button(master, text="", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0)
        self.empty3Btn.grid(row=6, column=2, padx=X, pady=Y)

        self.equalBtn = Button(master, text="=", width=WIDTH, height=HEIGHT, font='Arial 12', highlightthickness=0, command=lambda: self.calculate())
        self.equalBtn.grid(row=6, column=3, padx=X, pady=Y)







app = Tk()
app.title("Calculator")

app.minsize(340, 500)
app.resizable(width=False, height=False)

gui = GUI(app)

app.mainloop()