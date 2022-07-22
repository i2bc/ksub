#!/bin/bash

#PBS -q common
#PBS -N REINDEERSeo
#PBS -M nikita.lagrange@i2bc.paris-saclay.fr
#PBS -l ncpus=8

/home/nikita.lagrange/R/REINDEER/Reindeer --index -f /home/nikita.lagrange/R/REINDEER/fof.txt -o /data/work/I2BC/nikita.lagrange/idx -t 16
