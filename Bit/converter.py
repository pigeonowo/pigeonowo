from toBit import toBitConvert
from toDeci import toDeciConvert
import re
from tkinter import *
from tkinter import ttk

# vars and defs
outcomeNumber = ""
yourNumber = 0
convertFrom = ''
convertTo = ''

def convertFromDef(selection):
    convertFrom = variableFrom.get()
    return convertFrom              
                                                                    
                                                                    
def conversion():
    outcomeLabelfake = Entry()
    outcomeLabelfake.grid(column=1, row=1)  #### so that outputs dont overlap
    convertTo = variable.get()
    convertFrom = variableFrom.get() 
    if re.search("^[0-9ABCDEF]*$", entryYou.get()):   
        yourNumber = int(entryYou.get())              
        if convertTo == "Bit":                                                                     
            labelnum = toBitConvert(convertFrom, yourNumber)
            outcomeLabel = ttk.Label(text=labelnum).grid(column=1, row=1)
        if convertTo == "Decimal":
            print("Decimal")
            labelnum = toDeciConvert(convertFrom, yourNumber)
            outcomeLabel = ttk.Label(text=labelnum).grid(column=1, row=1)
        #if To == "Hexa":
        #    print("Hexa")
        #    labelnum = outcomeNumber
        #    ttk.Label(text=labelnum).grid(column=1, row=1)
    else:
        outcomeNumber = "This is not a number"
        labelnum = outcomeNumber
        ttk.Label(text=labelnum).grid(column=1, row=1)
    

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid(rowspan=2)
root.geometry("375x100")
root.title('Converter')

############ ENTER #############



# label
ttk.Label(text="Your Unit and Number:  ").grid(column=0, row=0)

# entry
entryYou = Entry()
entryYou.grid(column=1, row=0)

# choice button
choices = ['Bit', 'Decimal', 'Hexa']
variableFrom = StringVar(root)
variableFrom.set('choose')
Option = OptionMenu(root, variableFrom, *choices)
Option.grid(column=2, row=0,)





############### OUTCOME ################



# label
ttk.Label(text="Outcome:").grid(column=0, row=1)

# outcome Label
outcomeLabelfake = Entry()
outcomeLabelfake.grid(column=1, row=1)

# choice button OUTCOME
choices = ['Bit', 'Decimal', 'Hexa']
variable = StringVar(root)
variable.set('choose')
OptionOutcome = OptionMenu(root, variable, *choices)
OptionOutcome.grid(column=2, row=1)

####### CONVERT BUTTON #######

# button
ttk.Button(text="Convert", command=lambda : conversion(), ).grid(column=1, row= 3)

root.mainloop()