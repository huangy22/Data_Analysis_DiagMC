# monte carlo job defintion
MonteCarlo={
"Control": {
    "__Execute" : "./simulator.exe",
    "__Duplicate" :  0,
    "__IsCluster" : False, 
    "__AutoRun" : True,
    },
"Job": {"Sample" : 100000000}  ##0.8 min for 1000000(*1000) Samples in MC
}
Dyson={
"Control": {
    "__Execute" : ["python", "./dyson/main.py"],
    "__Duplicate" : 1,
    "__IsCluster" : MonteCarlo["Control"]["__IsCluster"],
    "__AutoRun" : MonteCarlo["Control"]["__AutoRun"], 
    "__PBSCommand": "#PBS -l mem=5gb"
    },
"Job": {
    "DysonOnly": MonteCarlo["Control"]["__Duplicate"]==0
    #"DysonOnly": False
    }
}

Beta=1.5
Order=3
Common={
"Tau": {"MaxTauBin" : 64, "Beta": Beta},
"Lattice":  {
    #2D lattice
    #"Name": "Square", "NSublat": 1,
    #"Name": "Checkboard", "NSublat": 2,
    #"Name": "Honeycomb", "NSublat": 2,
    #"Name": "Kagome", "NSublat": 3,
    #"L": [8,8]

    #3D lattice
    #"Name": "Cubic", "NSublat": 1,
    "Name": "3DCheckerboard", "NSublat": 2,
    #"Name": "Pyrochlore", "NSublat": 4,
    "L": [8,8,8]
    },
"Model": {
    "Name": "J1J2",
    #"Description": ["ImW",],
    "Interaction": [1.0,0.0],
    "ExternalField": [0.01, -0.01, 0.0, 0.0]
    #ExternalField on Sublattice A and B
    },
}

MonteCarlo["Markov"]={
    "Order": Order, "Sweep" : 10, "Toss" : 1000,
    #Start from order 0, so that OrderReWeight has Order+1 elements
    "OrderReWeight" : [100.0, 0.5, 1.0, 0.1, 0.05, 0.05, 0.01, 0.005],
    "WormSpaceReweight" : 0.05,
    "PolarReweight" : 2.0,
    "OrderTimeRatio" : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    #"Timer": {
        #"PrinterTimer": 300,
        #"DiskWriterTimer": 300,
        #"MessageTimer": 310,
        #"ReweightTimer": 600
        #},
    "Timer": {
        "PrinterTimer": 60,
        "DiskWriterTimer": 60,
        "MessageTimer": 60,
        "ReweightTimer":60
        },
    }

Dyson["Dyson"]={
    "SleepTime": 40,
    #"SleepTime": 300,
    "OrderAccepted": {"Sigma":3, "Polar":3}, "ErrorThreshold": 0.2,
    "Annealing": {
        "DeltaField": [0.2, -0.2, 0.0, 0.0],
        "Interval": [-0.1, +0.1, -0.0, -0.0]
        }
    }

import job_class as job
'''This is the input file of all jobs. 
   You have to add new job objects to TO_DO list
   if you want to run simulation.'''
TO_DO = []
MonteCarlo.update(Common)
TO_DO.append(job.JobMonteCarlo(MonteCarlo))
Dyson.update(Common)
TO_DO.append(job.JobDyson(Dyson))
CPU = 4
SLEEP = 1    #check job status for every SLEEP seconds
