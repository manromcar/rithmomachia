from copy import deepcopy
import random
import game
import machiaEngine

pieces=["C_01","C_02","C_03","C_04","C_05","C_06","C_07","C_08","C_09","C_16","C_25","C_36","C_49","C_64","C_81",
        "T_06","T_09","T_12","T_16","T_20","T_25","T_30","T_36","T_42","T_49","T_56","T_64","T_72","T_81","T_90","T_100",
        "S_15","S_25","S_28","S_36","S_45","S_49","S_64","S_66","S_81","S_120","S_121","S_225","S_361","S_153","S_169","S_289",
        "P"]
people=3
chromosomes=len(pieces)
gen=1

population=[[random.randint(1,100) for x in range(chromosomes)] for y in range(people)]
class geneticAlgorythm():
    def __init__(self,people,chromosomes,gen,population, pieces):
        self.people=people
        self.chromosomes=chromosomes
        self.gen=gen
        self.population=population
        self.pieces=pieces
        self.movement=machiaEngine.Move()


    def evaluationCorpore(self,population):
        
        winner=[0 for i in range(len(population))]
        for x,person in enumerate(population):
            for oponent in population:
                print(person)
                n=2 #numero de niveles que crea en el arbol, tiene que ser par para que coja un grupo de movimientos de blancas y negras
                turn=True
                gs = machiaEngine.GameState()
                
                gaming=game.App(40, 0, 10,0,0)
                
                gaming.board()
                if len(gaming.boardPieces)==0:
                    gaming.loadImages()
                
                gaming.showPieces()
                print(gaming.playing)
                
                
                
                while gaming.playing==True:
                    if turn:
                        
                        decisionTree= Tree(0,[0,0])
                        #creo el arbol
                        decisionTree=self.create_Tree(n,turn,person,gaming,gs,decisionTree)
                        move = decisionTree.minmax(n)
                        print(move)
                        gaming.play(move[2],move[3])
                        gaming.play(move[0],move[1])
                        print(gaming.deletedList)
                        print (gaming.gs.pieces)
                        turn=False
                        win="W"
                    else:
                        decisionTree= Tree(0,[0,0])
                        #creo el arbol
                        decisionTree=self.create_Tree(n,turn,oponent,gaming,gs,decisionTree)
                        move = decisionTree.minmax(n)
                        gaming.play(move[2],move[3])
                        gaming.play(move[0],move[1])
                        win="B"
                        turn=True
                        print(move)
                gaming.quit()
                del gaming
                if win.startswith("W"):
                    winner[x]=winner[x]+1
            
        return winner


                    
            
                    
                
                
                







    #poner el tablero en algun valor que se le pasa

    def create_Tree(self,n,turn,person,gaming,gs,decisionTree):
        
        for i_y,y in enumerate(gs.pieces):
            for i_x,x in enumerate(y):
                
                
                pyramid=""
                color=""
                if turn:
                    color="W"
                    pyramid=gaming.WPyramid
                else:
                    color="B"
                    pyramid=gaming.BPyramid
                if str(x).startswith(color):
                    
                    
                    decisionTree.add_node([i_x+1,i_y+1])
                    branch=decisionTree.get([i_x+1,i_y+1])
                    
                    premoves=self.movement.premove([i_x+1,i_y+1],gs.pieces,pyramid)
                    premoves=premoves+self.movement.preirregular([i_x+1,i_y+1],gs.pieces,pyramid)
                    z=0
                    while z<len(premoves):
                        branch.add_node([premoves[z],premoves[z+1]])
                        z=z+2
                        #mueves miras si has comido alguna del adversario y si es asi guardas el valor
                    for br in branch.nodes:
                        gaming.play(i_x+1,i_y+1)
                        gaming.play(br.pos[0],br.pos[1])


                        
                        if n>1:
                            br=self.create_Tree(n-1,not turn,person,gaming,gs,br)
                            
                        else:
                            for d in gaming.deletedList:
                                if str(d).startswith(color):
                                    ind=pieces.index(d[1:])
                                    br.val=br.val+ person[ind]
                                else:
                                    ind=pieces.index(d[1:])
                                    br.val=br.val- person[ind]
        
        return decisionTree







class Tree:

    def __init__(self, val,pos):
        self.val = val
        self.pos =pos
        self.nodes = []

    def add_node(self, pos,val=0):
        self.nodes.append(Tree(val,pos))
        return 

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
    def max2(self):
        val=self.nodes[0].val
        for node in self.nodes:
            node.val=node.max.val
            if node.val > val:
                val= node.val


        return val
    def min2(self):
        val=self.nodes[0].val
        for node in self.nodes:
            node.val=node.min.val
            if node.val < val:
                val= node.val


        return val

    def minmax(self,n):
        move=[0,0,0,0]
        if n>1:
            
            for node in self.nodes:
                for node2 in node.nodes:
                    node2.minmax(n-1)
                    if n%2==0:
                        self.val=self.max2
                    else:
                        self.val=self.min2

    
        if n==2:
            maxnodes=0
            for node in self.nodes:
                for node2 in self.nodes:
                    if self.val==node2.val:
                        move[0]=node2.pos[0]
                        move[1]=node2.pos[1]
                        move[2]=node.pos[0]
                        move[3]=node.pos[1]
                    
                maxnodes=maxnodes+1
            if move==[0,0,0,0]:
                maxnodes2=0
                while maxnodes2<1:   
                    num1=random.randint(0,maxnodes-1)
                    maxnodes2=0
                    for node2 in self.nodes[num1].nodes:
                        maxnodes2=maxnodes2+1
                    
                num2=random.randint(0,maxnodes2-1)
                move[0]=self.nodes[num1].nodes[num2].pos[0]
                move[1]=self.nodes[num1].nodes[num2].pos[1]
                move[2]=self.nodes[num1].pos[0]
                move[3]=self.nodes[num1].pos[1]

        return move
    def get(self,pos):
        res=0
        for n in self.nodes:
            if pos[0]==n.pos[0] and pos[1]==n.pos[1]:
                res=n
        return res
    def __repr__(self):
        
        return f"({self.pos},{self.val}): {self.nodes}"
        


        
genetic=geneticAlgorythm(people,chromosomes,gen,population, pieces)
winner=genetic.evaluationCorpore(population)
print (winner)







