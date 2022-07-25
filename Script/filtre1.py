import os
file = open("normalisation_factor","r")
dico_norm = {}
for line in file:
    k,v = line.split()
    dico_norm[k] = float(v)
path_in = "/store/EQUIPES/SSFA/nikita.lagrange/bcalm"
path_out = "/store/EQUIPES/SSFA/nikita.lagrange/filtre1/cancer" 
l = os.listdir(path_in)
filter_count = 10
for f in l:
    name = f.split("_")[0]
    i = 0
    fn = dico_norm[name]
    file_in = open(path_in+"/"+f,"r")
    file_out = open(path_out+"/"+name+".fa","w")
    flag = 0
    for line in file:
        if line[0]==">":
            ft = line.strip()
            count = float(ft.split()[3].split(":")[-1])
            count_norm = int(round(count*dico_norm[name]))
            if count_norm==0:
                count_norm=1
            if count_norm>=filter_count:
                flag = 1
        elif flag:
            seq = line.strip()
            file_out.write(">"+str(i)+"_"+str(count_norm)+"\n")
            file_out.write(seq+"\n")
            flag = 0
            i+=1
    file_in.close()
    file_out.close()
