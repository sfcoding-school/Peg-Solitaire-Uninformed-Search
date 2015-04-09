#!/usr/bin/python
# -*- coding: cp1252 -*-
from copy import deepcopy
from math import floor
from UninformedSearchs import solve_dfs,solve_bfs,solve_ids,solve_ucs

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
    def get_data(self):
        return self.configuration
    def print_sol(self):
        if self.parent is not None:
            self.parent.print_sol()
        print
        for i in range(0,self.columns+2):
                print "-",
        print
        for i in self.configuration:
            print "|",
            for j in i:
                print str(j),
            print "|"
        for i in range(0,self.columns+2):
            print "-",
        print
        print

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
