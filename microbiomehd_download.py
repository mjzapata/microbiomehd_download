import pandas as pd
import numpy as np
import wget
import sys
import os
# https://gist.github.com/sourabhdattawad/53d765a8c9c72c1c4ec1af56c44e35a7
datahost="SRA"

filepath='/Users/malcolm/Downloads/MicroBiomeHD_SuppTable2.txt'
table = pd.read_table(filepath, sep='\t')
#print(table.head(3))
f = open("SraAccList.txt", "w+")


for index, row in table.iterrows():
    if(row["DataHost"] == datahost):
        print("downloading " + row["RawData"])
        sra_id = row["RawData"]
        f.writelines(sra_id+"\n")
        uniqueStudyName = row["Disease"]+row["Year"]+row["DatasetID"]
        os.system("mkdir " + uniqueStudyName)
        os.system("mkdir " + uniqueStudyName + "/" + "seqs")
        os.system("esearch -db sra -query " + row["RawData"] + " | efetch --format runinfo | cut -d ',' -f 1 | grep SRR | xargs fastq-dump --split-files" )
        #url = 'ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/' + sra_id[:3] + '/' + sra_id[:6] + '/' + sra_id + '/' + sra_id + '.sra'
        #filename = wget.download(url)
        #if filename:
         #   print("\nDownload Complete " + sra_id)
         #   print("\nConverting...")
        #    cmd = 'fastq-dump ' + sra_id + '.sra'
         #   os.system(cmd)

