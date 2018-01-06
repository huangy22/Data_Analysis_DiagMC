#!/usr/bin/env python
import numpy as np
import math
import random
import unittest
from logger import *

def GetUnifChi(Order, Beta):
    r = 3.0/4.0  #s(s+1)
    Coeff=np.zeros(8)
    Coeff[0] = r/3
    Coeff[1] = -2*r**2.0/3
    Coeff[2] = 1.0/18*r**2.0*(-3.0+20*r)
    Coeff[3] = -1.0/135*r**2.0*(6.0-91*r+224*r**2.0)
    Coeff[4] = 1.0/1080*r**2.0*(-15.0+376*r-1816*r**2.0+2544*r**3.0)
    Coeff[5] = -1.0/14175*r**2.0*(72.0-2406*r+18909*r**2.0-47188*r**3.0
            +46848.0*r**4.0)
    Coeff[6] = 1.0/2041200*r**2.0*(-4347.0+176346*r-1901709*r**2.0
            +7300134*r**3.0-11982944.0*r**4.0+9482624*r**5.0)
    Coeff[7] = -1.0/61236000*r**2.0*(61560.0-2887056*r+38320749*r**2.0
            -202461642*r**3.0+477409712.0*r**4.0-601876480*r**5.0
            + 399408640*r**6.0)

    Chi = 0.0
    for i in range(Order):
        Chi+=Coeff[i]*(Beta)**(i+1.0)
    return Chi


if __name__=='__main__':
    import IO
    BetaList = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    Dict={}
    Dict["Beta"]=BetaList
    Dict["UnifChi_Order8"]=[]
    Dict["UnifChi_Order7"]=[]
    Dict["UnifChi_Order6"]=[]
    Dict["UnifChi_Order5"]=[]
    for Beta in BetaList:
        Dict["UnifChi_Order8"].append(GetUnifChi(8, Beta))
        Dict["UnifChi_Order7"].append(GetUnifChi(7, Beta))
        Dict["UnifChi_Order6"].append(GetUnifChi(6, Beta))
        Dict["UnifChi_Order5"].append(GetUnifChi(5, Beta))

    IO.SaveDict("HTE_UnifChi", "w", Dict)
    
