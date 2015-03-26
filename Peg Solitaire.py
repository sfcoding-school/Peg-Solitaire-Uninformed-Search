#!/usr/bin/python
from copy import deepcopy
from math import floor
# Funzione che controlla se sono in uno stato finale, cioè
# se è rimasta una sola pallina e se essa si trova nella
# posizione centrale della scacchiera
def goal_state(state):
    found=False
    for i in range(0,len(state)):
        for j in range(0,len(state[0])):
            if state[i][j]==1:
                if not found:
                    found=True
                else:
                    return False
    if state[int(floor(len(state)/2))][int(floor(len(state[0])/2))]==1:
        return True
    else:
        return False
# Quattro funzioni che definiscono le possibili mosse.
# Controllo prima di non sforare la scacchiera, poi
# se la mossa è corretta (e quindi mangio un pezzo).
def move_down(state,x,y):
    if x+2<len(state) and state[x+1][y]==1 and state[x+2][y]==0:
        state[x][y]=0
        state[x+1][y]=0
        state[x+2][y]=1
        return state
    else:
        return False
def move_up(state,x,y):
    if x-2>=0 and state[x-1][y]==1 and state[x-2][y]==0:
        state[x][y]=0
        state[x-1][y]=0
        state[x-2][y]=1
        return state
    else:
        return False
def move_left(state,x,y):
    if y-2>=0 and state[x][y-1]==1 and state[x][y-2]==0:
        state[x][y]=0
        state[x][y-1]=0
        state[x][y-2]=1
        return state
    else:
        return False
def move_right(state,x,y):
    if y+2<len(state[0]) and state[x][y+1]==1 and state[x][y+2]==0:
        state[x][y]=0
        state[x][y+1]=0
        state[x][y+2]=1
        return state
    else:
        return False
# Funzione di ordinamento rispetto ai costi
def partition(queue,low,high):
    pivot=queue[high]
    s=low
    for j in range(low,high):
        if queue[j][1]<pivot[1]:
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
    print
    for i in fringe:
        for j in range(0,len(i)+2):
            print "-",
        print
        for j in i:
            print "|",
            for k in j:
                print str(k),
            print "|"
        for j in range(0,len(i)+2):
            print "-",
        print
        print
# Metodo che risolve il problema tramite ricerca in profondità
# Uno stato è dato da una matrice, le frange sono liste di matrici,
# infine la coda LIFO è una lista di frange. Ad ogni passo estendo
# la frangia applicando una per una le quattro possibili mosse.
# Se non trovo la soluzione e la coda è vuota, allora il problema
# non ha soluzione.
def solve_dfs(start):
    queue=[[start]]
    c_gen=1
    c_vis=0
    c_depth=0
    while True:
        if len(queue)==0:
            print "Depth First Search - Solution: There's no solution"
            print "Depth First Search - Generated Nodes: "+str(c_gen)
            print "Depth First Search - Visited Nodes: "+str(c_vis)
            print "Depth First Search - Max reached depth: "+str(c_depth)
            return []
        else:
            fringe=queue[0]
            queue=queue[1:]
            head=fringe[0]
            c_vis+=1
            c_depth=max(c_depth,len(fringe))
            if goal_state(head):
                print "Depth First Search - Solution: "
                print_sol(fringe[::-1])
                print "Depth First Search - Generated Nodes: "+str(c_gen)
                print "Depth First Search - Visited Nodes: "+str(c_vis)
                print "Depth First Search - Max reached depth: "+str(c_depth)
                return fringe[::-1]
            else:
                for i in range(0,len(head)):
                    for j in range(0,len(head[0])):
                        if head[i][j]==1:
                            temp=move_right(deepcopy(head),i,j)
                            if temp!=False:
                                queue=[[temp]+fringe]+queue
                                c_gen+=1
                            temp=move_left(deepcopy(head),i,j)
                            if temp!=False:
                                queue=[[temp]+fringe]+queue
                                c_gen+=1
                            temp=move_down(deepcopy(head),i,j)
                            if temp!=False:
                                queue=[[temp]+fringe]+queue
                                c_gen+=1
                            temp=move_up(deepcopy(head),i,j)
                            if temp!=False:
                                queue=[[temp]+fringe]+queue
                                c_gen+=1
