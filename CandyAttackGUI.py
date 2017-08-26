 from tkinter import *
import time
from Tower import Tower
from CandyCoordinates import Coordinates
from Enemys import Enemy#http://stackoverflow.com/questions/13215215/python-tkinter-animation
start_time = time.time()
grid = []
entitygrid=[]
level = 1
window = Tk() #creates gui
canvas = Canvas(window,bg="#e1ff89",height=950,width=950)
canvas.create_oval(11,11,41,41,fill="yellow")
for _ in range(2^level):
    entitygrid.append(Enemy("Circle",1,25,Coordinates(0,0)))
for row in range(20):
    for col in range(20):
        grid.append(canvas.create_rectangle(row*50,col*50,3,3))
def moveLeft(object):
    canvas.after(100,moveLeft)
    canvas.move(object,-1,0)
def moveRight(object):
    canvas.after(100,moveRight)
    canvas.move(object,1,0)
def moveForward(object):
    canvas.after(100,moveForward)
    canvas.move(object,0,-1)
canvas.pack()
#def redraw():
#    canvas.after(100,redraw)
#    canvas.move(e,0,1)
#canvas = Canvas(window,bg="#e1ff89",height=950,width=950,)
#image = PhotoImage(file="")
#coord = 10,50,240,210
##arc = canvas.create_arc(coord,start=0,extent=150,fill="red")
#e = canvas.create_oval(11,11,41,41,fill="yellow")
#for row in range(20):
#    for col in range(20):
#        grid.append(canvas.create_rectangle(row*50,col*50,3,3))
#canvas.pack()
#w = Text(master=window,bg="#c8a2f9")
#w.insert(INSERT, "helolowlwlw")
#w.pack()
#if CanMoveForward:

#redraw()
window.mainloop()
print("--- %s seconds ---" % (time.time() - start_time))
