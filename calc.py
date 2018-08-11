#calculator#

from tkinter import*

def iCalc(source ,side):
    storeObj = Frame(source,borderwidth=2,bd=2,bg="powder blue")
    storeObj.pack(side=side,expand=YES,fill=BOTH)
    return storeObj

def button(source,side,text,command=None):
    storeObj = Button(source,text=text,command=command)
    storeObj.pack(side=side,expand=YES,fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('Font','arial 10 bold')
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Calculator")

        display=StringVar()
        Entry(self,relief=RIDGE,textvariable=display,justify='right',bd=20,bg="powder blue").pack(side=TOP,expand=YES,fill=BOTH)


        #we can use ridge,flat,raise,sunken,groove

        for clearBut in(["CE"],["C"]):
            erase=iCalc(self,TOP)
            for ichar in clearBut:
                button(erase,LEFT,ichar,lambda storeObj=display,q=ichar:storeObj.set(''))

        for NumBut in ("789/","456*","123-","0.+"):
            FunctionNum=iCalc(self,TOP)
            for iEquals in NumBut:
                button(FunctionNum,LEFT,iEquals,lambda storeObj=display,q=iEquals:storeObj.set(storeObj.get()+q))
                          

        EqualsButton=iCalc(self,TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals=button(EqualsButton,LEFT,iEquals)
                btniEquals.bind('<ButtonRelease-1>',lambda e,s=self,storeObj=display:s.calc(storeObj),'+')
            else:
                btniEquals=button(EqualsButton,LEFT,iEquals,lambda storeObj=display,s='%s'%iEquals:storeObj.set(storeObj.get()+s))


    def calc(self,display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("Error")

if __name__ == "__main__":
    app().mainloop()
