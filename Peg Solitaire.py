#!/usr/bin/python
from copy import deepcopy
from math import floor

# Classe che rappresenta uno stato. In essa sono memorizzati alcuni
# dati sullo stato, come il costo per generarlo, la profondità a cui
# si trova nell'albero di ricerca ed un puntatore al nodo padre, oltre
# ovviamente al valore dello stato stesso. Inoltre esso ha un metodo che
# ritorna una lista dei suoi stati successori ed un predicato che verifica
# se la configurazione salvata è finale.
class State:
    def __init__(self,configuration,parent=None,depth=0,cost=0):
        self.configuration=configuration
        self.rows=len(self.configuration)
        self.columns=len(self.configuration[0])
        self.cost=cost
        self.parent=parent
        self.depth=depth
    def goal_state(self):
            found=False
            for i in range(0,self.rows):
                for j in range(0,self.columns):
                    if self.configuration[i][j]==1:
                        if not found:
                            found=True
                        else:
                            return False
            if self.configuration[int(floor(self.rows/2))][int(floor(self.columns/2))]==1:
                return True
            else:
                return False
    def __move_down(self,x,y,c):
        if x+2<self.rows and self.configuration[x+1][y]==1 and self.configuration[x+2][y]==0:
            temp=deepcopy(self.configuration)
            temp[x][y]=0
            temp[x+1][y]=0
            temp[x+2][y]=1
            child=State(temp,self,self.depth+1,self.cost+c)
            return child
        else:
            return None
    def __move_up(self,x,y,c):
        if x-2>=0 and self.configuration[x-1][y]==1 and self.configuration[x-2][y]==0:
            temp=deepcopy(self.configuration)
            temp[x][y]=0
            temp[x-1][y]=0
            temp[x-2][y]=1
            child=State(temp,self,self.depth+1,self.cost+c)
            return child
        else:
            return None
    def __move_left(self,x,y,c):
        if y-2>=0 and self.configuration[x][y-1]==1 and self.configuration[x][y-2]==0:
            temp=deepcopy(self.configuration)
            temp[x][y]=0
            temp[x][y-1]=0
            temp[x][y-2]=1
            child=State(temp,self,self.depth+1,self.cost+c)
            return child
        else:
            return None
    def __move_right(self,x,y,c):
        if y+2<self.columns and self.configuration[x][y+1]==1 and self.configuration[x][y+2]==0:
            temp=deepcopy(self.configuration)
            temp[x][y]=0
            temp[x][y+1]=0
            temp[x][y+2]=1
            child=State(temp,self,self.depth+1,self.cost+c)
            return child
        else:
            return None
    def successors(self,c=(1,1,1,1)):
        succ=[]
        for i in range(0,self.rows):
            for j in range(0,self.columns):
                if self.configuration[i][j]==1:
                    temp=self.__move_down(i,j,c[0])
                    if temp is not None:
                        succ.append(temp)
                    temp=self.__move_up(i,j,c[1])
                    if temp is not None:
                        succ.append(temp)
                    temp=self.__move_left(i,j,c[2])
                    if temp is not None:
                        succ.append(temp)
                    temp=self.__move_right(i,j,c[3])
                    if temp is not None:
                        succ.append(temp)
        return succ

# Funzione di ordinamento rispetto ai costi
def partition(queue,low,high):
        pivot=queue[high]
        s=low
        for j in range(low,high):
            if queue[j].cost<pivot.cost:
                temp=queue[j]
                queue[j]=queue[s]
                queue[s]=temp
                s+=1
        queue[high]=queue[s]
        queue[s]=pivot
        return s
def quicksort(queue,low,high):
    if low<high:
        s=partition(queue,low,high)
        quicksort(queue,low,s-1)
        quicksort(queue,s+1,high)
# Funzione che stampa una soluzione
def print_sol(fringe):
    if fringe.parent is not None:
        print_sol(fringe.parent)
    print
    for i in range(0,fringe.columns+2):
            print "-",
    print
    for i in fringe.configuration:
        print "|",
        for j in i:
            print str(j),
        print "|"
    for i in range(0,fringe.columns+2):
        print "-",
    print
    print

# Metodo che risolve il problema tramite ricerca in profondità
# Le frange sono oggetti State con puntatori all'indietro,
# la coda LIFO è una lista di frange. Ad ogni passo estendo
# la frangia con i nuovi possibili stati successori. Se non trovo
# la soluzione e la coda è vuota, allora il problema non ha soluzione.
def solve_dfs(start):
    queue=[start]
    c_gen=1
    c_vis=0
    c_depth=0
    while True:
        if len(queue)==0:
            print "Depth First Search - Solution: There's no solution"
            print "Depth First Search - Generated Nodes: "+str(c_gen)
            print "Depth First Search - Visited Nodes: "+str(c_vis)
            print "Depth First Search - Max reached depth: "+str(c_depth)
            return None
        else:
            fringe=queue[0]
            queue=queue[1:]
            c_vis+=1
            c_depth=max(c_depth,fringe.depth)
            if fringe.goal_state():
                print "Depth First Search - Solution: "
                print_sol(fringe)
                print "Depth First Search - Solution found at depth: "+str(fringe.depth)
                print "Depth First Search - Generated Nodes: "+str(c_gen)
                print "Depth First Search - Visited Nodes: "+str(c_vis)
                print "Depth First Search - Max reached depth: "+str(c_depth)
                return fringe
            else:
                extensions=fringe.successors()
                queue=extensions+queue
                c_gen+=len(extensions)

