import json
import pandas as pd
import numpy as np
import glob
import re

hexa44Data=glob.glob('../logs/hexa44/*')
hexa44Data=[x for x in hexa44Data if '/Run_' in x]

hexa48Data=glob.glob('../logs/hexa48/*')
hexa48Data=[x for x in hexa48Data if '/Run_' in x]


#get file lists
fileNames44=np.array(hexa44Data)
fileNames44.sort()
fileNames48=np.array(hexa48Data)
fileNames48.sort()

#parse jsons, get total error counts
errorCountLists=[]

def countsTotal(x):
   rollOvers=(x[1:]-x[:-1]<0).sum(axis=0)
   return rollOvers*256 + x[-1]

for fname in fileNames44:
    runNum=re.findall('Run_(\w*)_test',fname)[0]
    data=json.load(open(fname))
    try:
        regNames=data['tests'][1]['metadata']['tmr_err_names']
        errCounts=data['tests'][1]['metadata']['tmr_err_cnts']
        errCounts=np.array(errCounts)
        errCounts=countsTotal(errCounts).tolist()
    except:
        errCounts=[0]*53
    errorCountLists.append([runNum,44]+errCounts)
for fname in fileNames48:
    runNum=re.findall('Run_(\w*)_test',fname)[0]
    data=json.load(open(fname))
    try:
        regNames=data['tests'][1]['metadata']['tmr_err_names']
        errCounts=data['tests'][1]['metadata']['tmr_err_cnts']
        errCounts=np.array(errCounts)
        errCounts=countsTotal(errCounts).tolist()
    except:
        errCounts=[0]*51
    errorCountLists.append([runNum,48]+errCounts)

df=pd.DataFrame(errorCountLists)
df.columns=['Run','Hexacontroller']+regNames

df.to_csv('../data/tmr_error_counts_by_run.csv',index=False)
