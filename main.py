from functools import partial
from pickle import TRUE
import tkinter 
from turtle import left
import game

#Se crea la ventana tkinter
window= tkinter.Tk()
window.geometry("300x500")

#Defino la función que llama al tablero de juego

        
def defineValues(n):
        window.destroy()
        window2= tkinter.Tk()
        window2.geometry("400x150")
        window2.title("Choose values")
        if n==0:
                capNum=tkinter.IntVar()
                tkinter.Label(window2, text="Now we establish the pieces needed to be captured to win").grid(row=1,columnspan=2)
                tkinter.Label(window2,font=("Times bold",7), text="(We only accept Integer numbers bigger than 0, if a decimal number is \n used It would be replaced for the integer part only)").grid(row=7,columnspan=2)

                tkinter.Label(window2, text="Max pieces:").grid(row=2)
                e = tkinter.Entry(window2,textvariable=capNum)
                e.grid(row=2, column=1)
                print()
                isIntButton=tkinter.Button(window2,text="Corpore",font=("Times bold",12),command=lambda:IsInt(n,window2,capNum.get()),width=20)
                isIntButton.grid(row=3, column=1)
                window2.mainloop()
        if n==1:
                capNum=tkinter.IntVar()
                tkinter.Label(window2, text="Now we establish the points needed to be captured to win").grid(row=1,columnspan=2)
                tkinter.Label(window2,font=("Times bold",7), text="(We only accept Integer numbers bigger than 0, if a decimal number is \n used It would be replaced for the integer part only)").grid(row=7,columnspan=2)

                tkinter.Label(window2, text="Max points:").grid(row=2)
                e = tkinter.Entry(window2,textvariable=capNum)
                e.grid(row=2, column=1)
                isIntButton=tkinter.Button(window2,text="Bonis",font=("Times bold",12),command=lambda:IsInt(n,window2,0,capNum.get()),width=20)
                isIntButton.grid(row=3, column=1)
                window2.mainloop()
        if n==2:
                capNum=tkinter.IntVar()
                capNum2=tkinter.IntVar()
                tkinter.Label(window2, text="Now we establish the points and digits needed to be captured to win").grid(row=1,columnspan=2)
                tkinter.Label(window2,font=("Times bold",7), text="(We only accept Integer numbers bigger than 0, if a decimal number is \n used It would be replaced for the integer part only)").grid(row=7,columnspan=2)

                tkinter.Label(window2, text="Max points:").grid(row=2)
                e = tkinter.Entry(window2,textvariable=capNum)
                e.grid(row=2, column=1)
                tkinter.Label(window2, text="Max digits:").grid(row=3)
                e2 = tkinter.Entry(window2,textvariable=capNum2)
                e2.grid(row=3, column=1)
                isIntButton=tkinter.Button(window2,text="Lite",font=("Times bold",12),command=lambda:IsInt(n,window2,0,capNum.get(),capNum2.get()),width=20)
                isIntButton.grid(row=4, column=1)
                window2.mainloop()
        if n==3:
                capNum=tkinter.IntVar()
                capNum2=tkinter.IntVar()
                tkinter.Label(window2, text="Now we establish the points and pieces needed to be captured to win").grid(row=1,columnspan=2)
                tkinter.Label(window2,font=("Times bold",7), text="(We only accept Integer numbers bigger than 0, if a decimal number is \n used It would be replaced for the integer part only)").grid(row=7,columnspan=2)

                tkinter.Label(window2, text="Max pieces:").grid(row=2)
                e = tkinter.Entry(window2,textvariable=capNum)
                e.grid(row=2, column=1)
                tkinter.Label(window2, text="Max points:").grid(row=3)
                e2 = tkinter.Entry(window2,textvariable=capNum2)
                e2.grid(row=3, column=1)
                isIntButton=tkinter.Button(window2,text="Honore",font=("Times bold",12),command=lambda:IsInt(n,window2,capNum.get(),capNum2.get()),width=20)
                isIntButton.grid(row=4, column=1)
                window2.mainloop()
        if n==4:
                capNum=tkinter.IntVar()
                capNum2=tkinter.IntVar()
                capNum3=tkinter.IntVar()
                tkinter.Label(window2, text="Now we establish the points, pieces and digits needed to be captured to win").grid(row=1,columnspan=2)
                tkinter.Label(window2,font=("Times bold",7), text="(We only accept Integer numbers bigger than 0, if a decimal number is \n used It would be replaced for the integer part only)").grid(row=7,columnspan=2)

                tkinter.Label(window2, text="Max pieces:").grid(row=2)
                e = tkinter.Entry(window2,textvariable=capNum)
                e.grid(row=2, column=1)
                tkinter.Label(window2, text="Max points:").grid(row=3)
                e2 = tkinter.Entry(window2,textvariable=capNum2)
                e2.grid(row=3, column=1)
                tkinter.Label(window2, text="Max digits:").grid(row=4)
                e3 = tkinter.Entry(window2,textvariable=capNum3)
                e3.grid(row=4, column=1)
                isIntButton=tkinter.Button(window2,text="Honore Litique",font=("Times bold",12),command=lambda:IsInt(n,window2,capNum.get(),capNum2.get(),capNum3.get()),width=20)
                isIntButton.grid(row=5, column=1)
                window2.mainloop()
        