# Metodo che usa la ricerca in ampiezza. Vale quanto detto per la
# ricerca in profondità, ma la coda è gestica con una politica FIFO.
def solve_bfs(start):
    queue=[[start]]
    c_gen=1
    c_vis=0
    c_depth=0
    while True:
        if len(queue)==0:
            print "Breadth First Search - Solution: There's no solution"
            print "Breadth First Search - Generated Nodes: "+str(c_gen)
            print "Breadth First Search - Visited Nodes: "+str(c_vis)
            print "Breadth First Search - Max reached depth: "+str(c_depth)
            return []
        else:
            fringe=queue[0]
            queue=queue[1:]
            head=fringe[0]
            c_vis+=1
            c_depth=max(c_depth,len(fringe))
            if goal_state(head):
                print "Breadth First Search - Solution: "
                print_sol(fringe[::-1])
                print "Breadth First Search - Generated Nodes: "+str(c_gen)
                print "Breadth First Search - Visited Nodes: "+str(c_vis)
                print "Breadth First Search - Max reached depth: "+str(c_depth)
                return fringe[::-1]
            else:
                for i in range(0,len(head)):
                    for j in range(0,len(head[0])):
                        if head[i][j]==1:
                            temp=move_right(deepcopy(head),i,j)
                            if temp!=False:
                                queue=queue+[[temp]+fringe]
                                c_gen+=1
                            temp=move_left(deepcopy(head),i,j)
                            if temp!=False:
                                queue=queue+[[temp]+fringe]
                                c_gen+=1
                            temp=move_down(deepcopy(head),i,j)
                            if temp!=False:
                                queue=queue+[[temp]+fringe]
                                c_gen+=1
                            temp=move_up(deepcopy(head),i,j)
                            if temp!=False:
                                queue=queue+[[temp]+fringe]
                                c_gen+=1
# Metodo di ricerca in profondità iterata. Per ogni iterazione controllo
# se ha senso andare più in profondità con la prossima oppure se
# effettivamente non c'è soluzione.
def solve_ids(start):
    iteration=0
    while True:
        iteration+=1
        queue=[[start]]
        c_gen=1
        c_vis=0
        c_depth=0
        go_on=False
        while len(queue)!=0:
            fringe=queue[0]
            queue=queue[1:]
            head=fringe[0]
            c_vis+=1
            c_depth=max(c_depth,len(fringe))
            if goal_state(head):
                print "Iterative Deepening - Solution: "
                print_sol(fringe[::-1])
                print "Iterative Deepening - Generated Nodes: "+str(c_gen)
                print "Iterative Deepening - Visited Nodes: "+str(c_vis)
                print "Iterative Deepening - Max reached depth: "+str(c_depth)
                return fringe[::-1]
            else:
                for i in range(0,len(head)):
                    for j in range(0,len(head[0])):
                        if head[i][j]==1:
                            temp=move_right(deepcopy(head),i,j)
                            if temp!=False:
                                if len(fringe)<iteration:
                                    queue=[[temp]+fringe]+queue
                                    c_gen+=1
                                else:
                                    go_on=True
                            temp=move_left(deepcopy(head),i,j)
                            if temp!=False and len(fringe)<iteration:
                                if len(fringe)<iteration:
                                    queue=[[temp]+fringe]+queue
                                    c_gen+=1
                                else:
                                    go_on=True
                            temp=move_down(deepcopy(head),i,j)
                            if temp!=False and len(fringe)<iteration:
                                if len(fringe)<iteration:
                                    queue=[[temp]+fringe]+queue
                                    c_gen+=1
                                else:
                                    go_on=True
                            temp=move_up(deepcopy(head),i,j)
                            if temp!=False and len(fringe)<iteration:
                                if len(fringe)<iteration:
                                    queue=[[temp]+fringe]+queue
                                    c_gen+=1
                                else:
                                    go_on=True
        if not go_on:
            print "Iterative Deepening - Solution: There's no solution"
            print "Iterative Deepening - Generated Nodes: "+str(c_gen)
            print "Iterative Deepening - Visited Nodes: "+str(c_vis)
            print "Iterative Deepening - Max reached depth: "+str(c_depth)
            return []
