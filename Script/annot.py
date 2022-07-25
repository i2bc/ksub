import os

l = "/store/EQUIPES/SSFA/nikita.lagrange/ANNOT/cancer_1"
list_file = os.listdir(l)
po = "/home/nikita.lagrange/config/cancer/"

for n in list_file:
    file = open(po+"config_"+n+".json","w")
    file.write("{"+"\n")
    file.write("\"input_file\": \"/store/EQUIPES/SSFA/nikita.lagrange/filtre3/cancer_1/"+n+".tsv.gz\","+"\n")
    file.write("\"sequence_col\": \"contig\","+"\n")
    file.write("\"id_col\": \"tag\","+"\n")
    file.write("\"map_to\" : [\"human\"],"+"\n")
    file.write("\"human_index\" : \"/store/EQUIPES/SSFA/antoine.laine/General_Annot_Tool/human_index\","+"\n")
    file.write("\"supp_map_to\":[\"ig\",\"human_repeat_ref\",\"rdp\",\"viruses\"],"+"\n")
    file.write("\"ig_fasta\" : \"/store/EQUIPES/SSFA/nikita.lagrange/annot/ig.fasta\","+"\n")
    file.write("\"human_repeat_ref_fasta\" : \"/store/EQUIPES/SSFA/nikita.lagrange/annot/human_repeat_ref.fasta\","+"\n")
    file.write("\"rdp_fasta\" : \"/store/EQUIPES/SSFA/nikita.lagrange/annot/rdp.fasta\","+"\n")
    file.write("\"viruses_fasta\" : \"/store/EQUIPES/SSFA/nikita.lagrange/annot/viruses.fasta\","+"\n")
    file.write("\"output_dir\": \"/store/EQUIPES/SSFA/nikita.lagrange/ANNOT/cancer_1/"+n+"\","+"\n")
    file.write("\"keep_col\": [\"contig\",\"tag\"],"+"\n")
    file.write("\"threads\": 8,"+"\n")
    file.write("\"library_type\": \"unstranded\""+"\n")
    file.write("}")
    file.close()

file = open("annot.sh","w")
file.write("#!/bin/bash"+"\n")
file.write("#PBS -q common"+"\n")
file.write("#PBS -l select=1:ncpus=4"+"\n"+"\n")
for n in list_file:
    file.write("cp "+po+"config_"+n+".json"+" /home/nikita.lagrange/config.json"+"\n")
    file.write("singularity -v run -B /store:/store ./general-annot.simg --configfile config.json --cores 4"+"\n")
file.close()
