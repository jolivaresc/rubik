# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:43:35 2016

http://cgi.csc.liv.ac.uk/~tbc/comp210/7lectureSearchSpeedup.pdf

@author: jose
"""


from search import trajectory
from stack import Stack

class DFS:        
    @staticmethod    
    def search(start,stop):
        agenda, explored = Stack(), set()         
        if (stop(start)):
            return trajectory(start)        
        agenda.push(start)
        while(agenda):
                nodo = agenda.pop()
                explored.add(nodo)
                for child in nodo.expand():
                    if (stop(child)):
                        return trajectory(child)
                    elif(not child in explored):
                        agenda.push(child)
        return None
                
      
                
                
                
                
                