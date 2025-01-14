from tkinter import*
#creating gui window
screen = Tk()
screen.geometry("800x500")
screen.config(background="red")
#button element
button = Button(screen, text = "press",bd="1",background="green",command=screen.destroy)
button.pack(side="bottom")
#label element
label = Label(screen, text = "i am a label").place(x=125, y=235)
#entry box
write = Entry(screen, width=50).place(x=125,y=300)
screen.mainloop()
