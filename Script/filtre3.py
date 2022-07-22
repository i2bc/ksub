import statsmodels.api as SM
from scipy.stats import nbinom
import numpy as np
import os

# REINDEER query results path
path_query = "/store/EQUIPES/SSFA/nikita.lagrange/result_reindeer/cancer_1/query_results"
# BN parameters path
path_params = "/store/EQUIPES/SSFA/nikita.lagrange/params_BN/cancer_1/"
# path of the sequences that passed the BN filter
path_filtre = "/store/EQUIPES/SSFA/nikita.lagrange/filtre3/cancer_1/"
# FASTA files path
path_file = "/store/EQUIPES/SSFA/nikita.lagrange/normalisation/cancer/"
file = open("normalization_factor.txt", "r")
dico_norm = {}
for line in file:
    k, v = line.split()
    dico_norm[k] = float(v)
file = open("fof.txt", "r")
F = []
for line in file:
    if "ERR" in line:
        F.append(line.strip().split("_")[0])
    else:
        F.append(line.strip().split(".")[0])
file.close()

list_file = os.listdir(path_query)

p0 = 0.9734166040720748
n0 = 0.00029413385899137377

l0 = int(nbinom.interval(0.99, n0, p0)[0])
u0 = int(nbinom.interval(0.99, n0, p0)[1])

for name_file in list_file:
    file = open(path_query+"/"+name_file, "r")
    i = 1
    name = name_file.split("_")[-2]
    file_fasta = open(path_file+name+".fa", "r")
    dico_ft_seq = {}
    for line in file_fasta:
        if line[0] == ">":
            ft = line.strip()
        else:
            seq = line.strip()
            dico_ft_seq[ft] = seq
    path_file.close()
    file_params = open(path_params + name, "w")
    file_params.write("N"+"\t"+"P"+"\n")
    file_filtre = open(path_filtre + name+".tsv", "w")
    file_filtre.write("contig"+"\t"+"tag"+"\n")
    # Reading REINDEER results
    for line in file:
        count_query = int(line.split()[0].split("_")[-1])
        ft = line.split()[0]
        distrib = []
        counts = line.split()[1:]
        ix = 0
        for c in counts:
            name_col = F[ix]
            nf = dico_norm[name_col]
            if c == "*":
                distrib.append(0)
            elif "," in c:
                list_c = c.split(",")
                num = 0
                den = 0
                for v in list_c:
                    cm = float(v.split(":")[1])*nf
                    i = int(v.split(":")[0].split("-")[0])
                    j = int(v.split(":")[0].split("-")[1])
                    num += (j-i+1)*cm
                    den += (j-i+1)
                count = int(round(num/den))
                if count == 0:
                    count = 1
                distrib.append(count)
            else:
                count = round(float(c.split(":")[1])*nf)
                if count == 0:
                    count = 1
                distrib.append(count)
            ix += 1
        # Learning BN parameters
        X = np.ones_like(distrib)
        if sum(distrib) != 0:
            res = SM.NegativeBinomial(distrib, X).fit(start_params=[1, 1], disp=0)
            p = 1/(1+np.exp(res.params[0])*res.params[1])
            n = np.exp(res.params[0])*p/(1-p)
            lower, upper = nbinom.interval(0.99, n, p)
            N = n
            P = p
        else:
            N = n0
            P = p0
            lower, upper = u0, u0
        file_params.write(str(N)+"\t"+str(P)+"\n")
        if count_query > upper:
            seq = dico_ft_seq[ft]
            f = ">"+str(i)+"_"+str(count_query)
            file_filtre.write(seq+"\t"+f+"\n")
            i += 1
    file.close()
    file_params.close()
    file_filtre.close()
