from copy import deepcopy
import random
from tkinter.tix import Tree
import game
import machiaEngine

pieces=["C_01","C_02","C_03","C_04","C_05","C_06","C_07","C_08","C_09","C_16","C_25","C_36","C_49","C_64","C_81",
        "T_06","T_09","T_12","T_16","T_20","T_25","T_30","T_36","T_42","T_49","T_56","T_64","T_72","T_81","T_90","T_100",
        "S_15","S_25","S_28","S_36","S_45","S_49","S_64","S_66","S_81","S_120","S_121","S_225","S_361","S_153","S_169","S_289",
        "P"]
people=7
chromosomes=len(pieces)
gen=10

population=[[random.randint(0,100) for x in range(chromosomes)] for y in range(people)]

def evaluationCorpore(population,pieces):
    for person in population:
        for oponent in population:
            n=6 #numero de niveles que crea en el arbol, tiene que ser par para que coja un grupo de movimientos de blancas y negras
            turn=True
            playing=True
            gs = machiaEngine.GameState()
            gaming=game.App(20, 1, 15,0,0)
            gaming()
            while playing==True:
                if turn:
                    decisionTree= Tree(0,[0,0])
                    #creo el arbol
                    decisionTree=create_Tree(n,turn,person,gaming,gs,decisionTree)
                    move = minmax(n, decisionTree)


                    
                    
                                    
#poner el tablero en algun valor que se le pasa

def create_Tree(n,turn,person,gaming,gs,decisionTree):
    for i_y,y in enumerate(gs.pieces):
        for i_x,x in enumerate(y):
            color=""
            if turn:
                color="W"
                pyramid=gaming.WPyramid
            else:
                color="B"
                pyramid=gaming.BPyramid
            if str(x).startswith(color):
                branch=decisionTree.add_node([i_x+1,i_y+1])
                temp=deepcopy(gs.pieces)
                dList=gaming.deletedList
                premoves=machiaEngine.Move.premove([i_x+1,i_y+1],temp,pyramid)
                z=0
                while z<len(premoves):
                    branch.add_node([premoves[z],premoves[z+1]])
                    z=z+2
                    #mueves miras si has comido alguna del adversario y si es asi guardas el valor
                for br in branch.nodes:
                    gaming.play(i_x+1,i_y+1)
                    gaming.play(br.pos[0],br.pos[1])
                    newList=gaming.deletedList
                    for d in dList:
                        newList.remove(d)
                    if newList!=[]:
                        for new in newList:
                            ind=pieces.index(new[1:])
                            br.val=br.val+int(person[ind])
                        #Estoy sumandole los valores a la rama padre pues al ser par esta es una decision max
                        if n%2==0:
                            decisionTree.val=decisionTree.val+br.max.val
                        else:
                            decisionTree.val=decisionTree.val-br.min.val

                    if(n>0):
                        turn= not turn
                        br=create_Tree(n,turn,person,gaming,gs,br)
                        gs.pieces=temp   
                    n= n -1
    return decisionTree 
          
    

                            



class Tree:

    def __init__(self, val,pos):
        self.val = val
        self.pos =pos
        self.nodes = []

    def add_node(self, pos,val=0):
        self.nodes.append(Tree(val,pos))
    
    def max(self):
        res=self.nodes[0]
        val=self.nodes[0].val
        for node in self.nodes:
            if node.val > val:
                res= node
                val= node.val
        return res
    def min(self):
        res=self.nodes[0]
        val=self.nodes[0].val
        for node in self.nodes:
            if node.val < val:
                res= node
                val= node.val
        return res
    def minmax(self,n):
        res=[0,0,0,0,0]
        oldN=n
        if n>0:
            if n%2==0:
                for node1 in self.nodes:
                    for node2 in node1.nodes:
                        


    
        