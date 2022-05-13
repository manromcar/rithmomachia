from asyncio.windows_events import NULL
from operator import truediv
from pickle import TRUE
from tkinter import W
import copy


class GameState():
    def __init__(self) :
        self.pieces=[
            ["BS_49","BS_121","","","","","BS_225","BS_361"],
            ["BS_28","BS_66","BT_36","BT_30","BT_56","BT_64","BS_120","BP"],
            ["BT_16","BT_12","BC_09","BC_25","BC_49","BC_81","BT_90","BT_100"],
            ["","","BC_03","BC_05","BC_07","BC_09","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","WC_08","WC_06","WC_04","WC_02","",""],
            ["WT_81","WT_72","WC_64","WC_36","WC_16","WC_04","WT_06","WT_09"],
            ["WS_153","WP","WT_49","WT_42","WT_20","WT_25","WS_45","WS_15"],
            ["WS_289","WS_169","","","","","WS_81","WS_25"],
            ]
        self.moveLog=[]
    
            



class Move():
    
    def premove(self,pos,pieces,pyramid):
        self.premov=[]
        piece=str(pieces[pos[1]-1][pos[0]-1])
        if piece=="":
            return self.premov
        
        elif piece.startswith("W") or piece.startswith("B"):
            
            newPiece=piece[1:]
            if  newPiece.startswith("P"):
                C=True
                T=True
                S=True
                qieces=copy.deepcopy(pieces)
                for p in pyramid:
                    q=p[1:]
                    
                    if C and q.startswith("C"):
                        qieces[pos[1]-1][pos[0]-1]=p
                        self.premov=self.premov+self.premove(pos,qieces,pyramid)
                        C=False
                    elif T and q.startswith("T"):
                        qieces[pos[1]-1][pos[0]-1]=p
                        self.premov=self.premov+self.premove(pos,qieces,pyramid)
                        T=False
                    elif S and q.startswith("S"):
                        qieces[pos[1]-1][pos[0]-1]=p
                        self.premov=self.premov+self.premove(pos,qieces,pyramid)
                        S=False


            elif newPiece.startswith("C"):
                if (0<=pos[0]-2<8) & (0<=pos[1]<16):
                    if pieces[pos[1]][pos[0]-2]=="":
                        self.premov.append(pos[0]-1)
                        self.premov.append(pos[1]+1)
                if (0<=pos[0]-2<8) & (0<=pos[1]-2<16):
                    if pieces[pos[1]-2][pos[0]-2]=="":
                        self.premov.append(pos[0]-1)
                        self.premov.append(pos[1]-1)
                if (0<=pos[0]<8) & (0<=pos[1]-2<16):
                    if pieces[pos[1]-2][pos[0]]=="":
                        self.premov.append(pos[0]+1)
                        self.premov.append(pos[1]-1)
                if (0<=pos[0]<8) & (0<=pos[1]<16):
                    if pieces[pos[1]][pos[0]]=="":
                        self.premov.append(pos[0]+1)
                        self.premov.append(pos[1]+1)
            
            elif newPiece.startswith("T"):
                if (0<=pos[0]-3<8) & (0<=pos[1]-1<16):
                    if ((pieces[pos[1]-1][pos[0]-3]=="")&(pieces[pos[1]-1][pos[0]-2]=="")):
                        self.premov.append(pos[0]-2)
                        self.premov.append(pos[1])
                if (0<=pos[0]-1<8) & (0<=pos[1]-3<16):
                    if ((pieces[pos[1]-3][pos[0]-1]=="")&(pieces[pos[1]-2][pos[0]-1]=="")):
                        self.premov.append(pos[0])
                        self.premov.append(pos[1]-2)
                if (0<=pos[0]+1<8) & (0<=pos[1]-1<16):
                    if ((pieces[pos[1]-1][pos[0]+1]=="")&(pieces[pos[1]-1][pos[0]]=="")):
                        self.premov.append(pos[0]+2)
                        self.premov.append(pos[1])
                if (0<=pos[0]-1<8) & (0<=pos[1]+1<16):
                    if ((pieces[pos[1]+1][pos[0]-1]=="") & (pieces[pos[1]][pos[0]-1]=="")):
                        self.premov.append(pos[0])
                        self.premov.append(pos[1]+2)
            elif newPiece.startswith("S"):
                if (0<=pos[0]-4<8) & (0<=pos[1]-1<16):
                    if ((pieces[pos[1]-1][pos[0]-4]=="")&(pieces[pos[1]-1][pos[0]-3]=="")&(pieces[pos[1]-1][pos[0]-2]=="")):
                        self.premov.append(pos[0]-3)
                        self.premov.append(pos[1])
                if (0<=pos[0]-1<8) & (0<=pos[1]-4<16):
                    if ((pieces[pos[1]-4][pos[0]-1]=="")&(pieces[pos[1]-3][pos[0]-1]=="")&(pieces[pos[1]-2][pos[0]-1]=="")):
                        self.premov.append(pos[0])
                        self.premov.append(pos[1]-3)
                if (0<=pos[0]+2<8) & (0<=pos[1]-1<16):
                    if ((pieces[pos[1]-1][pos[0]+2]=="")&(pieces[pos[1]-1][pos[0]+1]=="")&(pieces[pos[1]-1][pos[0]]=="")):
                        self.premov.append(pos[0]+3)
                        self.premov.append(pos[1])
                if (0<=pos[0]-1<8) & (0<=pos[1]+2<16):
                    if ((pieces[pos[1]+2][pos[0]-1]=="")&(pieces[pos[1]+1][pos[0]-1]=="") & (pieces[pos[1]][pos[0]-1]=="")):
                        self.premov.append(pos[0])
                        self.premov.append(pos[1]+3)
        return self.premov   
    def preirregular(self,pos,pieces,pyramid):
        self.irregular=[]
        piece=str(pieces[pos[1]-1][pos[0]-1])
        print(pieces[pos[1]-1][pos[0]-1])
        if piece=="":
            return self.irregular
        
        elif piece.startswith("W") or piece.startswith("B"):
            newPiece=piece[1:]
            if  newPiece.startswith("P"):
                C=True
                T=True
                S=True
                qieces=copy.deepcopy(pieces)
                for p in pyramid:
                    q=p[1:]
                    if T and q.startswith("T"):
                        qieces[pos[1]-1][pos[0]-1]=p
                        self.irregular=self.irregular+self.preirregular(pos,qieces,pyramid)
                        T=False
                    elif S and q.startswith("S"):
                        qieces[pos[1]-1][pos[0]-1]=p
                        self.irregular=self.irregular+self.preirregular(pos,qieces,pyramid)
                        S=False
            
            elif newPiece.startswith("T"):
                if (0<=pos[0]-3<8) & (0<=pos[1]-2<16):
                    if (pieces[pos[1]-2][pos[0]-3]==""):
                        self.irregular.append(pos[0]-2)
                        self.irregular.append(pos[1]-1)
                if (0<=pos[0]-3<8) & (0<=pos[1]<16):
                    if (pieces[pos[1]][pos[0]-3]==""):
                        self.irregular.append(pos[0]-2)
                        self.irregular.append(pos[1]+1)
                if (0<=pos[0]<8) & (0<=pos[1]-3<16):
                    if (pieces[pos[1]-3][pos[0]]==""):
                        self.irregular.append(pos[0]+1)
                        self.irregular.append(pos[1]-2)
                if (0<=pos[0]-2<8) & (0<=pos[1]-3<16):
                    if (pieces[pos[1]-3][pos[0]-2]==""):
                        self.irregular.append(pos[0]-1)
                        self.irregular.append(pos[1]-2)
                if (0<=pos[0]+1<8) & (0<=pos[1]-2<16):
                    if (pieces[pos[1]-2][pos[0]+1]==""):
                        self.irregular.append(pos[0]+2)
                        self.irregular.append(pos[1]-1)
                if (0<=pos[0]+1<8) & (0<=pos[1]<16):
                    if (pieces[pos[1]][pos[0]+1]==""):
                        self.irregular.append(pos[0]+2)
                        self.irregular.append(pos[1]+1)
                if (0<=pos[0]-2<8) & (0<=pos[1]+1<16):
                    if (pieces[pos[1]+1][pos[0]-2]=="") :
                        self.irregular.append(pos[0]-1)
                        self.irregular.append(pos[1]+2)
                if (0<=pos[0]<8) & (0<=pos[1]+1<16):
                    if (pieces[pos[1]+1][pos[0]]==""):
                        self.irregular.append(pos[0]+1)
                        self.irregular.append(pos[1]+2)
            elif newPiece.startswith("S"):
                if (0<=pos[0]-4<8) & (0<=pos[1]-2<16):
                    if (pieces[pos[1]-2][pos[0]-4]==""):
                        self.irregular.append(pos[0]-3)
                        self.irregular.append(pos[1]-1)
                if (0<=pos[0]-4<8) & (0<=pos[1]<16):
                    if (pieces[pos[1]][pos[0]-4]==""):
                        self.irregular.append(pos[0]-3)
                        self.irregular.append(pos[1]+1)
                if (0<=pos[0]-2<8) & (0<=pos[1]-4<16):
                    if (pieces[pos[1]-4][pos[0]-2]==""):
                        self.irregular.append(pos[0]-1)
                        self.irregular.append(pos[1]-3)
                if (0<=pos[0]<8) & (0<=pos[1]-4<16):
                    if (pieces[pos[1]-4][pos[0]]==""):
                        self.irregular.append(pos[0]+1)
                        self.irregular.append(pos[1]-3)
                if (0<=pos[0]+2<8) & (0<=pos[1]-2<16):
                    if (pieces[pos[1]-2][pos[0]+2]==""):
                        self.irregular.append(pos[0]+3)
                        self.irregular.append(pos[1]-1)
                if (0<=pos[0]+2<8) & (0<=pos[1]<16):
                    if (pieces[pos[1]][pos[0]+2]==""):
                        self.irregular.append(pos[0]+3)
                        self.irregular.append(pos[1]+1)
                if (0<=pos[0]-2<8) & (0<=pos[1]+2<16):
                    if (pieces[pos[1]+2][pos[0]-2]==""):
                        self.irregular.append(pos[0]-1)
                        self.irregular.append(pos[1]+3)
                if (0<=pos[0]<8) & (0<=pos[1]+2<16):
                    if (pieces[pos[1]+2][pos[0]]==""):
                        self.irregular.append(pos[0]+1)
                        self.irregular.append(pos[1]+3)
        return self.irregular 
    def move(self,pos,pieces):
        
        piece=str(pieces[pos[3]-1][pos[2]-1])
        pieces[pos[3]-1][pos[2]-1]=""
        pieces[pos[1]-1][pos[0]-1]=piece
        return pieces
    def revive(self,pos,pieces,deleted,dpiece):
        dpiece=str(dpiece)
        deleted.remove(dpiece)
        if dpiece.startswith("W"):
            dpiece="B"+dpiece[1:]
        else:
            dpiece="W"+dpiece[1:]
            
        pieces[pos[1]-1][pos[0]-1]=dpiece


        return pieces,deleted  
    def pyramidCapture(self,pos,pieces,deleted,WPyramid,BPyramid,WP,BP):
        d=False
        temp=""
        if WPyramid!=[] and BPyramid!=[]:
            #mira primero si se puede eliminar la piramide entera
            pieces[WP[1]-1][WP[0]-1]="WP_"+str(WP[2])
            pieces[BP[1]-1][BP[0]-1]="BP_"+str(BP[2])
            if pieces[pos[1]-1][pos[0]-1].startswith("Wd") or pieces[pos[1]-1][pos[0]-1].startswith("Bd"):
                d=True
                temp=pieces[pos[1]-1][pos[0]-1]
            pieces,deleted=self.canCapture(pos,pieces,deleted,WPyramid,BPyramid)
            if d:
                d=False
                pieces[pos[1]-1][pos[0]-1]=temp
            if pieces[WP[1]-1][WP[0]-1]!="":
                pieces[WP[1]-1][WP[0]-1]="WP"
            else:
                WPyramid=[]
                pieces[WP[1]-1][WP[0]-1]="d"
                BP[2]=0
                removed=True
            if pieces[BP[1]-1][BP[0]-1]!="":
                pieces[BP[1]-1][BP[0]-1]="BP"
            else:
                BPyramid=[] 
                pieces[BP[1]-1][BP[0]-1]="d"
                BP[2]=0
                removed=True

        if WPyramid==[] and BPyramid!=[] and not removed:
            pieces[BP[1]-1][BP[0]-1]="BP_"+str(BP[2])
            pieces,deleted=self.canCapture(pos,pieces,deleted,WPyramid,BPyramid)
            if pieces[BP[1]-1][BP[0]-1]!="":
                pieces[BP[1]-1][BP[0]-1]="BP"
            else:
                BPyramid=[]
                pieces[BP[1]-1][BP[0]-1]="d"
                BP[2]=0
                removed=True
        if WPyramid!=[] and BPyramid==[] and not removed:
            pieces[WP[1]-1][WP[0]-1]="WP_"+str(WP[2])
            pieces,deleted=self.canCapture(pos,pieces,deleted,WPyramid,BPyramid)
            if pieces[WP[1]-1][WP[0]-1]!="":
                pieces[WP[1]-1][WP[0]-1]="WP"
            else:
                WPyramid=[]
                pieces[WP[1]-1][WP[0]-1]="d"
                WP[2]=0
                removed=True 

            
        #Vamos a dividir los 4 casos posibles Hay piramide blnca pero no negra, hay negra pero no blanca, no hay ninguna o hay las dos
        if WPyramid==[] and BPyramid==[] and not removed:
            pieces,deleted=self.canCapture(pos,pieces,deleted,WPyramid,BPyramid)
        #aqui no se pone removed porque se puede dar el caso en el que se haya eliminado una piramide pero la otra pueda comer algo mas por eso se ha sustituido el sitio de las piramides por en vez de un espacio vacio por una d
        if WPyramid==[] and BPyramid!=[]:
            for q in BPyramid:
                    #poner que se sustituya p  en la posicion wp 
                pieces[BP[1]-1][BP[0]-1]=q
                pieces,deleted=self.canCapture(pos,pieces,deleted,WPyramid,BPyramid)
                if pieces[BP[1]-1][BP[0]-1]!=q:
                    BPyramid.remove(q)
                    deleted.remove(q)
                    BP[2]=BP[2]-int(q[q.index("_")+1:])
                    if BPyramid==[]:
                        pieces[BP[1]-1][BP[0]-1]="d"
            
        if WPyramid!=[] and BPyramid==[]:
            
            for p in WPyramid:
                    #poner que se sustituya p  en la posicion wp 
                pieces[WP[1]-1][WP[0]-1]=p
                pieces,deleted=self.canCapture(pos,pieces,deleted,WPyramid,BPyramid)
                if pieces[WP[1]-1][WP[0]-1]!=p:
                    WPyramid.remove(p)
                    deleted.remove(p)
                    WP[2]=self.WP[2]-int(p[p.index("_")+1:])
                    if WPyramid==[]:
                        pieces[WP[1]-1][WP[0]-1]="d"
        if WPyramid!=[] and BPyramid!=[]:                        
            for p in WPyramid:
                    #poner que se sustituya p y q en la posicion wp y bp
                pieces[WP[1]-1][WP[0]-1]=p

                for q in BPyramid:
                    pieces[BP[1]-1][BP[0]-1]=q
                    if pieces[pos[1]-1][pos[0]-1].startswith("Wd") or pieces[pos[1]-1][pos[0]-1].startswith("Bd"):
                        d=True
                        temp=pieces[pos[1]-1][pos[0]-1]
                    pieces,deleted=self.canCapture(pos,pieces,deleted,WPyramid,BPyramid)
                    if d:
                        d=False
                        pieces[pos[1]-1][pos[0]-1]=temp
                    #mira si alguna pieza de la piramide se ha eliminado y la quita de la lista a la vez que la quista de la lista de piezas eliminadas
                    
                    if pieces[BP[1]-1][BP[0]-1]!=q:
                        BPyramid.remove(q)
                        deleted.remove(q)
                        BP[2]=BP[2]-int(q[q.index("_")+1:])
                        if BPyramid==[]:
                            pieces[BP[1]-1][BP[0]-1]="d"
                if pieces[WP[1]-1][WP[0]-1]!=p:
                    WPyramid.remove(p)
                    deleted.remove(p)
                    WP[2]=WP[2]-int(p[p.index("_")+1:])
                    if WPyramid==[]:
                        pieces[WP[1]-1][WP[0]-1]="d"
        
    #Para que no aparezca la ultima iteración como la pieza en el tablero se establece que siemre aparece la piramide siempre y cuando esta no esté vacía
        if WPyramid!=[]:
            pieces[WP[1]-1][WP[0]-1]="WP"
        else:
            pieces[WP[1]-1][WP[0]-1]=""
        if BPyramid!=[]:
            pieces[BP[1]-1][BP[0]-1]="BP"
        else:
            pieces[BP[1]-1][BP[0]-1]=""
        return pieces,deleted,WPyramid,BPyramid,WP,BP  
    def canCapture(self,pos,pieces,deleted,WPyramid,BPyramid):
        markpos=[]
        piece=str(pieces[pos[1]-1][pos[0]-1])
        if piece.startswith("W"):
            if piece.startswith("Wd"):
                pieces[pos[1]-1][pos[0]-1]="d"
            for j in range(16):
                for i in range(8):
                    
                    obj=str(pieces[j][i])
                    posobj=[i+1,j+1]
                    
                    if obj.startswith("B"):
                        premobj=self.premove(posobj,pieces,BPyramid)
                        
                        if len(premobj)==0:
                            if obj.startswith("BC") or obj.startswith("BP"):
                                if (j+1<16) & (i+1<8):
                                    if str(pieces[j+1][i+1])==piece:
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio C1")
                                        continue
                                if (j+1<16) & (i-1>=0):
                                    if str(pieces[j+1][i-1])==piece:
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio C2")
                                        continue
                                if (j-1>=0) & (i+1<8):
                                    if str(pieces[j-1][i+1])==piece:
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio C3")
                                        continue
                                if (j-1>=0) & (i-1>=0):
                                    if str(pieces[j-1][i-1])==piece:
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio C4")
                                        continue
                            if obj.startswith("BT") or obj.startswith("BP"):
                                if j+2<16:    
                                    if (str(pieces[j+1][i])==piece)|((str(pieces[j+2][i])==piece)&(str(pieces[j+1][i])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio T1")
                                        continue
                                if j-2>=0:
                                    if (str(pieces[j-1][i])==piece)|((str(pieces[j-2][i])==piece)&(str(pieces[j-1][i])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio T2")
                                        continue
                                if i+2<8:
                                    if (str(pieces[j][i+1])==piece)|((str(pieces[j][i+2])==piece)&(str(pieces[j][i+1])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio T3")
                                        continue
                                if i-2>=0:
                                    if (str(pieces[j][i-1])==piece)|((str(pieces[j][i-2])==piece)&(str(pieces[j][i-1])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio T4")
                                        continue
                            if obj.startswith("BS"):
                                if j+3<16:
                                    if (str(pieces[j+1][i])==piece)|((str(pieces[j+2][i])==piece)&(str(pieces[j+1][i])==""))|((str(pieces[j+3][i])==piece)&(str(pieces[j+2][i])=="")&(str(pieces[j+1][i])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio S1")
                                        continue
                                if j-3>=0:
                                    if (str(pieces[j-1][i])==piece)|((str(pieces[j-2][i])==piece)&(str(pieces[j-1][i])==""))|((str(pieces[j-3][i])==piece)&(str(pieces[j-2][i])=="")&(str(pieces[j-1][i])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio S2")
                                        continue
                                if i+3<8:
                                    if (str(pieces[j][i+1])==piece)|((str(pieces[j][i+2])==piece)&(str(pieces[j][i+1])==""))|((str(pieces[j][i+3])==piece)&(str(pieces[j][i+2])=="")&(str(pieces[j][i+1])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio S3")
                                        continue
                                if i-3>=0:
                                    if (str(pieces[j][i-1])==piece)|((str(pieces[j][i-2])==piece)&(str(pieces[j][i-1])==""))|((str(pieces[j][i-3])==piece)&(str(pieces[j][i-2])=="")&(str(pieces[j][i-1])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio S4")
                                        continue
                                          
                        down=True
                        up=True
                        right=True
                        left=True
                        downright=True
                        downleft=True
                        upright=True
                        upleft=True
                        numB=int(pieces[j][i][str(pieces[j][i]).index("_")+1:])
                        for n in range(1,16):
                            if (j+n<16)&down:
                                if str(pieces[j+n][i])!="":
                                    if str(pieces[j+n][i]).startswith("W"):
                                        down=False
                                        numW=int(str(pieces[j+n][i])[str(pieces[j+n][i]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("down")
                                            continue
                                    else:
                                        down=False

                            if (j-n>=0)&up:
                                if str(pieces[j-n][i])!="":
                                    if str(pieces[j-n][i]).startswith("W"):
                                        up=False
                                        numW=int(str(pieces[j-n][i])[str(pieces[j-n][i]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("up")
                                            continue
                                    else:
                                        up=False
                            if (i+n<8)&right:
                                if str(pieces[j][i+n])!="":
                                    if str(pieces[j][i+n]).startswith("W"):
                                        right=False
                                        numW=int(str(pieces[j][i+n])[str(pieces[j][i+n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("right")
                                            continue
                                    else:
                                        right=False
                            if (i-n>=0)&left:
                                if str(pieces[j][i-n])!="":
                                    if str(pieces[j][i-n]).startswith("W"):
                                        left=False
                                        numW=int(str(pieces[j][i-n])[str(pieces[j][i-n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("left")
                                            continue
                                    else:
                                        left=False
                            if (j+n<16) & (i+n<8) & downright :
                                if str(pieces[j+n][i+n])!="":
                                    if str(pieces[j+n][i+n]).startswith("W"):
                                        downright=False
                                        numW=int(str(pieces[j+n][i+n])[str(pieces[j+n][i+n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("downright")
                                            continue
                                    else:
                                        downright=False
                            if (j+n<16) & (i-n>=0) & downleft :
                                if str(pieces[j+n][i-n])!="":
                                    if str(pieces[j+n][i-n]).startswith("W"):
                                        downleft=False
                                        numW=int(str(pieces[j+n][i-n])[str(pieces[j+n][i-n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("downleft")
                                            continue
                                    else:
                                        downleft=False
                            if (j-n>=0) & (i+n<8) & upright :
                                if str(pieces[j-n][i+n])!="":
                                    if str(pieces[j-n][i+n]).startswith("W"):
                                        upright=False
                                        numW=int(str(pieces[j-n][i+n])[str(pieces[j-n][i+n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("upright")
                                            continue
                                    else:
                                        upright=False
                            if (j-n>=0) & (i-n>=0) & upleft :
                                if str(pieces[j-n][i-n])!="":
                                    if str(pieces[j-n][i-n]).startswith("W"):
                                        upleft=False
                                        numW=int(str(pieces[j-n][i-n])[str(pieces[j-n][i-n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("upleft")  
                                            continue
                                    else:
                                        upleft=False          
                    
                        if (j+1<16) & (i+1<8):
                            if str(pieces[j+1][i+1]).startswith("WC"):
                                markpos.append(str(pieces[j+1][i+1]))
                        if (j+1<16) & (i-1>=0):
                            if str(pieces[j+1][i-1]).startswith("WC"):
                                markpos.append(str(pieces[j+1][i-1]))
                        if (j-1>=0) & (i+1<8):
                            if str(pieces[j-1][i+1]).startswith("WC"):
                                markpos.append(str(pieces[j-1][i+1]))
                        if (j-1>=0) & (i-1>=0):
                            if str(pieces[j-1][i-1]).startswith("WC"):
                                markpos.append(str(pieces[j-1][i-1]))
                        if j+2<16:
                            if str(pieces[j+2][i]).startswith("WT")& (str(pieces[j+1][i])==""):
                                markpos.append(str(pieces[j+2][i]))
                        if i+2<8:
                           
                            if str(pieces[j][i+2]).startswith("WT")& (str(pieces[j][i+1])==""):
                                markpos.append(str(pieces[j][i+2]))
                        if j-2>0:
                            if str(pieces[j-2][i]).startswith("WT")& (str(pieces[j-1][i])==""):
                                markpos.append(str(pieces[j-2][i]))
                        if i-2>0:
                            if str(pieces[j][i-2]).startswith("WT")& (str(pieces[j][i-1])==""):
                                markpos.append(str(pieces[j][i-2]))
                        if j+3<16:
                            if str(pieces[j+3][i]).startswith("WS")& (str(pieces[j+2][i])=="")& (str(pieces[j+1][i])==""):
                                markpos.append(str(pieces[j+3][i]))
                        if i+3<8:
                            if str(pieces[j][i+3]).startswith("WS")& (str(pieces[j][i+2])=="")& (str(pieces[j][i+1])==""):
                                markpos.append(str(pieces[j][i+3]))
                        if j-3>0:
                            if str(pieces[j-3][i]).startswith("WS")& (str(pieces[j-2][i])=="")& (str(pieces[j-1][i])==""):
                                markpos.append(str(pieces[j-3][i]))
                        if i-3>0:
                            if str(pieces[j][i-3]).startswith("WS")& (str(pieces[j][i-2])=="")& (str(pieces[j][i-1])==""):
                                markpos.append(str(pieces[j][i-3]))
                        if len(markpos)!=0:
                            pieces,deleted=self.capture(j,i,markpos,pieces,deleted)
                            markpos=[]
            

        if piece.startswith("B"):
            if piece.startswith("Bd"):
                pieces[pos[1]-1][pos[0]-1]="d"
            for j in range(16):
                for i in range(8):
                    
                    obj=str(pieces[j][i])
                    posobj=[i+1,j+1]
                    
                    if obj.startswith("W"):
                        premobj=self.premove(posobj,pieces,WPyramid)
                        
                        if len(premobj)==0:
                            
                            if obj.startswith("WC") or obj.startswith("WP"):
                                if (j+1<16) & (i+1<8):
                                    if str(pieces[j+1][i+1])==piece:
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio C1")
                                        continue
                                if (j+1<16) & (i-1>=0):
                                    if str(pieces[j+1][i-1])==piece:
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio C2")
                                        continue
                                if (j-1>=0) & (i+1<8):
                                    if str(pieces[j-1][i+1])==piece:
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio C3")
                                        continue
                                if (j-1>=0) & (i-1>=0):
                                    if str(pieces[j-1][i-1])==piece:
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio C4")
                                        continue
                            if obj.startswith("WT") or obj.startswith("WP"):
                                if j+2<16:    
                                    if (str(pieces[j+1][i])==piece)|((str(pieces[j+2][i])==piece)&(str(pieces[j+1][i])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio T1")
                                        continue
                                if j-2>=0:
                                    if (str(pieces[j-1][i])==piece)|((str(pieces[j-2][i])==piece)&(str(pieces[j-1][i])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio T2")
                                        continue
                                if i+2<8:
                                    if (str(pieces[j][i+1])==piece)|((str(pieces[j][i+2])==piece)&(str(pieces[j][i+1])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio T3")
                                        continue
                                if i-2>=0:
                                    if (str(pieces[j][i-1])==piece)|((str(pieces[j][i-2])==piece)&(str(pieces[j][i-1])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio T4")
                                        continue
                            if obj.startswith("WS"):
                                if j+3<16:
                                    if (str(pieces[j+1][i])==piece)|((str(pieces[j+2][i])==piece)&(str(pieces[j+1][i])==""))|((str(pieces[j+3][i])==piece)&(str(pieces[j+2][i])=="")&(str(pieces[j+1][i])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio S1")
                                        continue
                                if j-3>=0:
                                    if (str(pieces[j-1][i])==piece)|((str(pieces[j-2][i])==piece)&(str(pieces[j-1][i])==""))|((str(pieces[j-3][i])==piece)&(str(pieces[j-2][i])=="")&(str(pieces[j-1][i])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio S2")
                                        continue
                                if i+3<8:
                                    if (str(pieces[j][i+1])==piece)|((str(pieces[j][i+2])==piece)&(str(pieces[j][i+1])==""))|((str(pieces[j][i+3])==piece)&(str(pieces[j][i+2])=="")&(str(pieces[j][i+1])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio S3")
                                        continue
                                if i-3>=0:
                                    if (str(pieces[j][i-1])==piece)|((str(pieces[j][i-2])==piece)&(str(pieces[j][i-1])==""))|((str(pieces[j][i-3])==piece)&(str(pieces[j][i-2])=="")&(str(pieces[j][i-1])=="")):
                                        deleted.append(str(pieces[j][i]))
                                        pieces[j][i]="d"
                                        print("captura por sitio S4")
                                        continue
                        if obj=="WP":
                            continue               
                        down=True
                        up=True
                        right=True
                        left=True
                        downright=True
                        downleft=True
                        upright=True
                        upleft=True
                        numB=int(pieces[j][i][str(pieces[j][i]).index("_")+1:])
                        for n in range(1,16):
                            if (j+n<16)&down:
                                if str(pieces[j+n][i])!="":
                                    if str(pieces[j+n][i]).startswith("B"):
                                        down=False
                                        numW=int(str(pieces[j+n][i])[str(pieces[j+n][i]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("down")
                                            continue
                                    else:
                                        down=False

                            if (j-n>=0)&up:
                                if str(pieces[j-n][i])!="":
                                    if str(pieces[j-n][i]).startswith("B"):
                                        up=False
                                        numW=int(str(pieces[j-n][i])[str(pieces[j-n][i]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("up")
                                            continue
                                    else:
                                        up=False
                                    
                            if (i+n<8)&right:
                                if str(pieces[j][i+n])!="":
                                    if str(pieces[j][i+n]).startswith("B"):
                                        right=False
                                        numW=int(str(pieces[j][i+n])[str(pieces[j][i+n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("right")
                                            continue
                                    else:
                                        right=False
                            if (i-n>=0)&left:
                                if str(pieces[j][i-n])!="":
                                    if str(pieces[j][i-n]).startswith("B"):
                                        left=False
                                        numW=int(str(pieces[j][i-n])[str(pieces[j][i-n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("left")
                                            continue
                                    else:
                                        left=False
                            if (j+n<16) & (i+n<8) & downright :
                                if str(pieces[j+n][i+n])!="":
                                    if str(pieces[j+n][i+n]).startswith("B"):
                                        downright=False
                                        numW=int(str(pieces[j+n][i+n])[str(pieces[j+n][i+n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("downright")
                                            continue
                                    else:
                                        downright=False
                            if (j+n<16) & (i-n>=0) & downleft :
                                if str(pieces[j+n][i-n])!="":
                                    if str(pieces[j+n][i-n]).startswith("B"):
                                        downleft=False
                                        numW=int(str(pieces[j+n][i-n])[str(pieces[j+n][i-n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("downleft")
                                            continue
                                    else:
                                        downleft=False
                            if (j-n>=0) & (i+n<8) & upright :
                                if str(pieces[j-n][i+n])!="":
                                    if str(pieces[j-n][i+n]).startswith("B"):
                                        upright=False
                                        numW=int(str(pieces[j-n][i+n])[str(pieces[j-n][i+n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("upright")
                                            continue
                                    else:
                                        upright=False
                            if (j-n>=0) & (i-n>=0) & upleft :
                                if str(pieces[j-n][i-n])!="":
                                    if str(pieces[j-n][i-n]).startswith("B"):
                                        upleft=False
                                        numW=int(str(pieces[j-n][i-n])[str(pieces[j-n][i-n]).index("_")+1:])
                                        if (numB*n==numW) | (numB/n==numW):
                                            deleted.append(str(pieces[j][i]))
                                            pieces[j][i]="d"
                                            print("upleft")  
                                            continue
                                    else:
                                        upleft=False          
                    
                        if (j+1<16) & (i+1<8):
                            if str(pieces[j+1][i+1]).startswith("BC"):
                                markpos.append(str(pieces[j+1][i+1]))
                        if (j+1<16) & (i-1>=0):
                            if str(pieces[j+1][i-1]).startswith("BC"):
                                markpos.append(str(pieces[j+1][i-1]))
                        if (j-1>=0) & (i+1<8):
                            if str(pieces[j-1][i+1]).startswith("BC"):
                                markpos.append(str(pieces[j-1][i+1]))
                        if (j-1>=0) & (i-1>=0):
                            if str(pieces[j-1][i-1]).startswith("BC"):
                                markpos.append(str(pieces[j-1][i-1]))
                        if j+2<16:
                            if str(pieces[j+2][i]).startswith("BT")& (str(pieces[j+1][i])==""):
                                markpos.append(str(pieces[j+2][i]))
                        if i+2<8:
                           
                            if str(pieces[j][i+2]).startswith("BT")& (str(pieces[j][i+1])==""):
                                markpos.append(str(pieces[j][i+2]))
                        if j-2>0:
                            if str(pieces[j-2][i]).startswith("BT")& (str(pieces[j-1][i])==""):
                                markpos.append(str(pieces[j-2][i]))
                        if i-2>0:
                            if str(pieces[j][i-2]).startswith("BT")& (str(pieces[j][i-1])==""):
                                markpos.append(str(pieces[j][i-2]))
                        if j+3<16:
                            if str(pieces[j+3][i]).startswith("BS")& (str(pieces[j+2][i])=="")& (str(pieces[j+1][i])==""):
                                markpos.append(str(pieces[j+3][i]))
                        if i+3<8:
                            if str(pieces[j][i+3]).startswith("BS")& (str(pieces[j][i+2])=="")& (str(pieces[j][i+1])==""):
                                markpos.append(str(pieces[j][i+3]))
                        if j-3>0:
                            if str(pieces[j-3][i]).startswith("BS")& (str(pieces[j-2][i])=="")& (str(pieces[j-1][i])==""):
                                markpos.append(str(pieces[j-3][i]))
                        if i-3>0:
                            if str(pieces[j][i-3]).startswith("BS")& (str(pieces[j][i-2])=="")& (str(pieces[j][i-1])==""):
                                markpos.append(str(pieces[j][i-3]))
                        if len(markpos)!=0:
                            pieces,deleted=self.capture(j,i,markpos,pieces,deleted)
                            markpos=[]
                            
        #Se decidó poner esto por un posible fallo en el que no solo come a una en una dirección si no que pode por ejemplo hacer sitio a 3 a la vez en la misma columna y consideramos que no era correcto
        for j in range(16):
            for i in range(8):
                if str(pieces[j][i]).startswith("d"):
                    pieces[j][i]=""
        
        
        return pieces,deleted

    def capture(self,i,j,markpos,pieces,deleted):
        
        marker=markpos[0]
        marknum=int(marker[marker.index("_")+1:])
        
        obpiece=str(pieces[i][j])
        obnum=int(obpiece[obpiece.index("_")+1:])
        
        
            
        if len(markpos)>=1:
            for x in range(len(markpos)):
                for y in range(len(markpos)):
                    namU=markpos[x] 
                    u=int(namU[namU.index("_")+1:])
                    namV=markpos[y] 
                    v=int(namV[namV.index("_")+1:])
                    if(namU!=namV):
                        #captura por igualdad
                        if u==obnum:
                            deleted.append(str(pieces[i][j]))
                            pieces[i][j]="d"
                            print("Captura por igualdad")
                        #Captura por potencia(el bucle es de 9 porque el valor mas pequeño es 2 y el más grande es 361 y la potencia a 9 de 2 supera a 361)
                        if u>obnum:
                            pot=1
                            for d in range(9):
                                pot=pot*obnum
                                if pot==u:
                                    deleted.append(str(pieces[i][j]))
                                    pieces[i][j]=""
                                    print("Captura por potencia")
                                    break
                        if u<obnum:
                            pot=1

                            for d in range(9):
                                pot=pot*u
                                if pot==obnum:
                                    deleted.append(str(pieces[i][j]))
                                    pieces[i][j]="d"
                                    print("Captura por potencia")
                                    break
                    #captura por operación aritmética
                        if len(markpos)>1:
                            if (u+v==obnum) | (u-v==obnum) | (v-u==obnum) | (v*u==obnum) | (v/u==obnum) | (u/v==obnum):
                                deleted.append(str(pieces[i][j]))
                                pieces[i][j]="d"
                                print("Captura por aritmetica")
                            else:
                                #captura por progresión aritmetica (4 9 14)
                                if u>v:
                                    if u<obnum:
                                        if obnum-u==u-v:
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion aritmetica")

                                    elif v>obnum:
                                        if u-v==v-obnum:
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion aritmetica")
                                    elif v<obnum<u:
                                        if u-obnum==obnum-v:
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion aritmetica")
                                elif u<v:
                                    if v<obnum:
                                        if obnum-v==v-u:
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion aritmetica")

                                    elif u>obnum:
                                        if v-u==u-obnum:
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion aritmetica")
                                    elif u<obnum<v:
                                        if v-obnum==obnum-u:
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion aritmetica")
                                
                                #captura por progresión geométrica 9 3 27
                                duv=u/v
                                dvu=v/u
                                dov=obnum/v
                                dou=obnum/u
                                duo=u/obnum
                                dvo=v/obnum
                                if  (duv==dvo) | (duv==dou) |(dvu==dov)| (dvu==duo) | (duo==dov) | (dvo==dou):
                                    deleted.append(str(pieces[i][j]))
                                    pieces[i][j]="d"
                                    print("Captura por progresion geometrica")
                                
                                #captura por progresion armonica 6 8 12
                                if u>v:
                                    if u<obnum:
                                        a=obnum-u
                                        b=u-v
                                        if (a/b)==(obnum/v):
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion armonica")

                                    elif v>obnum:
                                        a=u-v
                                        b=v-obnum
                                        if (a/b)==(u/obnum):
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion armonica")
                                    elif v<obnum<u:
                                        a=u-obnum
                                        b=obnum-v
                                        if (a/b)==(u/v):
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion armonica")
                                elif u<v:
                                    if v<obnum:
                                        a=obnum-v
                                        b=v-u
                                        if (a/b)==(obnum/u):
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion armonica")

                                    elif u>obnum:
                                        a=v-u
                                        b=u-obnum
                                        if (a/b)==(v/obnum):
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion armonica")
                                    elif u<obnum<v:
                                        a=v-obnum
                                        b=obnum-u
                                        if (a/b)==(v/u):
                                            deleted.append(str(pieces[i][j]))
                                            pieces[i][j]="d"
                                            print("Captura por progresion armonica")
                                

                            
                        

                
                



        
        return pieces,deleted

    
        
        
       