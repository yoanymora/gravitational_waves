#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 16:22:15 2018

@author: gravwaves
"""



# =============================================
# IMPORT LIBRARIES
# =============================================
import numpy as np
import pylab




# =============================================
# FUNCTION TO READ TEMPLATE
# =============================================
def Read(templatename,doplot):

    # ----------------------------------------------
    # Path of the catalog    
    rutacatalogs     = 'CatalogCCSN/'
    
    # ----------------------------------------------
    # Andresen16
    if templatename[:4] == 'AndS':
        # Select template
        if templatename == 'AndS11': filename = 's11gw_equ.csv'
        elif templatename == 'AndS20': filename = 's20gw_equ.csv'
        elif templatename == 'AndS27': filename = 's27gw_equ.csv'
        else:  print('PILAS: unknown CCSNe GW form the Andresen16 catalog')
        # Select folder and fullpath
        folder   = 'Andresen16/'
        fullpath = rutacatalogs + folder + filename
        # Load data        
        t        = np.loadtxt(fullpath,usecols=(0),delimiter=',')
        hp       = np.loadtxt(fullpath,usecols=(1),delimiter=',')
        hx       = np.loadtxt(fullpath,usecols=(2),delimiter=',')
        h        = hp + hx
    
    # ----------------------------------------------
    # Andresen18
    elif templatename[:3] == 'And':
        # Select template
        if   templatename == 'And1': filename = 'And1815fr1kpc_equ.txt'
        elif templatename == 'And2': filename = 'And1815nr1kpc_equ.txt'
        elif templatename == 'And3': filename = 'And1815r1kpc_equ.txt'
        else:  print('PILAS: unknown CCSNe GW form the Andresen18 catalog')
        
        folder   = 'Andresen18/'
        fullpath = rutacatalogs + folder + filename
        # Load data
        t        = np.loadtxt(fullpath,usecols=(0))
        hp       = np.loadtxt(fullpath,usecols=(1))
        hx       = np.loadtxt(fullpath,usecols=(2))
        h        = hp + hx
    
    
    # ----------------------------------------------
    # Dimmelmeier08
    elif templatename[:3] == 'Dim':
        # Select template
        if   templatename == 'Dim1': filename = 'signal_s15a2o05_ls.dat'
        elif templatename == 'Dim2': filename = 'signal_s15a2o09_ls.dat'
        elif templatename == 'Dim3': filename = 'signal_s15a3o15_ls.dat'
        else:  print('PILAS: unknown CCSNe GW form the Dimmelmeier08 catalog')
        
        folder   = 'Dimmelmeier08/'
        fullpath = rutacatalogs + folder + filename
        # Load data
        t        = np.loadtxt(fullpath,usecols=(0)) # ms
        hp       = 0*t
        hx       = 0*t
        h        = np.loadtxt(fullpath,usecols=(1)) # 10 Kpc
        
        t        = t/1000    # s
        h        = h*10      # 1 Kpc
    
    
    # ----------------------------------------------
    # Ott13
    elif templatename[:3] == 'Ott':
        # Select template
        if   templatename == 'Ott1': filename = 's27WHW02_LS220_j0_rx3_full_cc_fheat1.00_hD.dat'
        elif templatename == 'Ott2': filename = 's27WHW02_LS220_j0_rx3_full_cc_fheat1.05_hD.dat'
        elif templatename == 'Ott3': filename = 's27WHW02_LS220_j0_rx3_full_cc_fheat1.1_hD.dat'
        elif templatename == 'Ott4': filename = 's27WHW02_LS220_j0_rx3_full_cc_fheat1.15_hD.dat'
        else:  print('PILAS: unknown CCSNe GW form the Dimmelmeier08 catalog')

        folder   = 'Ott13/'
        fullpath = rutacatalogs + folder + filename
        # Load data  
        t        = np.loadtxt(fullpath,usecols=(0))
        hp       = np.loadtxt(fullpath,usecols=(1))
        hx       = np.loadtxt(fullpath,usecols=(2))
        
        # Eliminate samples lower than 0.3 s
        ind2keep = np.where(t>0.3) 
        t        = t[ind2keep]
        hp       = hp[ind2keep]
        hx       = hx[ind2keep]
        
        # time vector initiate at 0
        t        = t - t[0]
        
        # From cm to m
        hp       = hp/100
        hx       = hx/100
        
        # From m to parsecs
        hp       = hp/3.0857e16
        hx       = hx/3.0857e16
        
        # From parces to Kpc
        hp       = hp/1000
        hx       = hx/1000
        
        h        = hp + hx
        
        
    # ----------------------------------------------
    # Yakunin15
    elif templatename[:3] == 'Yak':
        # Select template
        if   templatename == 'Yak1': filename = 'rhplus-B12-WH07.d'
        elif templatename == 'Yak2': filename = 'rhplus-B15-WH07.d'
        elif templatename == 'Yak3': filename = 'rhplus-B20-WH07.d'
        elif templatename == 'Yak4': filename = 'rhplus-B25-WH07.d'
        else:  print('PILAS: unknown CCSNe GW form the Yakunin15 catalog')

        folder   = 'Yakunin15/'
        fullpath = rutacatalogs + folder + filename
        # Load data  
        t        = np.loadtxt(fullpath,usecols=(0))
        hp       = 0*t
        hx       = 0*t
        h        = np.loadtxt(fullpath,usecols=(1)) # cm
        
        # From cm to 1 Kpc
        h        = h/100        # From cm to m
        h        = h/3.0857e16  # From m to parsecs        
        h        = h/1000       # From parces to 1 Kpc
        
        
    # ----------------------------------------------
    # Unknown catalog of CCSNe GW
    else:
        # Do nothing
        print('PILAS: unknown catalog of CCSNe GW')
    
    
    # ----------------------------------------------
    # Print template name
    print('Template:    ' + folder + templatename)
    
    
    # ---------------------------------------------
    # DO PLOT
    if doplot == 1:
        pylab.figure(1)
        pylab.plot(t,hp,'r',linewidth=2.0)
        pylab.plot(t,hx,'b',linewidth=2.0)
        pylab.xlabel('Time (s)',fontsize=18,color='black')
        pylab.ylabel('Strain',fontsize=18,color='black')
        pylab.grid(True)
        
        pylab.figure(2)
        pylab.plot(t,h,linewidth=2.0)
        pylab.xlabel('Time (s)',fontsize=18,color='black')
        pylab.ylabel('Strain',fontsize=18,color='black')
        pylab.grid(True)    
    
    
    # ---------------------------------------------
    # RETURN OUTPUT DATA
    return t,hp,hx,h

