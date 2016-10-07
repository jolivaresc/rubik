# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import genfromtxt


class Data:

    def loadData(self,fileName = "data.txt"):
        return genfromtxt(fileName,delimiter=",")
    
    
