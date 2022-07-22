file = open("sample_conditions_full_SEO.tsv","r")
nf = []
for line in file:
    if line[0]!="s":
        nf.append(line.split()[0])
file = open("QC.sh","w")
file.write("#!/bin/bash \n\n#PBS -q common \n#PBS -M nikita.lagrange@i2bc.paris-saclay.fr \n#PBS -l ncpus=16 \n\n")
file.write("/home/nikita.lagrange/miniconda3/bin/fastqc --noextract --threads 32 --outdir /store/EQUIPES/SSFA/nikita.lagrange/QC")
for f in nf:
    file.write(" /store/EQUIPES/SSFA/Data/LUAD/LUADseo/trim_corfq/"+f+"_1.trim.cor.fq.gz /store/EQUIPES/SSFA/Data/LUAD/LUADseo/trim_corfq/"+f+"_2.trim.cor.fq.gz")
file.close()  