# -*- coding: utf-8 -*-
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    

Created on Wed Oct  5 22:31:14 2016

@author: jose
"""
from search import trajectory
from stack import Stack
#from memory_profiler import profile

#@profile
class DLS:
    @staticmethod    
    def search(start,stop,depthLimit,maxDepth=0):
        if depthLimit == 0:
            return None
        agenda, explored = Stack(), set()         
        if (stop(start)):
            return trajectory(start)        
        agenda.push(start)
        depth = 0
        while(agenda):
            nodo = agenda.pop()
            if depth <= depthLimit:
                #nodo = agenda.pop()
                explored.add(nodo)
                for child in nodo.expand():
                    if (stop(child)):
                        return trajectory(child)
                    elif(not child in explored):
                        agenda.push(child)
            else:
                break
            depth = depth + 1
        return None
                
                
                
                
                
                
                