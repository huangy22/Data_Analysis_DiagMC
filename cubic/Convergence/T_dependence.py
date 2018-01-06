#!/usr/bin/env python
import numpy as np
import os, matplotlib
import IO

if "DISPLAY" not in os.environ:
    matplotlib.use('Agg')
import matplotlib.pyplot as plt

def PlotDenomT(BetaList, OrderList, Data, Err, DoesSave):
    plt.figure()
    for Order in OrderList:
        plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="Order {0}".format(Order), ls='-')
    plt.yscale("log")
    plt.xscale("log")

    plt.ylabel("$1-J \Pi$", fontsize=20)
    plt.xlabel("T", fontsize=20)
    #plt.xlim(0.0, 1.0)
    plt.legend(loc='best', prop={"size":20})
    if DoesSave:
        plt.savefig("1-JP_vs_T.eps", format="eps")
    else:
        plt.show()
    plt.close()

def PlotUnifChiT(BetaList, OrderList, Data, Err, DoesSave):
    plt.figure()
    for Order in OrderList:
        plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="Order {0}".format(Order), ls='-')
    plt.ylabel("$\\chi_u$", fontsize=25)
    plt.xlabel("T", fontsize=20)
    #plt.ylim(0.0)
    #plt.xlim(0.0, 1.0)
    plt.legend(loc='best', prop={"size":20})
    if DoesSave:
        plt.savefig("UnifChi_vs_T.eps", format="eps")
    else:
        plt.show()
    plt.close()


def PlotStagChiT(BetaList, OrderList, Data, Err, Name, DoesSave):
    plt.figure()
    for Order in OrderList:
        #if Order==0:
            #plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="QMC", ls='-')
        #else:
            #plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="Order {0}".format(Order), ls='-')
        plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="h= {0}".format(Order), ls='-')
    plt.ylabel("$\\chi_{stag}$", fontsize=25)
    plt.xlabel("T", fontsize=20)
    #plt.ylim(0.0)
    plt.xlim(0.0)
    plt.legend(loc='best', prop={"size":20})
    if DoesSave:
        plt.savefig(Name+"StagChi_vs_T.eps", format="eps")
    else:
        plt.show()
    plt.close()

def PlotStagM(BetaList, OrderList, Data, Err, Name, DoesSave):
    plt.figure()
    for Order in OrderList:
        if Order==0:
            plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="QMC", ls='-')
        else:
            plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="Order {0}".format(Order), ls='-')
            #plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="h= {0}".format(Order), ls='-')
    plt.ylabel("$M_{stag}$", fontsize=25)
    plt.xlabel("T", fontsize=20)
    plt.ylim(0.0)
    #plt.xlim(0.0, 1.0)
    plt.legend(loc='best', prop={"size":20})
    if DoesSave:
        plt.savefig(Name+"StagMag_vs_T.eps", format="eps")
    else:
        plt.show()
    plt.close()

def PlotEnergy(BetaList, OrderList, Data, Err, Name, DoesSave):
    plt.figure()
    for Order in OrderList:
        if Order==0:
            plt.errorbar(1.0/BetaList[Order], np.array(Data[Order])/BetaList[Order], yerr=np.array(Err[Order]), label="QMC", ls='-')
        else:
            plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="Order {0}".format(Order), ls='-')
            #plt.errorbar(1.0/BetaList[Order], np.array(Data[Order]), yerr=np.array(Err[Order]), label="h= {0}".format(Order), ls='-')
    plt.ylabel("$E$", fontsize=25)
    plt.xlabel("T", fontsize=20)
    #plt.ylim(0.0)
    #plt.xlim(0.0, 1.0)
    plt.legend(loc='best', prop={"size":20})
    if DoesSave:
        plt.savefig(Name+"Energy_T.eps", format="eps")
    else:
        plt.show()
    plt.close()



def PlotUnifChivsHTE(Beta, Data, Err, Label, DoesSave=True):
    plt.figure()
    for i in range(len(Data)):
        if Label[i]=="DiagMC":
            plt.errorbar(1.0/np.array(Beta[i]), np.array(Data[i]), yerr=Err, marker='o', ls='-', label=Label[i])
        else:
            plt.plot(1.0/np.array(Beta[i]), np.array(Data[i]), 'o', ls='-', label=Label[i])
            
    plt.ylim(0.0)
    plt.xscale("log")

    plt.ylabel("$\\chi_u$", fontsize=20)
    plt.xlabel("T/J", fontsize=15)
    plt.legend(loc="best",prop={"size":15})
    if DoesSave:
        plt.savefig("UnifChi_compared_with_HTE.eps", format="eps")
    else:
        plt.show()
    plt.close()




