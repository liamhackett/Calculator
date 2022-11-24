# Liam Hackett
# CS 21
# This program builds a fully functioning calculator using tkinter with buttons that when you push make the numbers
# appear in the entry field.
import tkinter
# This imports messagebox from tkinter for the history button feature on the calculator
from tkinter import messagebox


class Calculator:
    # Initialization function
    def __init__(self, master):
        # These global functions allow expression, input_text, and expression_list to be used in all functions so
        # each can be used in other functions
        global expression
        global input_text
        global expression_list

        self.master = master

        # This creates the list of all of the Expressions
        expression_list = []

        # This sets the title of the window to Calculator
        master.title('Calculator')

        # This sets the initial size of the window when launched
        master.geometry("390x375")

        master.resizable(0, 0)

        # This sets the initial expression to a blank statement
        expression = ""

        # This sets an initial instance of input_text
        input_text = tkinter.StringVar()

        # Entry Field
        # This line builds the entry field. By setting textvariable=input_text it allows the buttons to change the
        # entry field
        input_field = tkinter.Entry(master, font=('arial', '18', 'bold'), textvariable=input_text, justify="right")
        # This selects where it is on the grid. The sticky means that the borders stick to the east and west sides
        # of the button
        input_field.grid(row=0, column=1, columnspan=3, sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        # First Row of Buttons

        # Clear Button
        # This builds the clear button and sets it's command to the clear_button function
        clear = tkinter.Button(master, text='C', width=22, height=4, command=lambda: self.clear_button())
        clear.grid(row=1, column=0, columnspan=2, sticky=tkinter.W + tkinter.E)


        # Exponent Button
        exponent = tkinter.Button(master, text='^', width=10, height=4, command=lambda: self.press('**'))
        exponent.grid(row=1, column=2, sticky=tkinter.W)

        # Division button
        divide = tkinter.Button(master, text='/', width=10, height=4, command=lambda: self.press('/'))
        divide.grid(row=1, column=3, sticky=tkinter.W)

        # Second Row of Buttons

        # 7 Button
        seven = tkinter.Button(master, text='7', width=11, height=4, command=lambda: self.press(7))
        seven.grid(row=2, column=0, sticky=tkinter.W)

        # 8 Button
        eight = tkinter.Button(master, text='8', width=11, height=4, command=lambda: self.press(8))
        eight.grid(row=2, column=1, sticky=tkinter.W)

        # 9 Button
        nine = tkinter.Button(master, text='9', width=10, height=4, command=lambda: self.press(9))
        nine.grid(row=2, column=2, sticky=tkinter.W)

        # Multiplication button
        multiply = tkinter.Button(master, text='x', width=10, height=4, command=lambda: self.press('*'))
        multiply.grid(row=2, column=3, sticky=tkinter.W)

        # Third Row of Buttons

        # 4 Button
        four = tkinter.Button(master, text='4', width=11, height=4, command=lambda: self.press(4))
        four.grid(row=3, column=0, sticky=tkinter.W)

        # 5 Button
        five = tkinter.Button(master, text='5', width=11, height=4, command=lambda: self.press(5))
        five.grid(row=3, column=1, sticky=tkinter.W)

        # 6 Button
        six = tkinter.Button(master, text='6', width=10, height=4, command=lambda: self.press(6))
        six.grid(row=3, column=2, sticky=tkinter.W)

        # Addition Button
        add = tkinter.Button(master, text='+', width=10, height=4, command=lambda: self.press('+'))
        add.grid(row=3, column=3, sticky=tkinter.W)

        # Fourth Row of Buttons

        # 1 Button
        one = tkinter.Button(master, text='1', width=11, height=4, command=lambda: self.press(1))
        one.grid(row=4, column=0, sticky=tkinter.W)

        # 2 Button
        two = tkinter.Button(master, text='2', width=11, height=4, command=lambda: self.press(2))
        two.grid(row=4, column=1, sticky=tkinter.W)

        # 3 Button
        three = tkinter.Button(master, text='3', width=10, height=4, command=lambda: self.press(3))
        three.grid(row=4, column=2, sticky=tkinter.W)

        # Subtraction Button
        subtract = tkinter.Button(master, text='-', width=10, height=4, command=lambda: self.press('-'))
        subtract.grid(row=4, column=3, sticky=tkinter.W)

        # Fifth Row of Buttons

        # Zero Button
        zero = tkinter.Button(master, text='0', width=22, height=4, borderwidth=2, command=lambda: self.press(0))
        zero.grid(row=5, column=0, columnspan=2, sticky=tkinter.W + tkinter.E)

        # Decimal Button
        decimal = tkinter.Button(master, text='.', width=10, height=4, command=lambda: self.press('.'))
        decimal.grid(row=5, column=2, sticky=tkinter.W)

        # Equals Button
        equal = tkinter.Button(master, text='=', width=10, height=4, command=lambda: self.equal_button())
        equal.grid(row=5, column=3, sticky=tkinter.W)

        # History Button
        history = tkinter.Button(master, text='History', width=10, height=2, command=lambda: self.history_button())
        history.grid(row=-0, column=0, sticky=tkinter.W + tkinter.E)

    # FUNCTIONS

    # This function updates the input field updating expression by adding item to it. Item is the parameter
    # that says what button you are pressing. Using the set method it changes the input field to the updated expression
    # value.
    def press(self, item):
        global expression
        global input_text
        expression = expression + str(item)
        input_text.set(expression)

    # This function sets the input field to a blank field by setting the expression to an empty set of quotation marks
    def clear_button(self):
        global expression
        global input_text
        expression = ""
        input_text.set(expression)

    # This function uses the eval function to evaluate the expression in the input field
    def equal_button(self):
        global expression
        global input_text
        global expression_list
        # This try except statement tries to evaluate the function and if there is a SyntaxError it prints error
        # a syntax error will occur when someone types using the keyboard into the entry field and tries to solve an
        # equation. If there is a ZeroDivisionError it says Error cannot divide by 0
        try:
            total = str(eval(expression))
            input_text.set(total)
            expression = total
            # This adds each of the expression typed to a list so the user can check their history
            expression_list.append(expression)

        except SyntaxError:
            expression = "Error"
            input_text.set(expression)  # changes the input field to Error
        except ZeroDivisionError:
            expression = "Error Cannot Divide by 0"
            input_text.set(expression)  # changes the input field to Error Cannot Divide by 0

    # This function using tkinters messagebox to work as a function for the history button. When the button is
    # clicked it brings up a separate window using message box that has all of the expressions the user has entered.
    def history_button(self):
        global expression
        global expression_list
        messagebox.showinfo('History', "\n".join(expression_list))


# This generates the window
window = tkinter.Tk()
my_gui = Calculator(window)
window.mainloop()
