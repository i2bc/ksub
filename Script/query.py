import os
input_path = "/store/EQUIPES/SSFA/nikita.lagrange/filtre2/cancer"
output_path = "/store/EQUIPES/SSFA/nikita.lagrange/result_reindeer/cancer"
file = open("query.sh","w")
file.write("#!/bin/bash"+"\n")
file.write("#PBS -q common"+"\n")
file.write("#PBS -l select=ncpus=1:mem=80gb"+"\n"+"\n")
l = os.listdir(input_path)
for f in l:
    file.write("/home/nikita.lagrange/R/REINDEER/Reindeer --query -l /data/work/I2BC/nikita.lagrange/idx_1 -q "+input_path+"/"+f+" -P 100 -o "+output_path+"\n")
file.close()