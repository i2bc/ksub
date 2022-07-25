file = open("sample_conditions_full_SEO.tsv","r")
nf = []
for line in file:
    if line[0]!="s" and line.split()[1]=="normal":
        nf.append(line.split()[0])

path_fastq = "/store/EQUIPES/SSFA/Data/LUAD/LUADseo/trim_corfq/"
path_bcalm = "/home/nikita.lagrange/R/REINDEER/bin/bcalm"
path_out = "/store/EQUIPES/SSFA/nikita.lagrange/bcalm"

file = open("bcalm.sh","w")
file.write("#!/bin/bash \n\n#PBS -q common \n#PBS -l ncpus=8 \n\n")
for f in nf:
    file.write(path_bcalm+" -in "+path_fastq+f+"_1.trim.cor.fq.gz"+" -in "+path_fastq+f+"_2.trim.cor.fq.gz -abundance-min 3 -kmer-size 31 -out-dir "+path_out+" -nb-cores 16 \n")
file.close()  
