import IO
import numpy as np
DOWN, UP=0,1
d=IO.LoadBigDict("./Beta1.0_Order4_Tau32_L8_Weight.hkl")
GammaG=d["GammaG"]["SmoothT"]
print "GammaG, dyson=\n",  0.5*(np.sum(GammaG[DOWN, :, :, :]-GammaG[UP, :, :, :], axis=0)).diagonal()
