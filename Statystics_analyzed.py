import os
import csv
import numpy as np
import traceback
import re
import pandas as pd
import glob

#data = np.loadtxt("Des___00DKO_00709_analyzed.txt", dtype=np.object, delimiter=",",skiprows=1, usecols=(2, 3, 4, 6, 7)) #use length, speed, RD, DP and DI columns from initial file.
data = np.genfromtxt("Des___00DKO_00709_analyzed.txt", delimiter=",",skip_header=1, usecols=(4, 6, 7)) #use length, speed, RD, DP and DI columns from initial file.
#print (data)
a = np.array([data])
#rd = a[:, [1, 2]]
#print(rd)
a.shape
print(a.shape)
#rd = np.array(data(usecols=4))
