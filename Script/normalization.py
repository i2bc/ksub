import pandas as pd


def normalization(path_input, path_output, k=31):
    df = pd.read_csv(path_input, sep='\t')
    dico_nbread = {}
    dico_lread = {}
    for i in range(len(df)):
        ky = df.iloc[i]["Sample"].split("_")[0]
        nb = int(df.iloc[i]["FastQC_mqc-generalstats-fastqc-total_sequences"])
        lg = df.iloc[i]["FastQC_mqc-generalstats-fastqc-avg_sequence_length"]
        lg = int(lg)
        if ky not in dico_nbread:
            dico_nbread[ky] = [nb]
            dico_lread[ky] = [lg]
        else:
            dico_nbread[ky].append(nb)
            dico_lread[ky].append(lg)
    file = open(path_output, "w")
    for ky in dico_lread.keys():
        nf = 1/((dico_lread[ky][0]-k+1)*dico_nbread[ky][0] +
                (dico_lread[ky][1]-k+1)*dico_nbread[ky][1])*1e9
        file.write(ky+"\t"+str(nf)+"\n")
    file.close()
