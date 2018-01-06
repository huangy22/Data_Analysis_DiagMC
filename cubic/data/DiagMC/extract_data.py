#!/usr/bin/env python
import numpy as np
import os, sys
import IO

filelist = IO.LoadDict("filelist")

for file in filelist['files']:
    print "Extracting "+file+"_Dyson_Output ..."
    try:
        Dict=IO.LoadDict("./OriginalData/"+file+"_Dyson_Output.txt")
    except:
        Dict={}  
        print "No such file!"

    ErrDict={}
    for quan in Dict.keys():
        start= int(len(Dict[quan])/3)
        print len(Dict[quan]), start
        value=Dict[quan][-1]
        error=(max(Dict[quan][start:], key=lambda x:x.real)-min(Dict[quan][start:], key=lambda x:x.real))/2
        ErrDict[quan]={}
        ErrDict[quan]["value"]=value
        ErrDict[quan]["error"]=error
    IO.SaveDict("./"+file+"_Dyson_Err.txt", "w", ErrDict)


###SINGLE FILE
#try:
    #Dict=IO.LoadDict("../From_Cluster/data/OriginalData/L8_Beta1.5_Order5_Dyson_Output_old.txt")
#except:
    #Dict={}  
    #print "No such file!"

#ErrDict={}
#for quan in Dict.keys():
    #start= int(len(Dict[quan])/3)
    #print len(Dict[quan]), start
    #if quan=="Chi_X(4Pi,2Pi,0)":
        #value=Dict[quan][-1][-1][0]
        #data=[]
        #for i in range(start, len(Dict[quan])):
            #data.append(Dict[quan][i][1][0])
        #error=(max(data, key=lambda x:x.real)-min(data, key=lambda x:x.real))/2
    #else:
        #value=Dict[quan][-1]
        #error=(max(Dict[quan][start:], key=lambda x:x.real)-min(Dict[quan][start:], key=lambda x:x.real))/2

    #ErrDict[quan]={}
    #ErrDict[quan]["value"]=value
    #ErrDict[quan]["error"]=error
#IO.SaveDict("../From_Cluster/data/L8_Beta1.5_Order5_Dyson_Err_old.txt", "w", ErrDict)



