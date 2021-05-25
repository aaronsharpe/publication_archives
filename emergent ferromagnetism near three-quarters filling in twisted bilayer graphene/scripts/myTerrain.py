# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:32:17 2017

@author: Aaron Sharpe
"""
import numpy as np
import os
from matplotlib.colors import LinearSegmentedColormap


def igorTerrain(n):
    n1 = np.around(n*25/256)
    n2 = np.around(n*37/256)
    n3 = np.around(n*100/256)
    n4 = np.around(n*150/256)

    r = np.zeros((n,3))
    g = np.zeros((n,3))
    b = np.zeros((n,3))

    r[0:int(n1),1]  = np.linspace(0.2,0,n1)
    r[int(n1)-1:int(n2),1] = np.linspace(0,0,(n2-n1)+1)
    r[int(n2)-1:int(n3),1] = np.linspace(0,1,(n3-n2)+1)
    r[int(n3)-1:int(n4),1] = np.linspace(1,.535,(n4-n3)+1)
    r[int(n4)-1:int(n),1]  = np.linspace(.535,1,(n-n4)+1)
    r[:,2] = r[:,1]
    
    g[0:int(n1),1]  = np.linspace(.2,.6,n1)
    g[int(n1)-1:int(n2),1] = np.linspace(.6,.8,(n2-n1)+1)
    g[int(n2)-1:int(n3),1] = np.linspace(.8,1,(n3-n2)+1)
    g[int(n3)-1:int(n4),1] = np.linspace(1,.356,(n4-n3)+1)
    g[int(n4)-1:int(n),1]  = np.linspace(.356,1,(n-n4)+1)
    g[:,2] = g[:,1]
    
    b[0:int(n1),1]  = np.linspace(.6,1,n1)
    b[int(n1)-1:int(n2),1] = np.linspace(1,.375,(n2-n1)+1)
    b[int(n2)-1:int(n3),1] = np.linspace(.375,.6,(n3-n2)+1)
    b[int(n3)-1:int(n4),1] = np.linspace(.6,.3,(n4-n3)+1)
    b[int(n4)-1:int(n),1]  = np.linspace(.3,1,(n-n4)+1)
    b[:,2] = b[:,1]
    
    x = np.linspace(0,1,n)
    r[:,0] = x
    g[:,0] = x
    b[:,0] = x
    
    r = tuple(map(tuple,r))
    g = tuple(map(tuple,g))
    b = tuple(map(tuple,b))
    cdict = {'red':r,'green':g,'blue':b}
    myTerrain = LinearSegmentedColormap('my_colormap', cdict)
    #print(myTerrain)
    return myTerrain


def coldHot(trunclo,trunchi):
    CURRENT_DIR = os.path.dirname(__file__)
    file_path = os.path.join(CURRENT_DIR,'coldwarm.txt')
    mat = np.loadtxt(file_path)
    n = np.shape(mat[int(trunclo):-int(trunchi)])[0]
    rdat = mat[int(trunclo):-int(trunchi),0]/np.max(mat[int(trunclo):-int(trunchi),0])
    gdat = mat[int(trunclo):-int(trunchi),1]/np.max(mat[int(trunclo):-int(trunchi),1])
    bdat = mat[int(trunclo):-int(trunchi),2]/np.max(mat[int(trunclo):-int(trunchi),2])
    r = np.zeros((n,3))
    g = np.zeros((n,3))
    b = np.zeros((n,3))
    r[:,1] = rdat; 
    r[:,2] = rdat
    g[:,1] = gdat; 
    g[:,2] = gdat
    b[:,1] = bdat; 
    b[:,2] = bdat
    x = np.linspace(0,1,n)
    r[:,0] = x
    g[:,0] = x
    b[:,0] = x
    r = tuple(map(tuple,r))
    g = tuple(map(tuple,g))
    b = tuple(map(tuple,b))
    cdict = {'red':r,'green':g,'blue':b}
    myColdhot = LinearSegmentedColormap('my_colormap', cdict)
    return myColdhot