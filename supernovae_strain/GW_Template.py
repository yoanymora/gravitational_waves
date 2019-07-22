#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 16:22:15 2018

@author: gravwaves
"""



# =============================================
# IMPORT LIBRARIES
# =============================================
from pycbc import types
from scipy.interpolate import CubicSpline
import pylab
import numpy as np
import GW_CCSNeFromCatalog





# =============================================
# FUNCTION TO READ TEMPLATE
# =============================================
def Read(templatename,fs,doplot):
    
    
    # ---------------------------------------------
    # READ THE TEMPLATE (RAW DATA)
    t,hp,hx,h = GW_CCSNeFromCatalog.Read(templatename,0)
    
    
    # ---------------------------------------------
    # COMPUTE STRAIN h(t) = F+ h+ + Fx hx
    
    
    # ---------------------------------------------
    # RESAMPLING TEMPLATE AT FS
    
    # Make sure that initial time is zero
    t        = t - t[0]
    
    # Create the new time vector for the new sampling frequency
    tend     = t[len(t)-1]
    tnew     = np.arange(0,tend,(1.0/fs))

    # Do de interpolation
    hs       = CubicSpline(t,h)
    hh       = hs(tnew)
    
    
    # ---------------------------------------------
    # CREATE TIME SERIES OBJECT
    template = types.TimeSeries(initial_array=hh,delta_t=1.0/fs,epoch=0)
    
    
    # ---------------------------------------------
    # DO PLOT
    if doplot == 1:        
        pylab.figure()
        pylab.plot(t,h,'r',label='Original')
        pylab.plot(tnew,hh,'b',label='Resampled')
        pylab.xlabel('Time (s)',fontsize=18)
        pylab.ylabel('Strain',fontsize=18)
        pylab.grid(True)
        pylab.legend()
        pylab.show()
        
        pylab.figure()
        pylab.plot(template.sample_times,template)
        pylab.xlabel('Time (s)',fontsize=18,color='black')
        pylab.ylabel('Strain',fontsize=18,color='black')
        pylab.grid(True)
        pylab.show()

    
    # ---------------------------------------------
    # RETURN OUTPUT DATA
    return template





# =============================================
# FUNCTION TO RESIZE TEMPLATE
# =============================================
def Resize(template,strain,doplot):
    
    
    # ---------------------------------------------
    # RESIZE
    template.resize(len(strain))
    
    
    # ---------------------------------------------
    # DO PLOT
    if doplot == 1:
        pylab.figure
        pylab.plot(template.sample_times,template)
        pylab.title('Template',fontsize=18)
        pylab.xlabel('Time (s)',fontsize=18,color='black')
        pylab.ylabel('Strain',fontsize=18,color='black')
        pylab.grid(True)
        pylab.show()
    
    
    # ---------------------------------------------
    # RETURN OUTPUT DATA
    return template