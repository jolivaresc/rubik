# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:59:56 2016

@author: jose
"""

class Stack:
    def __init__(self):
        self.items = []
        #self.container =[]
        
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        
        try:
            return self.items.pop()
        except IndexError:
            return False
        
#        if not self.isEmpty():
#            return self.items.pop()
#        else:
#            print("Stack is empty")
#            exit()
        
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:            
            return self.items[-1]
            
    
    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
    