from functools import partial
from pickle import TRUE
import tkinter
from turtle import left 

#Se crea la ventana tkinter
window= tkinter.Tk()

#Defino la función que llama al tablero de juego
def playMachia():
        window.destroy()
        import game


window.title("Rithmomachia")
interface=tkinter.Canvas(window)
interface.pack(fill=tkinter.BOTH,expand=True)
gameButton=tkinter.Button(window,text="Let's play",font=("Times bold",12),command=playMachia)

gameButton.place(relx=0.4,rely=0.1)
window.mainloop()

    
   



