from tkinter import *

def btnClick(number):
	global operator
	operator+=str(number)
	text_Input.set(operator)
def btnCDisplay():
	global operator
	operator=""
	text_Input.set("")
def btnEqualInput():
	global operator
	sumup=str(eval(operator))
	text_Input.set(sumup)
	operator=""
def btnrev():
    global operator
    operator=-(float(textDisplay.get()))
    text_Input.set(operator)
def btnpercent():
    global operator
    operator=(float(textDisplay.get()))
    text_Input.set(operator/100)

window=Tk();
window.title("Calculator")
operator=""
text_Input=StringVar()


textDisplay=Entry(window,textvariable=text_Input,justify='right',bd=12,font=("simsun",14))
textDisplay.grid(columnspan=4)

btnC=Button(window,text="C",width=7,height=2,command=btnCDisplay)
btnC.grid(row=1,column=0)
rev=Button(window,text="+/-",width=7,height=2,command=btnrev)
rev.grid(row=1,column=1)
percent=Button(window,text="%",width=7,height=2,command=btnpercent)
percent.grid(row=1,column=2)
div=Button(window,text="/",width=7,height=2,command=lambda:btnClick("/"))
div.grid(row=1,column=3)
########################
btn7=Button(window,text="7",width=7,height=2,command=lambda:btnClick(7))
btn7.grid(row=2,column=0)
btn8=Button(window,text="8",width=7,height=2,command=lambda:btnClick(8))
btn8.grid(row=2,column=1)
btn9=Button(window,text="9",width=7,height=2,command=lambda:btnClick(9))
btn9.grid(row=2,column=2)
mult=Button(window,text="x",width=7,height=2,command=lambda:btnClick("*"))
mult.grid(row=2,column=3)
########################
btn4=Button(window,text="4",width=7,height=2,command=lambda:btnClick(4))
btn4.grid(row=3,column=0)
btn5=Button(window,text="5",width=7,height=2,command=lambda:btnClick(5))
btn5.grid(row=3,column=1)
btn6=Button(window,text="6",width=7,height=2,command=lambda:btnClick(6))
btn6.grid(row=3,column=2)
sub=Button(window,text="-",width=7,height=2,command=lambda:btnClick("-"))
sub.grid(row=3,column=3)
########################
btn1=Button(window,text="1",width=7,height=2,command=lambda:btnClick(1))
btn1.grid(row=4,column=0)
btn2=Button(window,text="2",width=7,height=2,command=lambda:btnClick(2))
btn2.grid(row=4,column=1)
btn3=Button(window,text="3",width=7,height=2,command=lambda:btnClick(3))
btn3.grid(row=4,column=2)
add=Button(window,text="+",width=7,height=2,command=lambda:btnClick("+"))
add.grid(row=4,column=3)
########################
btn0=Button(window,text="0",width=16,height=2,command=lambda:btnClick(0))
btn0.grid(row=5,columnspan=2)
dot=Button(window,text=".",width=7,height=2,command=lambda:btnClick("."))
dot.grid(row=5,column=2)
equal=Button(window,text="=",width=7,height=2,command=btnEqualInput)
equal.grid(row=5,column=3)
window.mainloop();