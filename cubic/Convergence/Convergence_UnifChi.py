#!/usr/bin/env python
import numpy as np
import os, matplotlib
from matplotlib import rc
from pylab import *
import IO

if "DISPLAY" not in os.environ:
    matplotlib.use('Agg')
import matplotlib.pyplot as plt

def PlotConvergence(InBeta, InOrder, InData, InErr, HTE, DoesSave=True):
    import itertools
    rc('font', family='serif')
    a = axes()
    #errorbar(1.0/np.array(InOrderList), InData, yerr=2.0*np.array(InErr), label='T/J={0}'.format(1.0/InBeta), marker='o', markersize=5, ls='-', color='r')
    errorbar(np.array(InOrderList), np.array(InData)/3.0, yerr=np.array(InErr)/1.5, label='T/J={0}'.format(1.0/InBeta), marker='o', markersize=5, ls='-', color='black')

    xlim(0.0, 7.0)
    xlabel('N', fontsize=15)
    ylabel('$\chi_u$', rotation=0, fontsize=20)

    ##########For Beta=0.5 ################################################
    #xlim(0.05, 1.0)
    #xscale("log")
    #a.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    #a.set_xticks([0.05, 0.1, 0.2, 0.5, 1.0])
    #a.set_xticklabels([0.05, 0.1, 0.2, 0.5, 1.0])
    #xlabel('1/N', fontsize=15)
    #text(1.0/2.5, 0.1966, r"$\chi_u=0.1966(8)$", fontsize=20,  color='black') 
    #plot([0.0, 1.0/2.0], [HTE, HTE], 'm-')

    ylim(0.065, 0.067)
    yticks(np.arange(0.065, 0.067, 0.0004))

    plot([3.0, 7.0], [HTE, HTE], 'r-')

    #axhspan(0.0, 0.1974, facecolor='b', ec='none', alpha=0.2)
    text(4.5, 0.0653, "HTE $\chi_u=${0:.4f}".format(HTE), fontsize=15,  color='r') 
    ######################################################################

    ##########For Beta=0.8 ################################################
    #xlim(0.05, 1.0)
    #xscale("log")
    #a.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    #a.set_xticks([0.05, 0.1, 0.2, 0.5, 1.0])
    #a.set_xticklabels([0.05, 0.1, 0.2, 0.5, 1.0])
    #xlabel('1/N', fontsize=15)
    #text(1.0/2.5, 0.1966, r"$\chi_u=0.1966(8)$", fontsize=20,  color='black') 
    #plot([0.0, 1.0/2.0], [HTE, HTE], 'm-')

    #ylim(0.192, 0.202)
    #yticks(np.arange(0.192, 0.202, 0.002))
    ######################################################################

    legend(loc='best', prop={"size":15})

    if DoesSave:
        savefig(str(InBeta)+"_UnifChi_Convergence.pdf")
    else:
        show()
    close()

if __name__=="__main__":
    import IO

    path="../../From_Cluster/data/"

    InBeta=0.5
    InOrderList=[1, 2, 3, 4, 5, 6]

    InData=[]
    InErr=[]
    for Order in InOrderList:
        file="L8_Beta"+str(InBeta)+"Order"+str(Order)+"_Dyson_Err"
        InData.append(IO.LoadDict(path+file)["UnifChi"]["value"])
        InErr.append(IO.LoadDict(path+file)["UnifChi"]["error"])
    
    HTE = IO.LoadDict("HTE_UnifChi.txt")
    Tot = 0.0
    for i in range(len(HTE["Beta"])):
        if HTE["Beta"][i]==InBeta:
            Tot += HTE["UnifChi_Order5"][i]
            Tot += HTE["UnifChi_Order6"][i]
            Tot += HTE["UnifChi_Order7"][i]
            Tot += HTE["UnifChi_Order8"][i]
            Tot = Tot/4.0

    PlotConvergence(InBeta, InOrderList, InData, InErr, Tot, False)
    PlotConvergence(InBeta, InOrderList, InData, InErr, Tot, )
