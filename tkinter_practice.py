import tkinter
import tkinter.ttk as tk

master = tkinter.Tk()
master.geometry("175x175")

v = tkinter.StringVar(master, "1")

values = {
        "RadioButton 1" : "1", 
        "RadioButton 2" : "2", 
        "RadioButton 3" : "3", 
        "RadioButton 4" : "4", 
        "RadioButton 5" : "5"} 

for (text, value) in values.items():
    tk.Radiobutton(master, text = text, variable = v, 
    value = value).pack(fill = tkinter.X, ipady = 5)

tkinter.mainloop()
    



