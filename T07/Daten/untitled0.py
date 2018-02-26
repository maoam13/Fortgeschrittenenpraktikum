# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:28:23 2018

@author: morit
"""

file = open("C:\Users\morit\Desktop\T07\ALL0000\F0000CH1.CSV")
csv_reader = csv.reader(file, delimiter=",")
x = []
y = []
for row in csv_reader:
    wert = row[4]
    wert = float(wert)
    y.append(wert)
    
    wert = row[3]
    wert = float(wert)
    x.append(wert)
file.close()

plt.figure(3)
plt.plot(x,y)
