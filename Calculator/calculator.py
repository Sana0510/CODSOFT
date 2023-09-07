import tkinter
from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("278x600+100+200")
root.resizable(False,False)
root.configure(bg="#FFE4E1")

appicon=PhotoImage(file="C:/Users/DELL/Downloads/calc.png")
root.iconphoto(False,appicon)

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation !="" :
        try:
            result = eval(equation)
        except:result = "error"
        equation = ""
    label_result.config(text=result)

label_result= Label(root,width=25,height=1,text="",font=("calibri",30))
label_result.pack()

Button(root,text="C",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#33A1C9", command=lambda:clear()).place(x=4,y=100)
Button(root,text="/",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("/")).place(x=75,y=100)
Button(root,text="%",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("%")).place(x=146,y=100)
Button(root,text="*",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("*")).place(x=215,y=100)

Button(root,text="7",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("7")).place(x=4,y=200)
Button(root,text="8",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("8")).place(x=75,y=200)
Button(root,text="9",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("9")).place(x=146,y=200)
Button(root,text="-",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("-")).place(x=215,y=200)

Button(root,text="4",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("4")).place(x=4,y=300)
Button(root,text="5",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("5")).place(x=75,y=300)
Button(root,text="6",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("6")).place(x=146,y=300)
Button(root,text="+",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("+")).place(x=215,y=300)

Button(root,text="1",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("1")).place(x=4,y=400)
Button(root,text="2",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("2")).place(x=75,y=400)
Button(root,text="3",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("3")).place(x=146,y=400)
Button(root,text="0",width=7,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show("0")).place(x=4,y=500)

Button(root,text=".",width=3,height=1,font=("calibri",25,"bold"),bd=1,fg="white",bg="#AEEEEE", command=lambda:show(".")).place(x=146,y=500)
Button(root,text="=",width=3,height=4,font=("calibri",25,"bold"),bd=1,fg="white",bg="#33A1C9", command=lambda:calculate()).place(x=215,y=400)



root.mainloop()
