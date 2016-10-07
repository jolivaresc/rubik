# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:45:02 2016

@author: jose
"""

#import bfs, gbfs
from patternheuristic import PatternBasedHeuristic
from bfs import BFS
from gbfs import GBFS
from dls import DLS
from dfs import DFS
import time
from rubik import RubikPuzzle
#print("Algoritmos.\n")

aux = 0
DEPTH_DLS = 100
t,solution={},[]

#Se crea una lista de n cubos
def createCubes(n):
    return [RubikPuzzle() for i in range(0,n)]

#Mover cubos n movimientos
def applyShuffle(rubik,n):
    rubik.shuffle(n)

#Resolver cubo utilizando BFS
def solveBFS(rubik):
    aux = time.time()
    solution_BFS = BFS.search(rubik,lambda x:x==RubikPuzzle())
    t["BFS: "] = (time.time()-aux)*1000
    aux = 0
    return solution_BFS

#Resolver cubo utilizando DLS    
def solveDLS(rubik,depth):
    aux = time.time()
    solution_DLS = DLS.search(rubik,lambda x:x==RubikPuzzle(),depth)
    t["DLS: "] = (time.time()-aux)*1000
    aux = 0
    return solution_DLS

#Resolver cubo utilizando DFS
def solveDFS(rubik):
    aux = time.time()
    solution_DFS = DFS.search(rubik,lambda x:x==RubikPuzzle())
    time["DFS: "] (time.time()-aux)*1000
    aux = 0
    return solution_DFS

#Crear heurística para GBFS
def defineHeuristic(num):
    return PatternBasedHeuristic(num)
#Resolver cubo utilizando GBFS
def solveGBFS(rubik,db):
    aux = time.time()
    solution_GBFS = GBFS.search(rubik,lambda x:x==RubikPuzzle(),db.heuristic)
    t["GBFS: "] = (time.time()-aux)*1000
    return solution_GBFS



#Mover Cubos
#for i in len(cube):
#    applyShuffle(cube[i],4)    

#applyShuffle(cube[1],4)

#Variables auxiliares para cálculo de tiempo
#resultados = solveCubes(rubik)

#time_bfs,time_gbfs = resultados[0][0],resultados[0][1]

#for i in range(0,len(resultados[0])):
#    print(str(resultados[0][i]*1000))










