from tkinter import*
import parser
from math import factorial
root=Tk()
root.title("calculator")
root.geometry("400x400")
display=Entry(root)
display.grid(row=0,columnspan=6,sticky=W+E)
#get user input in the text field
i=0
def get_user(num):
    global i
    display.insert(i,num)
    i+=1

#clear function
def clear_all():
    display.delete(0,END)

#delete buutomn
def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"error")

def get_oper(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calc():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except :
        clear_all()
        display.insert(0,"syntax error")
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
# def recur(x):
#     if x==1 or x==0:
#         return 1
#     else:
#         return x*recur(x-1)
#
# def fact():
#     input=display.get()
#     result=recur(int(input))
#     clear_all()
#     display.insert(0,result)



#adding buttons
Button(root,text="7",command=lambda: get_user(7)).grid(row=1,column=0)
Button(root,text="8",command=lambda :get_user(8)).grid(row=1,column=1)
Button(root,text="9",command=lambda :get_user(9)).grid(row=1,column=2)
Button(root,text="4",command=lambda :get_user(4)).grid(row=2,column=0)
Button(root,text="5",command=lambda :get_user(5)).grid(row=2,column=1)
Button(root,text="6",command=lambda :get_user(6)).grid(row=2,column=2)
Button(root,text="1",command=lambda :get_user(1)).grid(row=3,column=0)
Button(root,text="2",command=lambda :get_user(2)).grid(row=3,column=1)
Button(root,text="3",command=lambda :get_user(3)).grid(row=3,column=2)
Button(root,text=".",command=lambda :get_user(".")).grid(row=4,column=0)
Button(root,text="0",command=lambda:get_user(0)).grid(row=4,column=1)
Button(root,text="=",command=lambda :calc()).grid(row=4,column=2)

Button(root,text="/",command=lambda:get_oper("/")).grid(row=1,column=3)
Button(root,text="*",command=lambda:get_oper("*")).grid(row=2,column=3)
Button(root,text="-",command=lambda:get_oper("-")).grid(row=3,column=3)
Button(root,text="+",command=lambda:get_oper("+")).grid(row=4,column=3)

Button(root,text="AC",command=lambda :clear_all()).grid(row=1,column=4)
Button(root,text="<-",command=lambda :undo()).grid(row=1,column=5)
Button(root,text="!",command=lambda:get_oper("(")).grid(row=2,column=4)
Button(root,text=")",command=lambda:get_oper(")")).grid(row=2,column=5)
Button(root,text="%",command=lambda:get_oper("/100")).grid(row=3,column=4)
Button(root,text="pi",command=lambda:get_oper("*3.14")).grid(row=3,column=5)
Button(root,text="exp",command=lambda:get_oper("**")).grid(row=4,column=4)
Button(root,text="x^2",command=lambda:get_oper("**2")).grid(row=4,column=5)
Button(root,text="!",command=lambda:fact()).grid(row=4,column=6)
root.mainloop()