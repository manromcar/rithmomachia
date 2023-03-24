from asyncio.windows_events import NULL
from contextlib import nullcontext
from gettext import NullTranslations
import tkinter

import machiaEngine
import os
from turtle import window_width


class App():
    def __init__(self,L_SQUARE,type,winpieces,points,digits):

        self.turn=True #TRUE is white, FALSE is black
        self.type=type #Dice el tipo de victoria que se desea
        self.L_SQUARE = L_SQUARE
        self.winpieces=winpieces
        self.winpoints=points
        self.windigits=digits
        self.path=os.path.dirname(__file__)
        self.images={}
        self.gs = machiaEngine.GameState()
        self.movement=machiaEngine.Move()
        self.pos=[0,0,0,0]
        self.premov=[]
        self.irregular=[]
        self.selected=NULL
        self.premoves=[]
        self.irregulars=[]
        self.deletedList=[]
        self.deleted=[]
        self.moved=False
        self.boardPieces=[]
        self.dpiece=""
        self.playing=True
        self.WPyramid=["WC_04","WT_09","WT_16","WS_25","WS_36","WC_01"]
        self.BPyramid=["BC_16","BT_25","BT_36","BS_49","BS_64"]
        self.WP=[2,15,91]#posición WP, valor
        self.BP=[8,2,190]#posición BP,valor
        winWidth = int(self.L_SQUARE*18)
        winHeight = int(self.L_SQUARE*16)
        self.window= tkinter.Tk()
        if self.type==0:
            title="Corpore"
            title2="  (Max pieces="+str(self.winpieces)+")"
        if self.type==1:
            title="Bonis"
            title2="  (Max points="+str(self.winpoints)+")"
        if self.type==2:
            title="Lite"
            title2="  (Max points="+str(self.winpoints)+", Max digits="+str(self.windigits)+")"
        if self.type==3:
            title="Honore"
            title2="  (Max pieces="+str(self.winpieces)+", Max points="+str(self.winpoints)+")"
        if self.type==4:
            title="Honore Litique"
            title2="  (Max pieces="+str(self.winpieces)+", Max points="+str(self.winpoints)+", Max digits= "+str(self.windigits)+")"
        if self.type==5:
            title="Magna"
            title2=""
        if self.type==6:
            title="Superior"
            title2=""
        if self.type==7:
            title="Excelentísima"
            title2=""
        self.window.title("Rithmomachia-"+title+title2)
        self.window.iconbitmap(default='./chess.ico')
        x_window = self.window.winfo_screenwidth() // 2 - winWidth // 2
        y_window = self.window.winfo_screenheight() // 2 - 4*winHeight // 7

        self.window.geometry(newGeometry=f"{str(winWidth)}x{str(winHeight)}+{x_window}+{y_window}")
        self.window.resizable(0,0)
        self.interface=tkinter.Canvas(self.window)
        self.interface.pack(fill=tkinter.BOTH,expand=True)

        playing=True







    def __call__(self):
        running=True

        self.interface.bind('<Button-1>', self.leftClick)
        self.window.mainloop()



    def board(self):
        self.interface.create_rectangle(0,0,5*self.L_SQUARE,16*self.L_SQUARE, fill="#734222")
        self.interface.create_rectangle(13*self.L_SQUARE,0,18*self.L_SQUARE,16*self.L_SQUARE, fill="#734222")
        for j in range(16):
            for i in range(13):
                if 4<i:
                    if (i+j)%2==0:
                        self.interface.create_rectangle(i*self.L_SQUARE,j*self.L_SQUARE,(i+1)*self.L_SQUARE,(j+1)*self.L_SQUARE, fill="#FBFAB8")
                    else:
                        self.interface.create_rectangle(i*self.L_SQUARE,j*self.L_SQUARE,(i+1)*self.L_SQUARE,(j+1)*self.L_SQUARE, fill="#3F3E29")
        
    def loadImages(self):
        pieces=["BC_03","BC_05","BC_07","BC_09","BC_25","BC_49","BC_81",
        "BC_02","BC_04","BC_06","BC_08","BC_16","BC_36","BC_64",
        "BS_15","BS_25","BS_45","BS_81","BS_153","BS_169","BS_289",
        "BT_06","BT_09","BT_20","BT_25","BT_42","BT_49","BT_72","BT_81",
        "BS_28","BS_49","BS_66","BS_120","BS_121","BS_225","BS_361",
        "BT_12","BT_16","BT_30","BT_36","BT_56","BT_64","BT_90","BT_100",
        "WC_02","WC_04","WC_06","WC_08","WC_16","WC_36","WC_64",
        "WC_03","WC_05","WC_07","WC_09","WC_25","WC_49","WC_81",
        "WS_28","WS_49","WS_66","WS_120","WS_121","WS_225","WS_361",
        "WT_12","WT_16","WT_30","WT_36","WT_56","WT_64","WT_90","WT_100",
        "WS_15","WS_25","WS_45","WS_81","WS_153","WS_169","WS_289",
        "WT_06","WT_09","WT_20","WT_25","WT_42","WT_49","WT_72","WT_81","BP","WP","BS_64","WC_01","WS_36"]
        directory=os.getcwd()
        directory.replace("\\","/")
        for piece in pieces:
            
            self.images[piece] = tkinter.PhotoImage(file=directory+"/images/"+ piece +".png")

    def showPieces(self):
        row=0
        rowB=15
        wcount=0
        bcount=0
        for p in self.boardPieces:
            self.interface.delete(p)

        for n_i, i in enumerate(self.gs.pieces):
            for n_j, j in enumerate(i):
                if j != "":
                    self.boardPieces.append(self.interface.create_image((n_j+5)*self.L_SQUARE,n_i*self.L_SQUARE,image=self.images[j], anchor="nw"))
        for n_d,d in enumerate(self.deleted):

            if d.startswith("W"):
                if (wcount==0)or(wcount%5!=0):
                    self.boardPieces.append(self.interface.create_image((wcount%5+13)*self.L_SQUARE,row*self.L_SQUARE,image=self.images[d], anchor="nw"))
                    wcount=wcount+1
                else:
                    row=row+1
                    self.boardPieces.append(self.interface.create_image((wcount%5+13)*self.L_SQUARE,row*self.L_SQUARE,image=self.images[d], anchor="nw"))
                    wcount=wcount+1
            elif d.startswith("B"):

                if (bcount==0)or(bcount%5!=0):
                    self.boardPieces.append(self.interface.create_image((bcount%5+13)*self.L_SQUARE,rowB*self.L_SQUARE,image=self.images[d], anchor="nw"))
                    bcount=bcount+1
                else:
                    rowB=rowB-1
                    self.boardPieces.append(self.interface.create_image((bcount%5+13)*self.L_SQUARE,rowB*self.L_SQUARE,image=self.images[d], anchor="nw"))
                    bcount=bcount+1
        for n_i, i in enumerate(self.BPyramid):
            self.boardPieces.append(self.interface.create_image(n_i*self.L_SQUARE,2*self.L_SQUARE,image=self.images[i], anchor="nw"))
        for n_i, i in enumerate(self.WPyramid):
            if n_i==5:
                self.boardPieces.append(self.interface.create_image(0*self.L_SQUARE,14*self.L_SQUARE,image=self.images[i], anchor="nw"))
            else:
                self.boardPieces.append(self.interface.create_image(n_i*self.L_SQUARE,15*self.L_SQUARE,image=self.images[i], anchor="nw"))

        tkinter.Label(self.window,text = self.BP[2]).place(x = self.L_SQUARE*2,y = self.L_SQUARE*3)
        tkinter.Label(self.window,text = self.WP[2]).place(x = self.L_SQUARE*2,y = self.L_SQUARE*14)














    def leftClick(self,event):
        if self.playing:    
            SquareX=(int)(event.x/self.L_SQUARE)-4
            SquareY=(int)(event.y/self.L_SQUARE)+1
            self.play(SquareX,SquareY)
            
    def play(self,SquareX,SquareY):
        #Se borra si se selecciona una pieza ya seleccionada se borra la selección yy premovimientos sin problemas

        if self.selected!=NULL:
            self.interface.delete(self.selected)
            for i in range(len(self.premoves)):
                self.interface.delete(self.premoves[i])
            for i in range(len(self.irregulars)):
                self.interface.delete(self.irregulars[i])

        if((self.pos[0]==SquareX) & (self.pos[1]==SquareY)):
            self.premov.clear()
            self.irregular.clear()
            self.pos[0]= 0
            self.pos[1]= 0
        elif SquareX>8 and SquareY<=8:
            if not self.turn:
                dpos=(SquareX-8)+(SquareY-1)*4
                self.selected = self.interface.create_rectangle((SquareX+4)*self.L_SQUARE,(SquareY-1)*self.L_SQUARE,(SquareX+5)*self.L_SQUARE,SquareY*self.L_SQUARE, fill="#FF7F50",stipple="gray75")
                for d in self.deleted:
                    if str(d).startswith("W"):
                        dpos=dpos-1
                        if dpos==0:
                            self.dpiece=d
        elif SquareX>8 and SquareY>8:
            if self.turn:
                dpos=(SquareX-8)+(16-SquareY)*4
                self.selected = self.interface.create_rectangle((SquareX+4)*self.L_SQUARE,(SquareY-1)*self.L_SQUARE,(SquareX+5)*self.L_SQUARE,SquareY*self.L_SQUARE, fill="#FF7F50",stipple="gray75")
                for d in self.deleted:
                    if str(d).startswith("B"):
                        dpos=dpos-1
                        if dpos==0:
                            self.dpiece=d



        else:
            self.pos[2]=self.pos[0]
            self.pos[3]=self.pos[1]
            self.pos[0]= SquareX
            self.pos[1]= SquareY
            i=0
            if self.dpiece.startswith("W") and self.gs.pieces[SquareY-1][SquareX-1]=="" and SquareY<=8:
                self.gs.pieces,self.deleted=self.movement.revive(self.pos,self.gs.pieces,self.deleted,self.dpiece)
                self.moved=True
                self.dpiece=""
                self.showPieces()
            elif self.dpiece.startswith("B") and self.gs.pieces[SquareY-1][SquareX-1]=="" and SquareY>8:
                self.gs.pieces,self.deleted=self.movement.revive(self.pos,self.gs.pieces,self.deleted,self.dpiece)
                self.moved=True
                self.dpiece=""
                self.showPieces()

            #si se ha seleccionado la casilla de un premovimiento se mueve la pieza

            while i<len(self.premov):
                if((self.pos[0]==self.premov[i])and(self.pos[1]==self.premov[i+1])):
                    
                    self.moved=True
                    for p in range(len(self.boardPieces)):
                        self.interface.delete(self.boardPieces[p])
                    self.gs.pieces=self.movement.move(self.pos,self.gs.pieces)
                    if self.pos[3]==self.WP[1] and self.pos[2]==self.WP[0]:

                        self.WP[0]=self.pos[0]
                        self.WP[1]=self.pos[1]
                    if self.pos[3]==self.BP[1] and self.pos[2]==self.BP[0]:

                        self.BP[0]=self.pos[0]
                        self.BP[1]=self.pos[1]

                    #ya se ha movido ahora se ve si se puedee capturar alguna pieza, empezando por las piramides completas, luego se mira por cada pieza de la pirmaide
                    
                    self.gs.pieces,self.deleted,self.WPyramid,self.BPyramid,self.WP,self.BP,self.deletedList=self.movement.pyramidCapture(self.pos,self.gs.pieces,self.deleted,self.WPyramid,self.BPyramid,self.WP,self.BP,self.deletedList)
                    
                    self.showPieces()
                i=i+2
                   
            j=0
            while j<len(self.irregular):
                if((self.pos[0]==self.irregular[j])&(self.pos[1]==self.irregular[j+1])):
                    
                    self.moved=True
                    for p in range(len(self.boardPieces)):
                        self.interface.delete(self.boardPieces[p])
                    self.gs.pieces=self.movement.move(self.pos,self.gs.pieces)
                    #Se elimina la pieza para que no pueda comer pues este es un movimiento irregular
                    prepiece=self.gs.pieces[self.pos[1]-1][self.pos[0]-1]
                    if self.gs.pieces[self.pos[1]-1][self.pos[0]-1].startswith("W"):
                        self.gs.pieces[self.pos[1]-1][self.pos[0]-1]="Wd"
                    if self.gs.pieces[self.pos[1]-1][self.pos[0]-1].startswith("B"):
                        self.gs.pieces[self.pos[1]-1][self.pos[0]-1]="Bd"
                    
                    if self.pos[3]==self.WP[1] and self.pos[2]==self.WP[0]:

                        self.WP[0]=self.pos[0]
                        self.WP[1]=self.pos[1]
                    if self.pos[3]==self.BP[1] and self.pos[2]==self.BP[0]:

                        self.BP[0]=self.pos[0]
                        self.BP[1]=self.pos[1]

                    
                    #ya se ha movido ahora se ve si se puedee capturar alguna pieza, empezando por las piramides completas, luego se mira por cada pieza de la pirmaide
                    self.gs.pieces,self.deleted,self.WPyramid,self.BPyramid,self.WP,self.BP,self.deletedList=self.movement.pyramidCapture(self.pos,self.gs.pieces,self.deleted,self.WPyramid,self.BPyramid,self.WP,self.BP,self.deletedList)
                    self.gs.pieces[self.pos[1]-1][self.pos[0]-1]=prepiece
                    self.showPieces()
                j=j+2
                
        #Se borran los premovimientos y se crea la selección
            self.premov.clear()
            self.premoves.clear()
            self.irregulars.clear()
            self.irregular.clear()
            self.selected = self.interface.create_rectangle((self.pos[0]+4)*self.L_SQUARE,(self.pos[1]-1)*self.L_SQUARE,(self.pos[0]+5)*self.L_SQUARE,self.pos[1]*self.L_SQUARE, fill="#FF7F50",stipple="gray75")
            
            #Se borra la selección si se ha movido
            if self.moved==True:
                self.turn= not self.turn
                self.interface.delete(self.selected)
                self.moved=False


                #Si no se ha movido se imprimen los posibles premovimientos de la ficha
            else:

                if str(self.gs.pieces[self.pos[1]-1][self.pos[0]-1]).startswith("W") and self.turn:
                    
                    self.premov=self.movement.premove(self.pos,self.gs.pieces,self.WPyramid)
                    
                    self.irregular=self.movement.preirregular(self.pos,self.gs.pieces,self.WPyramid)
                    
                    i=0
                    while i<len(self.premov):
                        if (0<self.premov[i]<9) & (0<self.premov[i+1]<17):
                            self.premoves.append(self.interface.create_rectangle((self.premov[i]+4)*self.L_SQUARE,(self.premov[i+1]-1)*self.L_SQUARE,(self.premov[i]+5)*self.L_SQUARE,self.premov[i+1]*self.L_SQUARE, fill="#FF7F50",stipple="gray50"))
                        i=i+2
                    j=0
                    while j<len(self.irregular):
                        if (0<self.irregular[j]<9) & (0<self.irregular[j+1]<17):
                            self.irregulars.append(self.interface.create_rectangle((self.irregular[j]+4)*self.L_SQUARE,(self.irregular[j+1]-1)*self.L_SQUARE,(self.irregular[j]+5)*self.L_SQUARE,self.irregular[j+1]*self.L_SQUARE, fill="#008000",stipple="gray50"))
                        j=j+2
                elif str(self.gs.pieces[self.pos[1]-1][self.pos[0]-1]).startswith("B") and not self.turn:
                    self.premov=self.movement.premove(self.pos,self.gs.pieces,self.BPyramid).copy()
                    self.irregular=self.movement.preirregular(self.pos,self.gs.pieces,self.WPyramid)
                    i=0
                    while i<len(self.premov):
                        if (0<self.premov[i]<9) & (0<self.premov[i+1]<17):
                            self.premoves.append(self.interface.create_rectangle((self.premov[i]+4)*self.L_SQUARE,(self.premov[i+1]-1)*self.L_SQUARE,(self.premov[i]+5)*self.L_SQUARE,self.premov[i+1]*self.L_SQUARE, fill="#FF7F50",stipple="gray50"))
                        i=i+2
                    j=0
                    while j<len(self.irregular):
                        if (0<self.irregular[j]<9) & (0<self.irregular[j+1]<17):
                            self.irregulars.append(self.interface.create_rectangle((self.irregular[j]+4)*self.L_SQUARE,(self.irregular[j+1]-1)*self.L_SQUARE,(self.irregular[j]+5)*self.L_SQUARE,self.irregular[j+1]*self.L_SQUARE, fill="#008000",stipple="gray50"))
        
                        j=j+2
        
        win=self.gs.win(self.type,self.winpieces,self.winpoints,self.windigits,self.gs.pieces,self.deletedList,self.WPyramid,self.BPyramid,self.WP,self.BP)
        if win is not NULL:
            if win is True:
                self.endgame("B")
            elif win is False:
                self.endgame("W")
            elif win is None:
                self.endgame("D")
        #soluciona un problema de imagen en la piramide
        del SquareX
        del SquareY

        return self

    def endgame(self,winner):
        self.playing=False
        top= tkinter.Toplevel(self.window)
        topWidth=200
        topHeight=100
        x_top = self.window.winfo_screenwidth() // 2 - topWidth // 2
        y_top = self.window.winfo_screenheight() // 2 - topHeight // 2

        top.geometry(newGeometry=f"{str(topWidth)}x{str(topHeight)}+{x_top}+{y_top}")
        top.resizable(0,0)
        top.geometry("200x100")
        top.title("Winner")
        if str(winner).startswith("W"):
            tkinter.Label(top, text= "\n      White WIN", font=('Times 18 bold')).grid(row=1,column=1)
        if str(winner).startswith("B"):
            tkinter.Label(top, text= "\n      Black WIN", font=('Times 18 bold')).grid(row=1,column=1)

    def quit(self):
        self.window.destroy()







                    

















    