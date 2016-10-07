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
    

Created on Thu Oct  6 23:11:37 2016

@author: jose
"""

from collections import deque
from search import trajectory

class Bidirectional:     
    @staticmethod
    def search(start,stop):
        
        if stop(start):
            return trajectory(start)
        
        bandera1,bandera2=False,False
        #Front        
        FF = deque()
        #Back
        FB = deque()
        
        FF.append(start)
        FB.append(stop)
        
        while (len(FF) != 0) or (len(FB) != 0):
            if len(FF) != 0:
                sol1 = FF.popleft()
                if (Bidirectional.exist(FB,sol1)):
                    trajectoryFF = trajectory(sol1)
                    bandera1 = True
                else:
                    FF.append(sol1.expand())            
            if len(FB) != 0:
                sol2 = FB.popleft()
                if(Bidirectional.exist(FF,sol2)):
                    trajectoryFB = trajectory(sol2)
                    bandera2 = True
                else:
                    FB.append(sol2.expand())
            if bandera1 and bandera2:
                return trajectoryFF + trajectoryFB
        return None
                
        
    @staticmethod    
    def exist(list,rubik):
        aux = []
        aux = list.copy()
        while (aux.count(1) != 0):
            if rubik.__eq__(aux.pop()):
                return True
            return False
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        