def IsInt(n,win,pieces=0,points=0,digits=0):
        if pieces>0 and points>0 and digits>0 and n==4:
                playMachia(win,n,pieces,points,digits)
        elif points>0 and pieces>0 and n==3:
                playMachia(win,n,pieces,points)
        elif points>0 and digits>0 and n==2:
                playMachia(win,n,0,points,digits)
        elif points>0 and n==1:
                playMachia(win,n,0,points)
        elif pieces>0 and n==0:
                playMachia(win,n,pieces)
        else:
                print("false")
def playMachia(win,n,pieces=0,points=0,digits=0):
        
        win.destroy()
        Engine=game.App(40,n,pieces,points,digits)
        Engine.board()
        Engine.loadImages()
        Engine.showPieces()
        Engine()
window.title("Rithmomachia")
interface=tkinter.Canvas(window)
interface.pack(fill=tkinter.BOTH,expand=True)
corporeButton=tkinter.Button(window,text="Corpore",font=("Times bold",12),command=lambda:defineValues(0),width=20)
bonisButton=tkinter.Button(window,text="Bonis",font=("Times bold",12),command=lambda:defineValues(1),width=20)
liteButton=tkinter.Button(window,text="Lite",font=("Times bold",12),command=lambda:defineValues(2),width=20)
honoreButton=tkinter.Button(window,text="Honore",font=("Times bold",12),command=lambda:defineValues(3),width=20)
honoreLitiqueButton=tkinter.Button(window,text="Honore Litique",font=("Times bold",12),command=lambda:defineValues(4),width=20)
magnaButton=tkinter.Button(window,text="Magna",font=("Times bold",12),command=lambda:playMachia(window,5),width=20)
superiorButton=tkinter.Button(window,text="Superior",font=("Times bold",12),command=lambda:playMachia(window,6),width=20)
excelentisimaButton=tkinter.Button(window,text="Excelentísima",font=("Times bold",12),command=lambda:playMachia(window,7),width=20)

corporeButton.pack(ipadx=1,ipady=5)
corporeButton.place(rely=0.4,relx=0.175)
bonisButton.pack(ipadx=0.4,ipady=5)
bonisButton.place(rely=0.47,relx=0.175)
liteButton.pack(ipadx=0.4,ipady=5)
liteButton.place(rely=0.54,relx=0.175)
honoreButton.pack(ipadx=0.4,ipady=5)
honoreButton.place(rely=0.61,relx=0.175)
honoreLitiqueButton.pack(ipadx=0.4,ipady=5)
honoreLitiqueButton.place(rely=0.68,relx=0.175)
magnaButton.pack(ipadx=0.4,ipady=5)
magnaButton.place(rely=0.75,relx=0.175)
superiorButton.pack(ipadx=0.4,ipady=5)
superiorButton.place(rely=0.82,relx=0.175)
excelentisimaButton.pack(ipadx=0.4,ipady=5)
excelentisimaButton.place(rely=0.89,relx=0.175)
window.mainloop()

    
   