if __name__=="__main__":
    import IO

    path="../data/DiagMC/"
    path0="../data/PathIntegral/"

    OrderList=[0]
    #OrderList=[0, 1, 2, 3, 4, 5, 6]
    #OrderList=[1, 2, 3]
    #OrderList=[1, 2]
    BetaList={}

    #h=1.0
    #BetaList[0]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[1]=np.array([0.25, 0.33, 0.5, 1.0])
    #BetaList[2]=np.array([0.25, 0.33, 0.5, 1.0])
    #BetaList[3]=np.array([0.25, 0.33, 0.5, 1.0])
    #BetaList[4]=np.array([1.0])
    #BetaList[5]=np.array([1.0])
    #BetaList[6]=np.array([1.0])

    #h=0.5
    #BetaList[0]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[1]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[2]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[3]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[4]=np.array([1.0, 1.5])
    #BetaList[5]=np.array([1.0, 1.5])
    #BetaList[6]=np.array([1.0, 1.5])

    #h=0.25
    #BetaList[0]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[1]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[2]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[3]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[4]=np.array([1.0])
    #BetaList[5]=np.array([1.0])
    #BetaList[6]=np.array([1.0])

    HList=[0.25, 0.2, 0.15, 0.1, 0.05]
    BetaList={}
    #BetaList[1.0]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    #BetaList[0.5]=np.array([0.25, 0.33, 0.5, 1.0, 1.5])
    BetaList[0.25]=np.array([0.555, 0.625, 0.714, 0.74, 0.77, 0.8, 0.833, 1.0])
    BetaList[0.2]=np.array([0.555, 0.625, 0.714, 0.74, 0.77, 0.8, 0.833, 1.0])
    BetaList[0.15]=np.array([0.74, 0.77, 0.8, 0.833, 0.87])
    BetaList[0.1]=np.array([0.77, 0.8, 0.833, 0.87, 0.909, 1.0, 1.25, 1.5])
    BetaList[0.05]=np.array([0.8, 0.833, 0.87, 0.909, 1.0])
    BetaList[0.0]=np.array([0.8, 0.833, 0.909, 1.0, 1.11])


    #Denom={}
    #ErrDenom={}
    #for Order in OrderList:
        #Denom[Order]=[]
        #ErrDenom[Order]=[]
        #for Beta in BetaList[Order]:
            #file="L8_Beta"+str(Beta)+"Order"+str(Order)+"_Dyson_Err"
            #try:
                #Denom[Order].append(IO.LoadDict(path+file)["1-JP"]["value"])
                #ErrDenom[Order].append(IO.LoadDict(path+file)["1-JP"]["error"])
            #except:
                #pass
    #PlotDenomT(BetaList, OrderList, Denom, ErrDenom, True)

    #UnifChi={}
    #ErrUnifChi={}
    #for Order in OrderList:
        #UnifChi[Order]=[]
        #ErrUnifChi[Order]=[]
        #for Beta in BetaList[Order]:
            #file="L8_Beta"+str(Beta)+"Order"+str(Order)+"_Dyson_Err"
            #try:
                #UnifChi[Order].append(IO.LoadDict(path+file)["UnifChi"]["value"])
                #ErrUnifChi[Order].append(IO.LoadDict(path+file)["UnifChi"]["error"])
            #except:
                #pass
    #PlotUnifChiT(BetaList, OrderList, UnifChi, ErrUnifChi, True)

    #ChiX={}
    #ErrChiX={}
    #for Order in OrderList:
        #if Order==0:
            #ChiX[Order]=[]
            #ErrChiX[Order]=[]
            #for Beta in BetaList[Order]:
                #file="L8_Beta"+str(Beta)+"_H"+str(h)+"_ext_hs_sqa0"
                #try:
                    #ChiX[Order].append(IO.LoadDict(path0+file)["StagChi"]["value"]-Beta*1024.0*(IO.LoadDict(path0+file)["StagMag"]["value"])**2.0)
                    #ErrChiX[Order].append(IO.LoadDict(path0+file)["StagChi"]["error"])
                #except:
                    #pass
        #else:
            #ChiX[Order]=[]
            #ErrChiX[Order]=[]
            #for Beta in BetaList[Order]:
                #file="L8_Beta"+str(Beta)+"_H"+str(h)+"_Order"+str(Order)+"_Dyson_Err"
                #try:
                    #ChiX[Order].append(IO.LoadDict(path+file)["StagChi"]["value"]-Beta*1024.0*(IO.LoadDict(path+file)["<Sz_0>"]["value"])**2.0)
                    #ErrChiX[Order].append(IO.LoadDict(path+file)["StagChi"]["error"])
                #except:
                    #pass
    #PlotStagChiT(BetaList, OrderList, ChiX, ErrChiX, "L8_H{0}_".format(h), True)

    #Energy={}
    #ErrEnergy={}
    #for Order in OrderList:
        #if Order==0:
            #Energy[Order]=[]
            #ErrEnergy[Order]=[]
            #for Beta in BetaList[Order]:
                #file="L8_Beta"+str(Beta)+"_H"+str(h)+"_ext_hs_sqa0"
                #try:
                    #Energy[Order].append(IO.LoadDict(path0+file)["Energy"]["value"])
                    #ErrEnergy[Order].append(IO.LoadDict(path0+file)["Energy"]["error"])
                #except:
                    #pass
        #else:
            #Energy[Order]=[]
            #ErrEnergy[Order]=[]
            #for Beta in BetaList[Order]:
                #file="L8_Beta"+str(Beta)+"_H"+str(h)+"_Order"+str(Order)+"_Dyson_Err"
                #try:
                    #Energy[Order].append(IO.LoadDict(path+file)["Energy"]["value"])
                    #ErrEnergy[Order].append(IO.LoadDict(path+file)["Energy"]["error"])
                #except:
                    #pass
    #PlotEnergy(BetaList, OrderList, Energy, ErrEnergy, "L8_H{0}_".format(h), True)

    #StagM={}
    #ErrStagM={}
    #for Order in OrderList:
        #if Order==0:
            #StagM[Order]=[]
            #ErrStagM[Order]=[]
            #for Beta in BetaList[Order]:
                #file="L8_Beta"+str(Beta)+"_H"+str(h)+"_ext_hs_sqa0"
                #try:
                    #StagM[Order].append(IO.LoadDict(path0+file)["StagMag"]["value"])
                    #ErrStagM[Order].append(IO.LoadDict(path0+file)["StagMag"]["error"])
                #except:
                    #pass
        #else:
            #StagM[Order]=[]
            #ErrStagM[Order]=[]
            #for Beta in BetaList[Order]:
                #file="L8_Beta"+str(Beta)+"_H"+str(h)+"_Order"+str(Order)+"_Dyson_Err"
                #try:
                    #StagM[Order].append(IO.LoadDict(path+file)["<Sz_1>"]["value"])
                    #ErrStagM[Order].append(IO.LoadDict(path+file)["<Sz_1>"]["error"])
                #except:
                    #pass
    #PlotStagM(BetaList, OrderList, StagM, ErrStagM, "L8_H{0}_".format(h), False)
    #PlotStagM(BetaList, OrderList, StagM, ErrStagM, "L8_H{0}_".format(h), True)

    ######QMC only########################################################
    ChiX={}
    ErrChiX={}
    for h in HList:
        ChiX[h]=[]
        ErrChiX[h]=[]
        for Beta in BetaList[h]:
            file="L8_Beta"+str(Beta)+"_H"+str(h)+"_ext_hs_sqa0"
            try:
                ChiX[h].append(IO.LoadDict(path0+file)["StagChi"]["value"]-Beta*1024.0*(IO.LoadDict(path0+file)["StagMag"]["value"])**2.0)
                ErrChiX[h].append(IO.LoadDict(path0+file)["StagChi"]["error"])
            except:
                pass
        print 1.0/BetaList[h]
        print ChiX[h]
    PlotStagChiT(BetaList, HList, ChiX, ErrChiX, "L8_QMC_", True)

    StagM={}
    ErrStagM={}
    for h in HList:
        StagM[h]=[]
        ErrStagM[h]=[]
        for Beta in BetaList[h]:
            file="L8_Beta"+str(Beta)+"_H"+str(h)+"_ext_hs_sqa0"
            try:
                StagM[h].append(IO.LoadDict(path0+file)["StagMag"]["value"])
                ErrStagM[h].append(IO.LoadDict(path0+file)["StagMag"]["error"])
            except:
                pass
    PlotStagM(BetaList, HList, StagM, ErrStagM, "L8_QMC_".format(h), True)
    ############################################################################



    #Chi = []
    #Label = []
    #Beta = []

    #Chi.append(np.array(IO.LoadDict("HTE_UnifChi")["UnifChi_Order8"])*3.0)
    #Label.append("HTE_Order8")
    #Beta.append(np.array(IO.LoadDict("HTE_UnifChi")["Beta"]))

    #Chi.append(np.array(IO.LoadDict("HTE_UnifChi")["UnifChi_Order7"])*3.0)
    #Label.append("HTE_Order7")
    #Beta.append(np.array(IO.LoadDict("HTE_UnifChi")["Beta"]))

    #BetaDiag= [0.1, 0.2, 0.3, 0.4, 0.5, 1.0, 1.5,2.0,3.0,4.0,5.0,6.0]
    #Err = [0.001, 0.001, 0.001, 0.001, 0.001, 0.002, 0.002, 0.002, 0.003, 0.004, 0.006, 0.010]
    #ChiDiag=[]
    #for i in range(len(BetaDiag)):
        #if i<4:
            #f="../../From_Cluster/data/L8_Beta{0}Order0_Dyson_Err".format(BetaDiag[i])
        #else:
            #f="../../From_Cluster/data/L8_Beta{0}Order4_Dyson_Err".format(BetaDiag[i])
        ##print f
        #ChiDiag.append(abs(IO.LoadDict(f)["UnifChi"]["value"]))

    #Chi.append(ChiDiag)
    #Label.append("DiagMC")
    #Beta.append(BetaDiag)

    #PlotUnifChivsHTE(Beta, Chi, Err, Label, False)
    #PlotUnifChivsHTE(Beta, Chi, Err, Label)