# Metodo di ricerca con costi uniformi. Ogni frangia è messa in una coppia
# con il suo costo, in modo che esse possano essere ordinate in base ad esso.
def solve_ucs(start,costs):
    queue=[([start],0)]
    c_gen=1
    c_vis=0
    c_depth=0
    while True:
        if len(queue)==0:
            print "Uniform Cost Search - Solution: There's no solution"
            print "Uniform Cost Search - Generated Nodes: "+str(c_gen)
            print "Uniform Cost Search - Visited Nodes: "+str(c_vis)
            print "Uniform Cost Search - Max reached depth: "+str(c_depth)
            return []
        else:
            fringe=queue[0]
            queue=queue[1:]
            head=fringe[0][0]
            c_vis+=1
            c_depth=max(c_depth,len(fringe[0]))
            if goal_state(head):
                print "Uniform Cost Search - Solution: "
                print_sol(fringe[0][::-1])
                print "Uniform Cost Search - Cost: "+str(fringe[1])
                print "Uniform Cost Search - Generated Nodes: "+str(c_gen)
                print "Uniform Cost Search - Visited Nodes: "+str(c_vis)
                print "Uniform Cost Search - Max reached depth: "+str(c_depth)
                return (fringe[0][::-1],fringe[1])
            else:
                for i in range(0,len(head)):
                    for j in range(0,len(head[0])):
                        if head[i][j]==1:
                            temp=move_down(deepcopy(head),i,j)
                            if temp!=False:
                                queue=[([temp]+fringe[0],costs[0]+fringe[1])]+queue
                                c_gen+=1
                            temp=move_up(deepcopy(head),i,j)
                            if temp!=False:
                                queue=[([temp]+fringe[0],costs[1]+fringe[1])]+queue
                                c_gen+=1
                            temp=move_left(deepcopy(head),i,j)
                            if temp!=False:
                                queue=[([temp]+fringe[0],costs[2]+fringe[1])]+queue
                                c_gen+=1
                            temp=move_right(deepcopy(head),i,j)
                            if temp!=False:
                                queue=[([temp]+fringe[0],costs[3]+fringe[1])]+queue
                                c_gen+=1
            quicksort(queue,0,len(queue)-1)
# Creo i problemi e li provo. I primi due problemi terminano
# in breve tempo, il terzo richiede invece più passi, infine
# l'ultimo non ha soluzione.
game_e1=[[" "," ",1,1,0," "," "],
         [" "," ",0,1,1," "," "],
         [0,0,0,0,0,0,0],
         [0,0,0,1,1,0,0],
         [0,0,0,0,0,1,0],
         [" "," ",0,0,0," "," "],
         [" "," ",0,0,0," "," "]]
game_e2=[[" "," "," ",0,0,0," "," "," "],
         [" "," "," ",0,0,0," "," "," "],
         [" "," "," ",0,0,1," "," "," "],
         [0,0,0,0,0,1,0,0,0],
         [1,1,0,0,1,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [" "," "," ",0,0,0," "," "," "],
         [" "," "," ",0,0,0," "," "," "],
         [" "," "," ",0,0,0," "," "," "]]
game_l=[[" "," ",0,1,1," "," "],
        [" "," ",1,0,1," "," "],
        [0,0,0,0,1,0,0],
        [0,0,1,1,0,1,0],
        [0,0,0,0,1,0,0],
        [" "," ",0,1,0," "," "],
        [" "," ",0,0,0," "," "]]
game_ns=[[1,1,1,0,1,1,1]]
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
