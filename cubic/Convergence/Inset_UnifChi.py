#!/usr/bin/env python
import numpy as np
import os, matplotlib
from matplotlib import rc
from pylab import *
import IO

if "DISPLAY" not in os.environ:
    matplotlib.use('Agg')
import matplotlib.pyplot as plt

def PlotInset(InBeta, InOrder, InData, InErr, OutBeta, OutData, OutErr, OutLabel, DoesSave=True):
    import itertools
    rc('font', family='serif')

    ax = axes()
    marker = itertools.cycle(('*', 's', 'v', '^', 'o')) 
    color = itertools.cycle(('b', 'c', 'g', 'm', 'r')) 

    for i in range(len(OutData)):
        if OutLabel[i]=="DiagMC":
            errorbar(1.0/np.array(OutBeta[i]), np.array(OutData[i])/3.0, yerr=np.array(OutErr)/3.0, marker=marker.next(), color=color.next(), ls='-', label=OutLabel[i])
        else:
            plot(1.0/np.array(OutBeta[i]), np.array(OutData[i]), marker=marker.next(), color=color.next(), ls='-', label=OutLabel[i])

    ylim(0.0, 0.125)
    xscale("log")
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax.set_xticks([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])
    ax.set_xticklabels([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])

    ylabel("Static Uniform Susceptibility $\chi_u$", fontsize=15)
    xlabel('T/J', fontsize=15)
    legend(loc="best",prop={"size":15})
    #text(7.0, 0.01, "(b)", fontsize=15,  color='black') 

    a = axes([0.2, 0.18, .31, .31], axisbg='w')
    errorbar(1.0/np.array(InOrderList), np.array(InData)/3.0, yerr=np.array(InErr)/3.0, label='T/J={0}'.format(1.0/InBeta), marker='o', markersize=3, ls='-', color='r')

    xscale("log")
    a.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    a.set_xticks([0.1, 0.2, 0.5, 1.0])
    a.set_xticklabels([0.1, 0.2, 0.5, 1.0])
    xlabel('1/N', fontsize=10)
    ylim(0.085, 0.105)
    yticks(np.arange(0.085, 0.115, 0.01))

    #plot([0.0, 1.0/3.0], [0.0896, 0.0896], 'm-')
    xlim(0.1)
    axhspan(0.0881, 0.0911, facecolor='b', ec='none', alpha=0.2)
    text(1.0/3.0, 0.0894, r"$\chi_u=0.0896(15)$", fontsize=12,  color='black') 
    #text(0.8, 0.086, "(a)", fontsize=10,  color='black') 

    legend(loc='best', prop={"size":10})

    if DoesSave:
        savefig("UnifChi_Inset.pdf")
    else:
        show()
    close()

if __name__=="__main__":
    import IO

    path="../../From_Cluster/data/"

    InBeta=2.0
    InOrderList=[1, 2, 3, 4, 5, 6]

    InData=[]
    InErr=[]
    for Order in InOrderList:
        file="L8_Beta"+str(InBeta)+"Order"+str(Order)+"_Dyson_Err"
        InData.append(IO.LoadDict(path+file)["UnifChi"]["value"])
        InErr.append(IO.LoadDict(path+file)["UnifChi"]["error"])

    OutChi = []
    OutLabel = []
    OutBeta = []

    OutChi.append(np.array(IO.LoadDict("HTE_UnifChi")["UnifChi_Order5"]))
    OutLabel.append("HTE_Order5")
    OutBeta.append(np.array(IO.LoadDict("HTE_UnifChi")["Beta"]))

    OutChi.append(np.array(IO.LoadDict("HTE_UnifChi")["UnifChi_Order6"]))
    OutLabel.append("HTE_Order6")
    OutBeta.append(np.array(IO.LoadDict("HTE_UnifChi")["Beta"]))

    OutChi.append(np.array(IO.LoadDict("HTE_UnifChi")["UnifChi_Order7"]))
    OutLabel.append("HTE_Order7")
    OutBeta.append(np.array(IO.LoadDict("HTE_UnifChi")["Beta"]))

    OutChi.append(np.array(IO.LoadDict("HTE_UnifChi")["UnifChi_Order8"]))
    OutLabel.append("HTE_Order8")
    OutBeta.append(np.array(IO.LoadDict("HTE_UnifChi")["Beta"]))

    BetaDiag= [0.1,    0.2,   0.3,   0.5,   0.8,   1.0,   1.5, 2.0,     3.0,   4.0,5.0,6.0]
    OutErr =  [0.001, 0.001, 0.001, 0.002, 0.002, 0.002, 0.002, 0.002, 0.003, 0.004, 0.006, 0.010]
    ChiDiag=[]
    for i in range(len(BetaDiag)):
        if i<3:
            f="../../From_Cluster/data/L8_Beta{0}Order0_Dyson_Err".format(BetaDiag[i])
        else:
            f="../../From_Cluster/data/L8_Beta{0}Order4_Dyson_Err".format(BetaDiag[i])
        ChiDiag.append(abs(IO.LoadDict(f)["UnifChi"]["value"]))

    OutChi.append(ChiDiag)
    OutLabel.append("DiagMC")
    OutBeta.append(BetaDiag)

    PlotInset(InBeta, InOrderList, InData, InErr, OutBeta, OutChi, OutErr, OutLabel, False)
    PlotInset(InBeta, InOrderList, InData, InErr, OutBeta, OutChi, OutErr, OutLabel)
