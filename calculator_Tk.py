from tkinter import *

# Creating calculator fram

def calc(source, side):
    storeObj = Frame(source, borderwidth = 4, bd =4, bg = 'orange')
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj

# Create Button
def button(source, side, text, command =None):
    storeObj = Button(source, text = text, command =command)
    storeObj.pack(side =side, expand = YES, fill = BOTH)
    return storeObj

class app(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill = BOTH)
        self.master.title('Calculator')

    # Display widget

        display = StringVar()
        Entry(self, relief =RIDGE, textvariable = display, justify = 'right',
            bd = 30, bg = 'darkorange').pack(side = TOP, expand = YES, fill = BOTH)

    # Clear Button Widget

        for eraseButton in (['C']):
            erase = calc(self, TOP)
            for ichar in eraseButton:
                button(erase, LEFT, ichar, lambda
                storeObj = display, q = ichar : storeObj.set(''))

    # Add numbers and symbols to widget
        for numButton in ('789/', '456*','123-',"0.+"):
            function_Num = calc(self, TOP)
            for iEquals in numButton:
                button(function_Num, LEFT, iEquals, lambda
                storeObj = display, q = iEquals:
                storeObj.set(storeObj.get() + q))

    # Add Equal Button
        EqualButton = calc(self, TOP)
        for iEquals in '=':
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)

                btniEquals.bind('ButtonRelease-1', lambda s =self,
                    storeObj = display: s.calc(storeObj), '+')

            else:
                btniEquals = button(EqualButton, LEFT, iEquals, lambda
                     storeObj = display, s = '%s' % iEquals:
                     storeObj.set(storeObj.get() + s))

    #Apply trigger on wedgets
        def calcu(self,display):
            try:
                display.set(eval(display.get()))
            except:
                display.set('ERROR')




# Start GUI
if __name__=='__main__':
    app().mainloop()
