import tkinter as tk

equation = "" 

def show(value):
    global equation
    equation += value
    text_result.config(text=equation)
    
def clear():
    global equation
    equation = ""
    text_result.config(text=equation)


def calculate():
    global equation
    eq = eval(equation)
    text_result.config(text=str(eq))

root = tk.Tk()
root.geometry("300x250")
root.title("Calculator")
root.resizable(False, False)

text_result = tk.Label(root, width=25, height=2, text="0")
text_result.pack(padx=0,pady=0)

tk.Button(root, text="C", width=3, height=2, bd=1,command=clear).place(x=0, y=50)
tk.Button(root, text="/", width=3, height=2, bd=1,command=lambda: show("/")).place(x=80, y=50)
tk.Button(root, text="%", width=3, height=2, bd=1,command=lambda: show("%")).place(x=160, y=50)
tk.Button(root, text="*", width=3, height=2, bd=1,command=lambda: show("*")).place(x=240, y=50)

tk.Button(root, text="7", width=3, height=2, bd=1,command=lambda: show("7")).place(x=0, y=100)
tk.Button(root, text="8", width=3, height=2, bd=1,command=lambda: show("8")).place(x=80, y=100)
tk.Button(root, text="9", width=3, height=2, bd=1,command=lambda: show("9")).place(x=160, y=100)
tk.Button(root, text="-", width=3, height=2, bd=1,command=lambda: show("-")).place(x=240, y=100)

tk.Button(root, text="4", width=3, height=2, bd=1,command=lambda: show("4")).place(x=0, y=150)
tk.Button(root, text="5", width=3, height=2, bd=1,command=lambda: show("5")).place(x=80, y=150)
tk.Button(root, text="6", width=3, height=2, bd=1,command=lambda: show("6")).place(x=160, y=150)
tk.Button(root, text="+", width=3, height=2, bd=1,command=lambda: show("+")).place(x=240, y=150)

tk.Button(root, text="1", width=3, height=2, bd=1,command=lambda: show("1")).place(x=0, y=200)
tk.Button(root, text="2", width=3, height=2, bd=1,command=lambda: show("2")).place(x=80, y=200)
tk.Button(root, text="3", width=3, height=2, bd=1,command=lambda: show("3")).place(x=160, y=200)
tk.Button(root, text="=", width=3, height=2, bd=1,command=lambda: calculate()).place(x=240, y=200)






root.mainloop()