# Metodo che usa la ricerca in ampiezza. Vale quanto detto per la
# ricerca in profondità, ma la coda è gestica con una politica FIFO.
def solve_bfs(start):
    queue=[start]
    c_gen=1
    c_vis=0
    c_depth=0
    while True:
        if len(queue)==0:
            print "Breadth First Search - Solution: There's no solution"
            print "Breadth First Search - Generated Nodes: "+str(c_gen)
            print "Breadth First Search - Visited Nodes: "+str(c_vis)
            print "Breadth First Search - Max reached depth: "+str(c_depth)
            return None
        else:
            fringe=queue[0]
            queue=queue[1:]
            c_vis+=1
            c_depth=max(c_depth,fringe.depth)
            if fringe.goal_state():
                print "Breadth First Search - Solution: "
                print_sol(fringe)
                print "Breadth First Search - Solution found at depth: "+str(fringe.depth)
                print "Breadth First Search - Generated Nodes: "+str(c_gen)
                print "Breadth First Search - Visited Nodes: "+str(c_vis)
                print "Breadth First Search - Max reached depth: "+str(c_depth)
                return fringe
            else:
                extensions=fringe.successors()
                queue=queue+extensions
                c_gen+=len(extensions)

# Metodo di ricerca in profondità iterata. Per ogni iterazione controllo
# se ha senso andare più in profondità con la prossima oppure se
# effettivamente non c'è soluzione.
def solve_ids(start):
    iteration=0
    while True:
        queue=[start]
        c_gen=1
        c_vis=0
        c_depth=0
        go_on=False
        while len(queue)!=0:
            fringe=queue[0]
            queue=queue[1:]
            c_vis+=1
            c_depth=max(c_depth,fringe.depth)
            if fringe.goal_state():
                print "Iterative Deepening Search - Solution: "
                print_sol(fringe)
                print "Iterative Deepening Search - Solution found at depth: "+str(fringe.depth)
                print "Iterative Deepening Search - Generated Nodes: "+str(c_gen)
                print "Iterative Deepening Search - Visited Nodes: "+str(c_vis)
                print "Iterative Deepening Search - Max reached depth: "+str(c_depth)
                return fringe
            else:
                extensions=fringe.successors()
                if fringe.depth<=iteration:
                    queue=extensions+queue
                    c_gen+=len(extensions)
                elif len(extensions)>0:
                    go_on=True
                    iteration+=1
        if not go_on:
            print "Iterative Deepening Search - Solution: There's no solution"
            print "Iterative Deepening Search - Generated Nodes: "+str(c_gen)
            print "Iterative Deepening Search - Visited Nodes: "+str(c_vis)
            print "Iterative Deepening Search - Max reached depth: "+str(c_depth)
            return None

# Metodo di ricerca con costi uniformi. Prima di essere estratte
# le frange vengono ordinate secondo il loro costo.
def solve_ucs(start,costs):
    queue=[start]
    c_gen=1
    c_vis=0
    c_depth=0
    while True:
        if len(queue)==0:
            print "Uniform Cost Search - Solution: There's no solution"
            print "Uniform Cost Search - Generated Nodes: "+str(c_gen)
            print "Uniform Cost Search - Visited Nodes: "+str(c_vis)
            print "Uniform Cost Search - Max reached depth: "+str(c_depth)
            return None
        else:
            fringe=queue[0]
            queue=queue[1:]
            c_vis+=1
            c_depth=max(c_depth,fringe.depth)
            if fringe.goal_state():
                print "Uniform Cost Search - Solution: "
                print_sol(fringe)
                print "Uniform Cost Search - Cost: "+str(fringe.cost)
                print "Uniform Cost Search - Solution found at depth: "+str(fringe.depth)
                print "Uniform Cost Search - Generated Nodes: "+str(c_gen)
                print "Uniform Cost Search - Visited Nodes: "+str(c_vis)
                print "Uniform Cost Search - Max reached depth: "+str(c_depth)
                return fringe
            else:
                extensions=fringe.successors(costs)
                queue=queue+extensions
                c_gen+=len(extensions)
            quicksort(queue,0,len(queue)-1)

# Creo i problemi e li provo. I primi due problemi terminano
# in breve tempo, il terzo richiede invece più passi, infine
# l'ultimo non ha soluzione.
e1=[[" "," ",1,1,0," "," "],
    [" "," ",0,1,1," "," "],
    [0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0],
    [0,0,0,0,0,1,0],
    [" "," ",0,0,0," "," "],
    [" "," ",0,0,0," "," "]]
e2=[[" "," "," ",0,0,0," "," "," "],
    [" "," "," ",0,0,0," "," "," "],
    [" "," "," ",0,0,1," "," "," "],
    [0,0,0,0,0,1,0,0,0],
    [1,1,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [" "," "," ",0,0,0," "," "," "],
    [" "," "," ",0,0,0," "," "," "],
    [" "," "," ",0,0,0," "," "," "]]
l=[[" "," ",0,1,1," "," "],
   [" "," ",1,0,1," "," "],
   [0,0,0,0,1,0,0],
   [0,0,1,1,0,1,0],
   [0,0,0,0,1,0,0],
   [" "," ",0,1,0," "," "],
   [" "," ",0,0,0," "," "]]
ns=[[1,1,1,0,1,1,1]]

game_e1=State(e1)
game_e2=State(e2)
game_l=State(l)
game_ns=State(ns)
solve_dfs(game_e1)
print
print "##########################################################################"
print
solve_bfs(game_l)
print
print "##########################################################################"
print
solve_ids(game_ns)
print
print "##########################################################################"
print
solve_ucs(game_e2,(1,3,2,0))
