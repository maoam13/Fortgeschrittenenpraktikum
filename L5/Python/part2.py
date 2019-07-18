import Praktikum as p
import os
import auswertung_nur_Methoden as AM
import numpy as np
import matplotlib.pyplot as plt
import peaks_func as pf


G, D = [], []
for i in range(1, 6):
    name = '4 Half sandwich on PMMA/Half ' + str(i) + '.txt'
    __G, __D = pf.peaks(name)
    G.append(__G)
    D.append(__D)

print(G)
print(D)
