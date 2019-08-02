# -*- coding: utf-8 -*-
"""
@author: Xuan Ai
"""
import os
import shutil

#获取当前路径和设置mass和PS路径
pwd=os.getcwd()
os.mkdir(pwd+"/potfiles")
psdirs='~/ps'
massfile='~/mass'
potfile=pwd+"/potfiles/pot"
#读取POSCAR和各元素相对原子质量文件
poslines=[]
with open ("POSCAR",'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for line in lines:
            poslines.append(line.strip().split())
masslines=[]
with open (massfile,'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for line in lines:
            masslines.append(line.strip().split())
#元素符号
elements=poslines[5]
#矢量
cellx=poslines[2]
celly=poslines[3]
cellz=poslines[4]
#一些文字
a="CELL_PARAMETERS (angstrom)"
b="ATOMIC_POSITIONS (crystal)"
#各原子数量
elementnumber=poslines[6]
#ps部分
elename=[]
for i in range(0,len(masslines)):
    elename.append(masslines[i][0])
pot=[]
for i in range(0,len(elements)):
    pot.append([])
    pot[i].append(elements[i])
    p=elename.index(elements[i])
    pot[i].append(masslines[p][1])
    psdir=psdirs+"/"+elements[i]
    pslist=os.listdir(psdir)
    for x in range(0,len(pslist)):
        print(str(x+1)+"  "+pslist[x])
    sle=int(input("Please slect:\n"))-1
    pot[i].append(pslist[sle])
    pspath=psdir+"/"+pslist[sle]
    pspathout=pwd+"/potfiles/"+pslist[sle]
    print(pspath)
    print(pspathout)
    shutil.copyfile(pspath,pspathout)
with open(potfile,'w') as f:
    f.write("ATOMIC_SPECIES"+"\n")
    for i in range(0,len(pot)):
        f.write(("   ").join(pot[i])+"\n")
#pos部分
if 'S' in poslines[7][0]:
    index=9
    tf=1
else:
    index=8
    tf=0
atoms=[]
atomnumber=0
for i in elementnumber:
    atomnumber=atomnumber+int(i)
for i in range(0,len(elementnumber)):
    for x in range(index,int(elementnumber[i])+index):
        if tf == 1:
            if "F" in poslines[x]:
                for n in range(3,6):
                    if 'F' == poslines[x][n]:
                        poslines[x][n]="0"
            else:
                poslines[x]=poslines[x][0:3]
        atoms.append(elements[i].split()+poslines[x])
        index=index+1
with open("pos",'w') as f:
    f.write(a+"\n")
    f.write(("   ").join(cellx)+"\n")
    f.write(("   ").join(celly)+"\n")
    f.write(("   ").join(cellz)+"\n")
    f.write("\n")
    f.write(b+"\n")
    for i in range(0,len(atoms)):
        f.write(("   ").join(atoms[i])+"\n")
