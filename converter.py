from tkinter import*
screen = Tk()
screen.geometry("300x100")

#function for conversion
def convert():
    gramconv = float(wkg.get())*1000
    poundsconv = float(wkg.get())*2.20462
    ounceconv = float(wkg.get())*35.274
    #deleting previous imputs
    tgrams.delete("1.0",END)
    tgrams.insert(END, gramconv)
    tpounds.delete("1.0",END)
    tpounds.insert(END, poundsconv)
    tounces.delete("1.0",END)
    tounces.insert(END, ounceconv)


#creating lables
heading = Label(screen,text="Enter weight in KG")
wkg = StringVar()
kg = Entry(screen,width=15,textvariable=wkg)
button = Button(screen,width=8,text="CONVERT",command=convert)
grams = Label(screen,text="grams")
tgrams = Text(screen,height=1,width=10)
pounds = Label(screen,text="pounds")
tpounds = Text(screen,height=1,width=10)
ounces = Label(screen,text="ounces")
tounces = Text(screen,height=1,width=10)

#grid method
heading.grid(row=0,column=0)
kg.grid(row=0,column=1)
button.grid(row=0,column=2)
grams.grid(row=1,column=0)
pounds.grid(row=1,column=1)
ounces.grid(row=1,column=2)
tgrams.grid(row=2,column=0)
tounces.grid(row=2,column=2)
tpounds.grid(row=2,column=1)


screen.mainloop()
