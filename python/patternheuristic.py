# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 23:45:55 2016

@author: stan
"""
from collections import deque
from rubik import RubikPuzzle
#from os import listdir
#import os
#os.path.isfile(W"W)

class PatternBasedHeuristic:
    def __init__(self,depth=7,objective=None,pattern=None):
        print('computing pattern data base...')
        if(objective==None):
            objective = RubikPuzzle()
        agenda = deque()
        self.explored = set()
        self.depth = depth
        agenda.append(objective)
        self.patterns = {}
        if(pattern==None):
            pattern ='ACGIJLgiMÑjlOQmñRToqrtxz'
        self.pattern = pattern
        self.pattern_mask = RubikPuzzle.get_pattern_mask(pattern)
        while(agenda):
            node = agenda.popleft()
            self.explored.add(node)
            self.patterns[self.pattern_mask&node.configuration]=\
            node.depth
            for child in node.expand():
                if(child.depth>depth):
                    return 
                elif(not child in self.explored):
                    agenda.append(child)
#        file = open("db.dat","w")
#        file.write(str(self.depth))
#        file.close()
#        
                    
    def heuristic(self,puzzle):
        key = self.pattern_mask&puzzle.configuration
        return (self.patterns[key] \
        if key in self.patterns else self.depth+1)
            

        
        
    
    
            