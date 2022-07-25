import os
import numpy as np

path_in = "/store/EQUIPES/SSFA/nikita.lagrange/filtre1/cancer" 
path_jc = "/store/EQUIPES/SSFA/nikita.lagrange/JC"
path_out = "/store/EQUIPES/SSFA/nikita.lagrange/filtre2/cancer"

l = os.listdir(path_jc)

for f in l:
    name = f.split("_")[1]
    file_in = open(path_in+"/"+name+".fa","r")
    ft = []
    sq = []
    for line in file_in:
        if line[0]==">":
            ft.append(line.strip())
        else:
            sq.append(line.strip())
    file_in.close()
    JC = []
    file_jc = open(path_jc+"/"+f,"r")
    for line in file_jc:
        JC.append(float(line))
    file_jc.close()
    JC = np.array(JC)
    filtre = np.where(JC!=100)[0]
    file_out = open(path_out+"/"+name+".fa","w")
    for i in filtre:
        file_out.write(ft[i]+"\n"+sq[i]+"\n")
    file_out.close()