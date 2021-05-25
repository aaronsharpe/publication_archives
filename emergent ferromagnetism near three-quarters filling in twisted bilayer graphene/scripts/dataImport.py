# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:17:32 2017

@author: Aaron Sharpe

"""

import numpy as np
from dataStructure import *

def T2Import(dirName,lineskip,parentdir,filelist,labels=None,delim='_'):
    if labels is None:
        labels=filelist

    newSweep = Sweep()
    for i in np.arange(len(filelist)):
        filename = ''.join(['../../Data/T2/',parentdir,'/',dirName,'/',dirName,delim,filelist[i],'.txt'])
        mat = np.loadtxt(filename,skiprows=lineskip)
        newSweep.add_param(filelist[i],np.transpose(mat[:,1:]),label=labels[i])

        
    return newSweep


def T2Import1Dswitch(dirName,lineskip,parentdir,filelist,labels=None):
    if labels is None:
        labels=filelist

    newSweep = Sweep()
    for i in np.arange(len(filelist)):
        filename = ''.join(['../../Data/T2/',parentdir,'/',dirName,'/',dirName,'_',filelist[i],'.txt'])
        mat = np.loadtxt(filename,skiprows=lineskip)
        newSweep.add_param(filelist[i],np.transpose(mat[1:]),label=labels[i])

        
    return newSweep

def T2Import1D(dirName,lineskip,parentdir,filelist,labels=None,delim='_'):
	if labels is None:
		labels=filelist
		
	newSweep = Sweep()
	for i in np.arange(len(filelist)):
		filename = ''.join(['../../Data/T2/',parentdir,'/',dirName,'/',dirName,delim,filelist[i],'.txt'])
		mat = np.loadtxt(filename,skiprows=1)
		newSweep.add_param(filelist[i],np.transpose(mat[:,1]),label=filelist[i])

	return newSweep

def T2Import1Dtuple(dirName,lineskip,parentdir,filelist,labels=None):
	if labels is None:
		labels=filelist
		
	newSweep = Sweep()
	for i in np.arange(len(filelist)):
		filename = ''.join(['../../Data/T2/',parentdir,'/',dirName,'/',dirName,'_',filelist[i],'.txt'])
		mat = np.loadtxt(filename,skiprows=1)
		newSweep.add_param(filelist[i],mat,label=filelist[i])

	return newSweep

def T2ImportDCdomains(dirName,lineskip,parentdir,filelist,labels=None):
	if labels is None:
		labels=filelist
		
	newSweep = Sweep()
	for i in np.arange(len(filelist)):
		filename = ''.join(['../../Data/T2/',parentdir,'/',dirName,'/',dirName,'_',filelist[i],'.txt'])
		mat = np.loadtxt(filename,skiprows=1)
		newSweep.add_param(filelist[i],np.transpose(mat[:,1]),label=filelist[i])


	filename = ''.join(['../../Data/T2/',parentdir,'/',dirName,'/',dirName,'_',filelist[0],'.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('dcbias',mat[:,0]*1E9,label=r'$I_{DC}\ (\mathrm{nA})$')


	newSweep.add_param('rxxt',newSweep.vxxt/(newSweep.current)/1000,label=r'$R_{xx}\ (\mathrm{k\Omega})$')
	newSweep.add_param('rxxb',newSweep.vxxb/(newSweep.current)/1000,label=r'$R_{xx}\ (\mathrm{k\Omega})$')
	newSweep.add_param('ryxl',newSweep.vyxl/(newSweep.current)/1000,label=r'$R_{yx}\ (\mathrm{k\Omega})$')
	newSweep.add_param('ryxr',newSweep.vyxr/(newSweep.current)/1000,label=r'$R_{yx}\ (\mathrm{k\Omega})$')

	return newSweep
	
def T2ImportHall(dirName):

	newSweep = Sweep()
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_vxx.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxx',np.transpose(mat[:,1:]),label=r'$V_{xx}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_vxxph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixx',np.transpose(mat[:,1:]),label=r'$\phi_{xx}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_vyx.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyx',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_vyxph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyx',np.transpose(mat[:,1:]),label=r'$\phi_{yx}\ (\mathrm{deg})$')

	
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('I',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphi',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('temp',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')
	
	newSweep.add_param('Rxx',newSweep.Vxx/(newSweep.I*1E-9)/1000,label=r'$R_{xx}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryx',newSweep.Vyx/(newSweep.I*1E-9)/1000,label=r'$R_{yx}\ (\mathrm{k\Omega})$')


	return newSweep



def T2ImportHystLoop(dirName):

	newSweep = Sweep()
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxx.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxdown',np.transpose(mat[:,1:]),label=r'$V_{xx}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxxph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxdown',np.transpose(mat[:,1:]),label=r'$\phi_{xx}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyx.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxdown',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyxph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxdown',np.transpose(mat[:,1:]),label=r'$\phi_{yx}\ (\mathrm{deg})$')

	
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Idown',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphidown',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempdown',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')
	
	newSweep.add_param('Rxxdown',newSweep.Vxxdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxdown',newSweep.Vyxdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}\ (\mathrm{k\Omega})$')
	

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxx.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxup',np.transpose(mat[:,1:]),label=r'$V_{xx}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxxph.txt'])    
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxup',np.transpose(mat[:,1:]),label=r'$\phi_{xx}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyx.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxup',np.transpose(mat[:,1:]),label=r'$V_{yx}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyxph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxup',np.transpose(mat[:,1:]),label=r'$\phi_{yx}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iup',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphiup',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempup',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxup',newSweep.Vxxup/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxup',newSweep.Vyxup/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}\ (\mathrm{k\Omega})$')


	return newSweep


def T2ImportAllPairsHystLoop(dirName):

	newSweep = Sweep()
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxxt.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxtdown',np.transpose(mat[:,1:]),label=r'$V_{xx}^{\mathrm{t}}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxxtph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxtdown',np.transpose(mat[:,1:]),label=r'$\phi_{xx}^{\mathrm{t}}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxxb.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxbdown',np.transpose(mat[:,1:]),label=r'$V_{xx}^{\mathrm{b}}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxxbph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxbdown',np.transpose(mat[:,1:]),label=r'$\phi_{xx}^{\mathrm{b}}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyxl.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxldown',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyxlph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxldown',np.transpose(mat[:,1:]),label=r'$\phi_{yx}^\mathrm{l}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyxr.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxrdown',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{r}\ (\mathrm{V})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyxrph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxrdown',np.transpose(mat[:,1:]),label=r'$\phi_{yx}^\mathrm{r}\ (\mathrm{deg})$')
	
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Idown',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphidown',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempdown',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')
	
	newSweep.add_param('Rxxtdown',newSweep.Vxxtdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbdown',newSweep.Vxxbdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxldown',newSweep.Vyxldown/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrdown',newSweep.Vyxrdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')
	

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxxt.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxtup',np.transpose(mat[:,1:]),label=r'$V_{xx}^\mathrm{t}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxxtph.txt'])    
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxtup',np.transpose(mat[:,1:]),label=r'$\phi_{xx}^\mathrm{t}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxxb.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxbup',np.transpose(mat[:,1:]),label=r'$V_{xx}^\mathrm{b}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxxbph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxbup',np.transpose(mat[:,1:]),label=r'$\phi_{xx}^\mathrm{b}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyxl.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxlup',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyxlph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxlup',np.transpose(mat[:,1:]),label=r'$\phi_{yx}^\mathrm{l}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyxr.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxrup',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{r}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyxrph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxrup',np.transpose(mat[:,1:]),label=r'$\phi_{yx}^\mathrm{r}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iup',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphiup',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempup',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtup',newSweep.Vxxtup/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbup',newSweep.Vxxbup/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxlup',newSweep.Vyxlup/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrup',newSweep.Vyxrup/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')

	return newSweep


def T2ImportAllPairsHystLoopTemp(dirName):

	newSweep = Sweep()
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_vxxt.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxtdown',np.transpose(mat[:,1:]),label=r'$V_{xx}^{\mathrm{t}}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_vxxtph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxtdown',np.transpose(mat[:,1:]),label=r'$\phi_{xx}^{\mathrm{t}}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_vxxb.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxbdown',np.transpose(mat[:,1:]),label=r'$V_{xx}^{\mathrm{b}}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_vxxbph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxbdown',np.transpose(mat[:,1:]),label=r'$\phi_{xx}^{\mathrm{b}}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_vyxl.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxldown',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_vyxlph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxldown',np.transpose(mat[:,1:]),label=r'$\phi_{yx}^\mathrm{l}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_vyxr.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxrdown',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{r}\ (\mathrm{V})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_vyxrph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxrdown',np.transpose(mat[:,1:]),label=r'$\phi_{yx}^\mathrm{r}\ (\mathrm{deg})$')
	
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Idown',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphidown',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempdown',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')
	
	newSweep.add_param('Rxxtdown',newSweep.Vxxtdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbdown',newSweep.Vxxbdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxldown',newSweep.Vyxldown/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrdown',newSweep.Vyxrdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')
	

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_vxxt.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxtup',np.transpose(mat[:,1:]),label=r'$V_{xx}^\mathrm{t}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_vxxtph.txt'])    
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxtup',np.transpose(mat[:,1:]),label=r'$\phi_{xx}^\mathrm{t}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_vxxb.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxbup',np.transpose(mat[:,1:]),label=r'$V_{xx}^\mathrm{b}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_vxxbph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxbup',np.transpose(mat[:,1:]),label=r'$\phi_{xx}^\mathrm{b}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_vyxl.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxlup',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_vyxlph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxlup',np.transpose(mat[:,1:]),label=r'$\phi_{yx}^\mathrm{l}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_vyxr.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxrup',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{r}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_vyxrph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxrup',np.transpose(mat[:,1:]),label=r'$\phi_{yx}^\mathrm{r}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iup',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphiup',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempup',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtup',newSweep.Vxxtup/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbup',newSweep.Vxxbup/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxlup',newSweep.Vyxlup/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrup',newSweep.Vyxrup/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')

	return newSweep


def T2ImportAllPairsHystLoop1D(dirName):

	newSweep = Sweep()
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxxt.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Vxxtdown',np.transpose(mat[:,1]),label=r'$V_{xx}^{\mathrm{t}}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxxtph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phixxtdown',np.transpose(mat[:,1]),label=r'$\phi_{xx}^{\mathrm{t}}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxxb.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Vxxbdown',np.transpose(mat[:,1]),label=r'$V_{xx}^{\mathrm{b}}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vxxbph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phixxbdown',np.transpose(mat[:,1]),label=r'$\phi_{xx}^{\mathrm{b}}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyxl.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Vyxldown',np.transpose(mat[:,1]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyxlph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phiyxldown',np.transpose(mat[:,1]),label=r'$\phi_{yx}^\mathrm{l}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyxr.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Vyxrdown',np.transpose(mat[:,1]),label=r'$V_{yx}^\mathrm{r}\ (\mathrm{V})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_vyxrph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phiyxrdown',np.transpose(mat[:,1]),label=r'$\phi_{yx}^\mathrm{r}\ (\mathrm{deg})$')
	
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_current.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Idown',np.transpose(mat[:,1])*1E9,label=r'$I\ (\mathrm{nA})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_currph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iphidown',np.transpose(mat[:,1]),label=r'$\phi_{I}\ (\mathrm{deg})$')
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_temp.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('tempdown',np.transpose(mat[:,1]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')
	
	newSweep.add_param('Rxxtdown',newSweep.Vxxtdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbdown',newSweep.Vxxbdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxldown',newSweep.Vyxldown/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrdown',newSweep.Vyxrdown/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')
	

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxxt.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Vxxtup',np.transpose(mat[:,1]),label=r'$V_{xx}^\mathrm{t}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxxtph.txt'])    
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phixxtup',np.transpose(mat[:,1]),label=r'$\phi_{xx}^\mathrm{t}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxxb.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Vxxbup',np.transpose(mat[:,1]),label=r'$V_{xx}^\mathrm{b}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vxxbph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phixxbup',np.transpose(mat[:,1]),label=r'$\phi_{xx}^\mathrm{b}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyxl.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Vyxlup',np.transpose(mat[:,1]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyxlph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phiyxlup',np.transpose(mat[:,1]),label=r'$\phi_{yx}^\mathrm{l}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyxr.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Vyxrup',np.transpose(mat[:,1]),label=r'$V_{yx}^\mathrm{r}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_vyxrph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phiyxrup',np.transpose(mat[:,1]),label=r'$\phi_{yx}^\mathrm{r}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_current.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iup',np.transpose(mat[:,1])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_currph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iphiup',np.transpose(mat[:,1]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_temp.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('tempup',np.transpose(mat[:,1]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtup',newSweep.Vxxtup/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbup',newSweep.Vxxbup/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxlup',newSweep.Vyxlup/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrup',newSweep.Vyxrup/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')
	
	return newSweep




def T2ImportIndContHystLoop1D(dirName):

	newSweep = Sweep()
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v1.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V1down',np.transpose(mat[:,1]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi1tdown',np.transpose(mat[:,1]),label=r'$\phi_{1}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v2.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V2down',np.transpose(mat[:,1]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi2down',np.transpose(mat[:,1]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v3.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V3down',np.transpose(mat[:,1]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi3down',np.transpose(mat[:,1]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v4.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V4down',np.transpose(mat[:,1]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi4down',np.transpose(mat[:,1]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_current.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Idown',np.transpose(mat[:,1])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_currph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iphidown',np.transpose(mat[:,1]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_temp.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('tempdown',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtdown',(newSweep.V1down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbdown',(newSweep.V4down-newSweep.V3down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxldown',(newSweep.V4down-newSweep.V1down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrdown',(newSweep.V3down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')



	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v1.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Bup',np.transpose(mat[:,0]),label=r'$B\ (\mathrm{T})$')

	newSweep.add_param('V1up',np.transpose(mat[:,1]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi1up',np.transpose(mat[:,1]),label=r'$\phi_{1}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v2.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V2up',np.transpose(mat[:,1]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi2up',np.transpose(mat[:,1]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v3.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V3up',np.transpose(mat[:,1]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi3up',np.transpose(mat[:,1]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v4.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V4up',np.transpose(mat[:,1]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi4up',np.transpose(mat[:,1]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_current.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iup',np.transpose(mat[:,1])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_currph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iphiup',np.transpose(mat[:,1]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_temp.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('tempup',np.transpose(mat[:,1]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtup',(newSweep.V1up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbup',(newSweep.V4up-newSweep.V3up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxlup',(newSweep.V4up-newSweep.V1up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrup',(newSweep.V3up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')
	return newSweep

def T2ImportIndContHystLoop1DTemp(dirName):

	newSweep = Sweep()
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v1.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V1down',np.transpose(mat[:,1]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi1tdown',np.transpose(mat[:,1]),label=r'$\phi_{1}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v2.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V2down',np.transpose(mat[:,1]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi2down',np.transpose(mat[:,1]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v3.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V3down',np.transpose(mat[:,1]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi3down',np.transpose(mat[:,1]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v4.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V4down',np.transpose(mat[:,1]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi4down',np.transpose(mat[:,1]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_current.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Idown',np.transpose(mat[:,1])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_currph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iphidown',np.transpose(mat[:,1]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_temp.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('tempdown',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtdown',(newSweep.V1down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbdown',(newSweep.V4down-newSweep.V3down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxldown',(newSweep.V4down-newSweep.V1down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrdown',(newSweep.V3down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')



	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v1.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Bup',np.transpose(mat[:,0]),label=r'$B\ (\mathrm{T})$')

	newSweep.add_param('V1up',np.transpose(mat[:,1]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi1up',np.transpose(mat[:,1]),label=r'$\phi_{1}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v2.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V2up',np.transpose(mat[:,1]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi2up',np.transpose(mat[:,1]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v3.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V3up',np.transpose(mat[:,1]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi3up',np.transpose(mat[:,1]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v4.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V4up',np.transpose(mat[:,1]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi4up',np.transpose(mat[:,1]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_current.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iup',np.transpose(mat[:,1])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_currph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iphiup',np.transpose(mat[:,1]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_temp.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('tempup',np.transpose(mat[:,1]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtup',(newSweep.V1up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbup',(newSweep.V4up-newSweep.V3up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxlup',(newSweep.V4up-newSweep.V1up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrup',(newSweep.V3up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')
	return newSweep


def T2ImportIndContHystLoop(dirName):

	newSweep = Sweep()
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v1.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V1down',np.transpose(mat[:,1:]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi1down',np.transpose(mat[:,1:]),label=r'$\phi_{1}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v2.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V2down',np.transpose(mat[:,1:]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi2down',np.transpose(mat[:,1:]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v3.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V3down',np.transpose(mat[:,1:]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi3down',np.transpose(mat[:,1:]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v4.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V4down',np.transpose(mat[:,1:]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi4down',np.transpose(mat[:,1:]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Idown',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphidown',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempdown',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtdown',(newSweep.V1down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbdown',(newSweep.V4down-newSweep.V3down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxldown',(newSweep.V4down-newSweep.V1down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrdown',(newSweep.V3down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')



	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v1.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Bup',np.transpose(mat[:,0]),label=r'$B\ (\mathrm{T})$')

	newSweep.add_param('V1up',np.transpose(mat[:,1:]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi1up',np.transpose(mat[:,1:]),label=r'$\phi_{1}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v2.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V2up',np.transpose(mat[:,1:]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi2up',np.transpose(mat[:,1:]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v3.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V3up',np.transpose(mat[:,1:]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi3up',np.transpose(mat[:,1:]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v4.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V4up',np.transpose(mat[:,1:]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi4up',np.transpose(mat[:,1:]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iup',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphiup',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempup',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtup',(newSweep.V1up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbup',(newSweep.V4up-newSweep.V3up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxlup',(newSweep.V4up-newSweep.V1up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrup',(newSweep.V3up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')
	return newSweep

def T2ImportIndContHystLoop1Djank(dirName):

	newSweep = Sweep()
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v1.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V1down',np.transpose(mat[1:]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi1down',np.transpose(mat[1:]),label=r'$\phi_{1}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v2.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V2down',np.transpose(mat[1:]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi2down',np.transpose(mat[1:]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v3.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V3down',np.transpose(mat[1:]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi3down',np.transpose(mat[1:]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v4.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V4down',np.transpose(mat[1:]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi4down',np.transpose(mat[1:]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Idown',np.transpose(mat[1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphidown',np.transpose(mat[1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_down_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempdown',np.transpose(mat[1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtdown',(newSweep.V1down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbdown',(newSweep.V4down-newSweep.V3down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxldown',(newSweep.V4down-newSweep.V1down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrdown',(newSweep.V3down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')



	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v1.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	#newSweep.add_param('Bup',np.transpose(mat[:,0]),label=r'$B\ (\mathrm{T})$')

	newSweep.add_param('V1up',np.transpose(mat[1:]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi1up',np.transpose(mat[1:]),label=r'$\phi_{1}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v2.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V2up',np.transpose(mat[1:]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi2up',np.transpose(mat[1:]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v3.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V3up',np.transpose(mat[1:]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi3up',np.transpose(mat[1:]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v4.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V4up',np.transpose(mat[1:]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi4up',np.transpose(mat[1:]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iup',np.transpose(mat[1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphiup',np.transpose(mat[1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_up_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempup',np.transpose(mat[1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtup',(newSweep.V1up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbup',(newSweep.V4up-newSweep.V3up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxlup',(newSweep.V4up-newSweep.V1up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrup',(newSweep.V3up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')
	return newSweep

def T2ImportIndContHystLoopTemp(dirName):

	newSweep = Sweep()
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v1.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V1down',np.transpose(mat[:,1:]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi1down',np.transpose(mat[:,1:]),label=r'$\phi_{1}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v2.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V2down',np.transpose(mat[:,1:]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi2down',np.transpose(mat[:,1:]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v3.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V3down',np.transpose(mat[:,1:]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi3down',np.transpose(mat[:,1:]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v4.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V4down',np.transpose(mat[:,1:]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi4down',np.transpose(mat[:,1:]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Idown',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphidown',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'down_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempdown',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtdown',(newSweep.V1down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbdown',(newSweep.V4down-newSweep.V3down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxldown',(newSweep.V4down-newSweep.V1down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrdown',(newSweep.V3down-newSweep.V2down)/(newSweep.Idown*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')



	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v1.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Bup',np.transpose(mat[:,0]),label=r'$B\ (\mathrm{T})$')

	newSweep.add_param('V1up',np.transpose(mat[:,1:]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi1up',np.transpose(mat[:,1:]),label=r'$\phi_{1}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v2.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V2up',np.transpose(mat[:,1:]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi2up',np.transpose(mat[:,1:]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v3.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V3up',np.transpose(mat[:,1:]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi3up',np.transpose(mat[:,1:]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v4.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V4up',np.transpose(mat[:,1:]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi4up',np.transpose(mat[:,1:]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iup',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphiup',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, 'up_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('tempup',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxtup',(newSweep.V1up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxbup',(newSweep.V4up-newSweep.V3up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxlup',(newSweep.V4up-newSweep.V1up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxrup',(newSweep.V3up-newSweep.V2up)/(newSweep.Iup*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')
	return newSweep

def T2ImportIndCont2D(dirName):

	newSweep = Sweep()
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v1.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V1',np.transpose(mat[:,1:]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi1',np.transpose(mat[:,1:]),label=r'$\phi_{1}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v2.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V2',np.transpose(mat[:,1:]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi2',np.transpose(mat[:,1:]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v3.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V3',np.transpose(mat[:,1:]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi3',np.transpose(mat[:,1:]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v4.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V4',np.transpose(mat[:,1:]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi4',np.transpose(mat[:,1:]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('I',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphi',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('temp',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxt',(newSweep.V1-newSweep.V2)/(newSweep.I*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxb',(newSweep.V4-newSweep.V3)/(newSweep.I*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxl',(newSweep.V4-newSweep.V1)/(newSweep.I*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxr',(newSweep.V3-newSweep.V2)/(newSweep.I*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')

	return newSweep

def T2ImportIndCont1D(dirName):

	newSweep = Sweep()
	
	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v1.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V1',np.transpose(mat[:,1]),label=r'$V_{1}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v1ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi1',np.transpose(mat[:,1]),label=r'$\phi_{1}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v2.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V2',np.transpose(mat[:,1]),label=r'$V_{2}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v2ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi2',np.transpose(mat[:,1]),label=r'$\phi_{2}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v3.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V3',np.transpose(mat[:,1]),label=r'$V_{3}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v3ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi3',np.transpose(mat[:,1]),label=r'$\phi_{3}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v4.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('V4',np.transpose(mat[:,1]),label=r'$V_{4}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_v4ph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('phi4',np.transpose(mat[:,1]),label=r'$\phi_{4}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_current.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('I',np.transpose(mat[:,1])*1E9,label=r'$I\ (\mathrm{nA})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_currph.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('Iphi',np.transpose(mat[:,1]),label=r'$\phi_{I}\ (\mathrm{deg})$')

	filename = ''.join(['../../Data/T2/Dil_fridge_data/', dirName, '/', dirName, '_temp.txt'])
	mat = np.loadtxt(filename,skiprows=1)
	newSweep.add_param('temp',np.transpose(mat[:,1]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')

	newSweep.add_param('Rxxt',(newSweep.V1-newSweep.V2)/(newSweep.I*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Rxxb',(newSweep.V4-newSweep.V3)/(newSweep.I*1E-9)/1000,label=r'$R_{xx}^\mathrm{b}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxl',(newSweep.V4-newSweep.V1)/(newSweep.I*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxr',(newSweep.V3-newSweep.V2)/(newSweep.I*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')

	return newSweep










def T2ImportHallTemp(dirName):

	newSweep = Sweep()
	
	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_v2t.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('V2t',np.transpose(mat[:,1:]),label=r'$V_{2t}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_v2tph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phi2t',np.transpose(mat[:,1:]),label=r'$\phi_{2t}\ (\mathrm{deg})$')
	
	
	
	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_vxxt.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vxxt',np.transpose(mat[:,1:]),label=r'$V_{xx}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_vxxtph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phixxt',np.transpose(mat[:,1:]),label=r'$\phi_{xx}\ (\mathrm{deg})$')


	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_vyxl.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxl',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_vyxlph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxl',np.transpose(mat[:,1:]),label=r'$\phi_{yx}\ (\mathrm{deg})$')

	
	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_vyxr.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Vyxr',np.transpose(mat[:,1:]),label=r'$V_{yx}^\mathrm{l}\ (\mathrm{V})$')

	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_vyxrph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('phiyxr',np.transpose(mat[:,1:]),label=r'$\phi_{yx}\ (\mathrm{deg})$')
	
	
	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_current.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('I',np.transpose(mat[:,1:])*1E9,label=r'$I\ (\mathrm{nA})$')
	
	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_currph.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('Iphi',np.transpose(mat[:,1:]),label=r'$\phi_{I}\ (\mathrm{deg})$')
	
	filename = ''.join(['../../Data/T2/VTI2_data/', dirName, '/', dirName, '_temp.txt'])
	mat = np.loadtxt(filename,skiprows=2)
	newSweep.add_param('temp',np.transpose(mat[:,1:]),label=r'$\mathrm{Temperature}\ (\mathrm{K})$')
	
	newSweep.add_param('Rxxt',newSweep.Vxxt/(newSweep.I*1E-9)/1000,label=r'$R_{xx}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('R2t',newSweep.V2t/(newSweep.I*1E-9)/1000,label=r'$R_{2t}^\mathrm{t}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxl',newSweep.Vyxl/(newSweep.I*1E-9)/1000,label=r'$R_{yx}^\mathrm{l}\ (\mathrm{k\Omega})$')
	newSweep.add_param('Ryxr',newSweep.Vyxr/(newSweep.I*1E-9)/1000,label=r'$R_{yx}^\mathrm{r}\ (\mathrm{k\Omega})$')


	return newSweep