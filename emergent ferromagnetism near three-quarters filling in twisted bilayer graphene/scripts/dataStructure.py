# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:17:32 2017

@author: Aaron Sharpe

This code creates a few usful classes for organizing data hierarchically in 
a meaningful way for devices

Levels:
    Chip
    Device
    Sweep
    Sweep parameters with inculded data

"""

from dataStructure import *

class Chip:
    """This class initializes an empty class for labeling a chip"""
    def __init__(self):
        self.data = []
        
class Device:
    """This class initializes an empty class for labeling an individual 
    device"""
    def __init__(self):
        self.data = []

class Sweep:
    """
        Alows you to add scanned parameters for a given sweep using the add_param mod
    """
    def __init__(self):
        self.data = []
        self.paramInfo = {}
    
    def add_param(self,param,data,label=r'',units=r''):
        """Add a swept parameter and the values from the sweep"""
        setattr(self,param,data)
        self.paramInfo.update({param:{'label':label,'units':units}})