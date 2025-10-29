import tkinter as tk
from tkinter import font
import numexpr

root=tk.Tk()
root.title("Modern Calculator")
realScreenWidth=root.winfo_screenwidth()
realScreenHeight=root.winfo_screenheight()
rootWidth=370
rootHeight=530
xAxisPosition=(realScreenWidth//2)-(rootWidth//2)
yAxisPosition=(realScreenHeight//2)-(rootHeight//2)
root.geometry(f"{rootWidth}x{rootHeight}+{xAxisPosition}+{yAxisPosition}")
root.configure(bg="#e0e5ec")
root.resizable(False,False)

expression= ""

def pressButton(button_value):
    global expression       #to use the same global expression instead of local expression variable
    expression +=str(button_value)
    equation.set(expression)

def clearEntry():
    global expression
    expression=""
    equation.set("")

def backSpace():
    global expression
    expression=expression[:-1]   #python slicing syntax with general form:sequence[start:end:step]
    equation.set(expression)

def equalPress():
    global expression
    try:
        expression = str(numexpr.evaluate(expression))
        equation.set(expression)
    except:
        equation.set("Error!")
        expression=""

equation=tk.StringVar()        #StringVar() is a special Tkinter variable class that holds a string value and connects Python variables to Tkinter widgets
displayFrame=tk.Frame(root,bd=0,bg="#e0e5ec")
displayFrame.pack(pady=20)     #pady sets extra space on top and bottom of display
displayEntry=tk.Entry(displayFrame,textvariable=equation,font=("Helvetica", 24), bd=0, bg="#f0f0f0",justify="right",
                      relief="flat")  #right set text in right of entry field and relief defines how the border of a widget looks — flat means no border
displayEntry.pack(ipadx=8,ipady=15)  #iPad is just internal padding

def validateKey(event):
    allowedKeys="0123456789+-*/%.()"
    if event.char not in allowedKeys:
        return "break"    #ignores invalid key presses
    return None

displayEntry.bind("<KeyPress>",validateKey)  #<KeyPress> is a Tkinter event for key press
buttonFrame=tk.Frame(root,bg="#e0e5ec")
buttonFrame.pack()

#creating a list of list(2D list)
buttons=[
    ['C','(',')','+'],
    ['1','2','3','-'],
    ['4','5','6','*'],
    ['7','8','9','/'],
    ['.','0','←','=']
]

whiteButtonBG="#ffffff"
darkButtonBG="#1f1f2e"
redButtonBG="#ff4b5c"

for r,row in enumerate(buttons):
    for col,char in enumerate(row):
        if char=='C':
            btn=tk.Button(buttonFrame,text=char,fg="white",bg=redButtonBG,font=("Helvetica",18,"bold"),bd=0,width=5,
                          height=2,command=clearEntry)
        elif char=='←':
            btn=tk.Button(buttonFrame,text=char,fg="black",bg=whiteButtonBG,font=("Helvetica",18,"bold"),bd=0,width=5,
                          height=2,command=backSpace)
        elif char=='=':
            btn=tk.Button(buttonFrame,text=char,fg="white",bg=darkButtonBG,font=("Helvetica",18,"bold"),bd=0,width=5,
                          height=2,command=equalPress)
        else:
            buttonColor=whiteButtonBG if char.isdigit() or char =='.' or char == '←' else darkButtonBG
            btn = tk.Button(buttonFrame, text=char, fg="black" if buttonColor==whiteButtonBG else "white",bg=buttonColor
                            , font=("Helvetica", 18,), bd=0,width=5, height=2, command= lambda ch=char :pressButton(ch))
        btn.grid(row=r,column=col,padx=6,pady=6)

root.mainloop()