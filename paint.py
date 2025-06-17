from tkinter import *
from tkinter.colorchooser import askcolor

#class for paint object
class paint(object):
    size = 5.0
    startcolor = "black"
    def __init__(self):
        self.screen = Tk()
        self.pen = Button(self.screen,text="pen",command=self.usepen)
        self.pen.grid(row=0,column=0)
        self.brush = Button(self.screen,text="brush",command=self.funbrush)
        self.brush.grid(row=0,column=1)
        self.bcolor = Button(self.screen,text="color",command=self.funcolor)
        self.bcolor.grid(row=0,column=2)
        self.eraser = Button(self.screen,text="eraser",command=self.funeraser)
        self.eraser.grid(row=0,column=3)
        self.size = Scale(self.screen,from_=1,to=10,orient=HORIZONTAL)
        self.size.grid(row=0,column=4)
        self.canvas = Canvas(self.screen,bg="white",width=500,height=400)
        self.canvas.grid(row=1,columnspan=5)
        self.setup()
        self.screen.mainloop()
    def setup(self):
        self.oldx = None
        self.oldy = None
        self.linewidth = self.size.get()
        self.color = self.startcolor
        self.eraseron = False
        self.active_button = self.pen
        self.canvas.bind("<B1-Motion>",self.painting)
        self.canvas.bind("<ButtonRelease-1>",self.reset)
    def funcolor(self):
        self.eraseron = False
        self.color = askcolor(color=self.color)[1]

    def currentbutton(self,button,eraser_mode=False):
        self.active_button.config(relief = RAISED)
        button.config(relief = SUNKEN)
        self.active_button=button
        self.eraseron = eraser_mode
    def usepen(self):
        self.currentbutton(self.pen)
    def funbrush(self):
        self.currentbutton(self.brush)
        self.linewidth = self.size.get()*2
    def funeraser(self):
        self.currentbutton(self.eraser,eraser_mode=True)
    def painting(self,event):
        #self.linewidth=self.size.get()
        s=self.size.get()
        if self.currentbutton == self.brush:
            self.linewidth = s*2
        else:
            self.linewidth = s
        paintcolor = "white" if self.eraseron else self.color
        if self.oldx and self.oldy:
            self.canvas.create_line(self.oldx,self.oldy,event.x,event.y,width=self.linewidth,fill=paintcolor,capstyle=ROUND,smooth=TRUE,splinesteps=36)
        self.oldx=event.x 
        self.oldy=event.y
    def reset(self,event):
        self.oldx,self.oldy = None,None
if __name__ == '__main__':
    paint()
