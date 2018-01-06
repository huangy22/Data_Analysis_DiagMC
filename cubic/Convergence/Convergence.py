#!/usr/bin/env python
import numpy as np
import os, matplotlib
import IO

if "DISPLAY" not in os.environ:
    matplotlib.use('Agg')
import matplotlib.pyplot as plt

def PlotConvergence(BetaList, OrderList, Data, Err, Quan, Name, Label, DoesSave, IsNew=True, IsLast=True):
    if IsNew:
        plt.figure()
    for Beta in BetaList:
        plt.errorbar(1.0/np.array(OrderList[Beta]), Data[Beta], yerr=2.0*np.array(Err[Beta]), label="T/J= {0}".format(1.0/Beta), ls='-')

    plt.xlabel("1/N", fontsize=20)
    plt.ylabel(Label, fontsize=25)

    if IsLast:
        plt.legend(loc='best')
        if DoesSave:
            plt.savefig(Name+Quan+"_Convergence.eps", format="eps")
        else:
            plt.show()
        plt.close()

####For the data that enforced Sum Rule
#def PlotConvergence_SR(BetaList, OrderList, Data, Err, Quan, Label, DoesSave, IsNew=True, IsLast=True):
    #if IsNew:
        #plt.figure()
    #for Beta in BetaList:
        #plt.errorbar(1.0/np.array(OrderList[Beta]), Data[Beta], yerr=2.0*np.array(Err[Beta]), label="T/J= {0}, Sum Rule enforced".format(1.0/Beta), ls='-')

    #plt.xlabel("1/N", fontsize=25)
    #plt.ylabel(Label, fontsize=20)

    #if IsLast:
        #plt.legend(loc='best', prop={"size":20})
        ##plt.xlim(0)
        ##plt.ylim(0.24)
        #if DoesSave:
            #plt.savefig(Quan+"_Convergence_SR.pdf")
        #else:
            #plt.show()
        #plt.close()

if __name__=="__main__":
    import IO

    path="../data/DiagMC/"
    path0="../data/PathIntegral/"
    QuanList=["UnifChi","StagChi","<Sz_1>"]
    PathIntegralQuanList=["UnifChi","StagChi","StagMag"]
    LabelList=["$\chi_u$","$\chi_{stag}$", "$M_{stag}$"]

    #BetaList=[0.25, 0.33, 0.5, 1.0]
    #BetaList=[1.0]
    BetaList=[0.5]
    OrderList={}

    #h=1.0
    #Name="L8_H1.0_"
    #OrderList[0.25]=[1, 2, 3, 1000] 
    #OrderList[0.33]=[1, 2, 3, 1000] 
    #OrderList[0.5]=[1, 2, 3, 1000] 
    #OrderList[1.0]=[1, 2, 3, 4, 5, 6, 1000] 

    h=0.5
    Name="L8_H0.5_"
    OrderList[0.25]=[1, 2, 3, 1000] 
    OrderList[0.33]=[1, 2, 3, 1000] 
    OrderList[0.5]=[1, 2, 3, 1000] 
    OrderList[1.0]=[1, 2, 3, 4, 5, 6, 1000] 
    OrderList[1.5]=[1, 2, 3, 4, 5, 6, 1000] 

    #h=0.25
    #Name="L8_H0.25_"
    #OrderList[0.25]=[1, 2, 3, 1000] 
    #OrderList[0.33]=[1, 2, 3, 1000] 
    #OrderList[0.5]=[1, 2, 3, 1000] 
    #OrderList[1.0]=[1, 2, 3, 4, 5, 6, 1000] 
    #OrderList[1.5]=[1, 2, 3, 1000] 



    for i in range(len(QuanList)):
        Data={}
        Err={}
        quan = QuanList[i]
        quan0 = PathIntegralQuanList[i]
        label = LabelList[i]
        for Beta in BetaList:
            Data[Beta]=[]
            Err[Beta]=[]
            for Order in OrderList[Beta]:
                if Order==1000:
                    file="L8_Beta"+str(Beta)+"_H"+str(h)+"_ext_hs_sqa0"
                    Data[Beta].append(IO.LoadDict(path0+file)[quan0]["value"])
                    Err[Beta].append(IO.LoadDict(path0+file)[quan0]["error"])

                else:
                    file="L8_Beta"+str(Beta)+"_H"+str(h)+"_Order"+str(Order)+"_Dyson_Err"
                    Data[Beta].append(IO.LoadDict(path+file)[quan]["value"])
                    Err[Beta].append(IO.LoadDict(path+file)[quan]["error"])

        PlotConvergence(BetaList, OrderList, Data, Err, quan, Name, label, False)
        PlotConvergence(BetaList, OrderList, Data, Err, quan, Name, label, True)

       ##########SUM RULE PLOT#####################################
        #for Beta in BetaList:
            #Data[Beta]=[]
            #Err[Beta]=[]
            #for Order in OrderList[Beta]:
                #file="SR_L8_Beta"+str(Beta)+"Order"+str(Order)+"_Dyson_Err"
                #Data[Beta].append(IO.LoadDict(path+file)[quan]["value"])
                #Err[Beta].append(IO.LoadDict(path+file)[quan]["error"])

        ##PlotConvergence(BetaList, OrderList, Data, Err, quan, False, IsLast=False)
        #PlotConvergence(BetaList, OrderList, Data, Err, quan, True, IsSR=True, IsNew=False)

