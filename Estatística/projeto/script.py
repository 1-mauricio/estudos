from numpy.lib.function_base import copy
import pandas as pd
import numpy as np
import random

dataframe = pd.read_csv('data.csv')
dataframe = dataframe.to_numpy()
dataframe2 = []*1000
for i in range(len(dataframe)):
    dataframe2.append(dataframe[i][0])


dataframe2.sort()

def_420p = dataframe2[0:334]
def_720p = dataframe2[334:667]
def_1080p = dataframe2[667:1001]


nav_a1 = []
nav_a2 = []
nav_a3 = []
nav_b1 = []
nav_b2 = []
nav_b3 = []

nav_a1.append(def_420p[0:167])
nav_b1.append(def_420p[167:334])
nav_a2.append(def_720p[0:167])
nav_b2.append(def_720p[167:334])
nav_a3.append(def_1080p[0:167])
nav_b3.append(def_1080p[167:334])


for i in range(40):
    val = random.choice(nav_b1[0])
    nav_a1[0].append(val)
    nav_b1[0].remove(val)

for i in range(40):
    val = random.choice(nav_a1[0])
    nav_b1[0].append(val)
    nav_a1[0].remove(val)

for i in range(40):
    val = random.choice(nav_b2[0])
    nav_a2[0].append(val)
    nav_b2[0].remove(val)

for i in range(40):
    val = random.choice(nav_a2[0])
    nav_b2[0].append(val)
    nav_a2[0].remove(val)

for i in range(40):
    val = random.choice(nav_b3[0])
    nav_a3[0].append(val)
    nav_b3[0].remove(val)

for i in range(40):
    val = random.choice(nav_a3[0])
    nav_b3[0].append(val)
    nav_a3[0].remove(val)

nav_a = nav_a1[0] + nav_a2[0] + nav_a3[0]
nav_b = nav_b1[0] + nav_b2[0] + nav_b3[0]

#print(nav_a)
#df = pd.DataFrame(nav_a)
#df.to_csv('test.csv')
np.savetxt("nav_a.csv", nav_a, delimiter=",", fmt="%f")


np.savetxt("nav_b.csv", nav_b, delimiter=",", fmt="%f")