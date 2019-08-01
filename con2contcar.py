# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:14:31 2019

@author: Vacian
"""
poslines=[]
with open ("cont",'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for line in lines:
            poslines.append(line.strip().split())
cellx=poslines[1]
celly=poslines[2]
cellz=poslines[3]
atoms=poslines[5:]
element=[]
slect=0
for i in range(0,len(atoms)):
    if len(atoms[i]) == 7:
        slect=1
        break
for i in range(0,len(atoms)):
    element.append(atoms[i][0])
    if slect == 1:
        if len(atoms[i]) == 7:
            for x in range(4,7):
                if "0" == atoms[i][x]:
                    atoms[i][x]="F"
                else:
                    atoms[i][x]="T"
        else:
            atoms[i].append("T")
            atoms[i].append("T")
            atoms[i].append("T")
        atoms[i]=atoms[i][1:]
    else:
        atoms[i]=atoms[i][1:]
elementset=sorted(set(element),key=element.index)
atomnumber=[]
for i in range(0,len(elementset)):
    atomnumber.append(str(element.count(elementset[i])))
with open("contcar.vasp",'w') as f:
    f.write("QEformat"+"\n")
    f.write("  1.0"+"\n")
    f.write("   ".join(cellx)+"\n")
    f.write("   ".join(celly)+"\n")
    f.write("   ".join(cellz)+"\n")
    f.write("   ".join(elementset)+"\n")
    f.write("   ".join(atomnumber)+"\n")
    if slect == 1:
        f.write("S"+"\n")
    f.write("Direct"+"\n")
    for i in range(0,len(atoms)):
        f.write("   ".join(atoms[i])+"\n")
