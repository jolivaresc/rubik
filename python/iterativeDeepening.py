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
    
    http://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/

Created on Thu Oct  6 21:01:53 2016

@author: jose
"""

from search import trajectory
from dls import DLS

class IterativeDeepening:
    @staticmethod
    def search(start,stop,depthLimit,maxDepth):
        if maxDepth == 0:
            return None
        if (stop(start)):
            return trajectory(start)
        else:
            for i in range(0,maxDepth):
                if DLS.search(start,stop,depthLimit,maxDepth):
                    return DLS.search(start,stop,depthLimit,maxDepth)
                depthLimit = depthLimit + 1
        return None
        
        
        
        
        
        
        