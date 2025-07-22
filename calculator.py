from tkinter import *

root = Tk()
root.title("Python Calculator")
root.geometry("350x400")

# Frame that fills root and contains everything
container = Frame(root, bg="white smoke")
container.pack(fill=BOTH, expand=1, padx=5, pady=5)

# The main display screen
txtDisplay = Entry(container, bd=2, font=("arial", 20, "bold"), insertwidth=2, bg="alice blue", justify="right")
txtDisplay.grid(columnspan=4, padx=20, pady=30)

## First row of buttons
# Clear screen button
clear_btn = Button(container, padx=59, pady=5, text="C", bd=1, font=("arial", 14), bg="indian red")
clear_btn.grid(row=1, columnspan=2)

# Bracket buttons
bracket1_btn = Button(container, padx=19, pady=5, text="(", bd=1, font=("arial", 14))
bracket1_btn.grid(row=1, column=2)

bracket2_btn = Button(container, padx=19, pady=5, text=")", bd=1, font=("arial", 14))
bracket2_btn.grid(row=1, column=3)

# third row
btn7 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="7")
btn7.grid(row=2, column=0)

btn8 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="8")
btn8.grid(row=2, column=1)

btn9 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="9")
btn9.grid(row=2, column=2)

btn_div = Button(container, padx=19, pady=5, bd=1, font=("arial", 14), text="/")
btn_div.grid(row=2, column=3)

# fourth row
btn4 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="4")
btn4.grid(row=3, column=0)

btn5 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="5")
btn5.grid(row=3, column=1)

btn6 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="6")
btn6.grid(row=3, column=2)

btn_minus = Button(container, padx=19, pady=5, bd=1, font=("arial", 14), text="-")
btn_minus.grid(row=3, column=3)

# fifth row
btn1 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="1")
btn1.grid(row=4, column=0)

btn2 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="2")
btn2.grid(row=4, column=1)

btn3 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="3")
btn3.grid(row=4, column=2)

btn_mult = Button(container, padx=19, pady=5, bd=1, font=("arial", 14), text="*")
btn_mult.grid(row=4, column=3)

# sixth row
btn0 = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="0")
btn0.grid(row=5, column=0)

btn_dot = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text=".")
btn_dot.grid(row=5, column=1)

btn_equal = Button(container, padx=16, pady=5, bd=1, font=("arial", 14), text="=")
btn_equal.grid(row=5, column=2)

btn_plus = Button(container, padx=19, pady=5, bd=1, font=("arial", 14), text="+")
btn_plus.grid(row=5, column=3)


root.mainloop()
