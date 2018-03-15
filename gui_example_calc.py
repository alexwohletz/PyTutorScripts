from tkinter import *
root = Tk()
root.title("Calculator")
total = 0
#=================================================================================
def Var(variable):
    Display.insert(total, variable)
def Operation(sign):
    Display.insert(total, sign)
# def _sub
# def _mult
# def _divide
# def _equals



#=================================================================================
Display = Entry(text = "", width = 15)

Dot = Button(root,text = ".", width = 2, height = 1, command = Var("."))
Zero = Button(text = "0", width = 2, height = 1, command = Var(0))
One = Button(text = "1", width = 2, height = 1, command = Var(1))
Two = Button(text = "2", width = 2, height = 1, command = Var(2))
Three = Button(text = "3", width = 2, height = 1, command = Var(3))
Four = Button(text = "4", width = 2, height = 1, command = Var(4))
Five = Button(text = "5", width = 2, height = 1, command = Var(5))
Six = Button(text = "6", width = 2, height = 1, command = Var(6))
Seven = Button(text = "7", width = 2, height = 1, command = Var(7))
Eight = Button(text = "8", width = 2, height = 1, command = Var(8))
Nine = Button(text = "9", width = 2, height = 1, command = Var(9))

Add = Button(text = "+", width = 2, height = 1, command = lambda x,y: x+y)
Sub = Button(text = "-", width = 2, height = 1, command = lambda : Operation("-"))
Mult = Button(text = "x", width = 2, height = 1, command = lambda : Operation("x"))
Divide = Button(text = "÷", width = 2, height = 1, command = lambda : Operation("÷"))
Equals = Button(text = "=", width = 2, height = 1)
#=================================================================================
Display.grid(row = 0,column = 0, columnspan = 4)

Dot.grid(row = 4,column = 2)
Zero.grid(row = 4,column = 0, columnspan = 2, sticky = "WE")
One.grid(row = 3,column = 0)
Two.grid(row = 3,column = 1)
Three.grid(row = 3,column = 2)
Four.grid(row = 2,column = 0)
Five.grid(row = 2,column = 1)
Six.grid(row = 2,column = 2)
Seven.grid(row = 1,column = 0)
Eight.grid(row = 1,column = 1)
Nine.grid(row = 1,column = 2)

Add.grid(row = 1,column = 3)
Sub.grid(row = 2,column = 3)
Mult.grid(row = 3,column = 3)
Divide.grid(row = 4,column = 3)
Equals.grid(row = 5,column = 0, columnspan = 4, sticky = "WE")
#=================================================================================



root.mainloop()