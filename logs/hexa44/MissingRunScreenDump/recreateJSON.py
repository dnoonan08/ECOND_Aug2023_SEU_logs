import re
import numpy as np

lines=''
with open("dump_log_run6.txt") as _file:
    lines=_file.read()

patternWordCount="'(.*) Word Count: (\d*), Error Count: (\d+)'"
wordCounts=re.findall(patternWordCount,lines)
wordCounts=[[x[0],int(x[1]),int(x[2])] for x in wordCounts]

patternTMRCount="tmr_err_cnt: (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+)"
tmr_cnts=re.findall(patternTMRCount,lines)
tmr_cnts=[[int(y,16) for y in x] for x in tmr_cnts]

patternOtherCount="other register errors: (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+)"
other_cnts=re.findall(patternOtherCount,lines)
other_cnts=[[int(y,16) for y in x] for x in other_cnts]

patternSCDiffs="(\d*), \[(\w*) (\w*) (\w*) (\w*) (\w*) (\w*)\] \[(\w*) (\w*) (\w*) (\w*) (\w*) (\w*)\]"
scDiffs=re.findall(patternSCDiffs,lines)

data_ASIC=np.array([[0x55555500]*6]*len(scDiffs)*8)
data_emulator=np.array([[0x55555500]*6]*len(scDiffs)*8)

d=np.vectorize(lambda x: int(x,16))(np.array(scDiffs)[:,1:])
c=np.vectorize(lambda x: int(x))(np.array(scDiffs)[:,0])

data_ASIC[c]=d[:,:6]
data_emulator[c]=d[:,6:]

#load another json, and replace the data
import json
fname='../Run_08_testReport_hexa44_2023-08-05_12-12-35.json'
jsonDump=json.load(open(fname))
jsonDump['created']=0
jsonDump['duration']=0
jsonDump['warnings']=[]

### remove metadata from test 0 (pre-beam)
jsonDump['tests'][0]['metadata']['daq_asic_before_beam']=[]
jsonDump['tests'][0]['metadata']['daq_emu_before_beam']=[]

### replace counts withvalues found in dump
jsonDump['tests'][1]['metadata']['word_err_count']=wordCounts
jsonDump['tests'][1]['metadata']['tmr_err_cnts']=tmr_cnts
jsonDump['tests'][1]['metadata']['other_register_err_cnts']=other_cnts
jsonDump['tests'][1]['metadata']['daq_asic_post_beam']=data_ASIC.tolist()
jsonDump['tests'][1]['metadata']['daq_emu_post_beam']=data_emulator.tolist()

#clear test[2] metadata which was missing
for k in jsonDump['tests'][2]['metadata'].keys():
    jsonDump['tests'][2]['metadata'][k]=[]

json.dump(jsonDump,open('../Run_06_testReport_hexa44_RECONSTRUCTED.json','w'))
