#!/user/bin/python
 
__author__ = 'Jason Williams (jaybwilliams1@uchicago.edu)'
__version__ = '0.0.1'
 
# imports
import sys
import csv
import itertools
from itertools import izip
import glob
import os
from collections import defaultdict
from operator import itemgetter
from math import log as ln


# Lists
fileID = []
cdr3parse = []
key = []
freq = []

# dictionaries
d1 = {}
d2 = {}
uniqueD = {}
d3 = defaultdict(int)
d4 = {}
d5 = {}
d6 = {}

# Raw inputs
#path_input = raw_input("path to data: ")
#filename_input = raw_input("Save file as: ")

#functions

#directory = "~/Users/jaybwilliams1/Dropbox/Gajweski_Lab/Projects/TCR_Sequencing/"
#programlocation = /Users/jaybwilliams1/Dropbox/Gajewski_Lab/Projects/TCR_Sequencing/PythonCode/Import_4.py

def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
		return i
   
# -----  This code extracts all CDR3 aa sequences and makes a list  --------
for name in glob.glob('*.txt'):
    d5[name[:]] = file_len(name)
    fileID.append(name[:])
    with open(name, 'rb') as files:
        reader = csv.reader(files, delimiter = '\t')
        reader.next()
        for row in reader:
            cdr3parse.append(row[4])
            freq.append(row[0])

# Create a unique data set        	
unique = list(set(cdr3parse))

# --- generates a dictionary with they keys = to the unique CDR3 aa sequences
# --- and the values as blank lists
for line in unique:
	uniqueD[line] = []

# ---- This code will parse all .cls the files in a directory 
# ---- and return a default nested dictionary {filename: {AA : count}}
# --- Since there are multiple nt seq for one aa seq I used a defaultdict(int)
for i in range(len(fileID)):
	for name in glob.glob('*.txt'):
		d1[name[:]] = defaultdict(int)
		with open(name, 'rb') as files:
			row = files.next()
		        for row in files:
			    row = row.strip().split('\t')
			    k, v = row[4], row[0]
			    d1[name[:]][k] += int(v)
			    
# --- this short bit of code will determine the number of 
# --- convergent sequenes in each patient. It's also a checkpoint
# --- because the returned value should never be negative
for k, v in d1.items():
	d4[k] = len(v)

convseq = []

for k, v in d5.items():
	 convseq.append([k, int(d5[k] - d4[k])])


# --- To compare unique sequence list to dictionary of patients
# --- and generate dictionary {AA : (p1ID, p1v), (p2ID, p2v)..etc}
# --- where p1ID = patient1 ID and p1v = Patient 1 value
for cdr3 in uniqueD.items():
    for key1 in d1.keys():
        if cdr3[0] in d1[key1].keys():  #{AA: []} is in {file : {AA : freq}}
            for seq in d1[key1].items():
	        if seq[0] == cdr3[0]:
		    cdr3[1].append((key1,str(seq[1])))
        else:
	    cdr3[1].append((key1,'0'))

# --- This sequence will compare dictionaries to unique sequence list 
# --- and generate a dictionary {AA : [p1v, p2v, p3v..etc]}. It's easier
# --- to work with however it's missing each patient identifier for each value
for cdr3 in uniqueD.items():
    for key1 in d2.keys():		
        if cdr3[0] in d2[key1].keys():
            for seq in d2[key1].items():
	        if seq[0] == cdr3[0]:
		    cdr3[1].append(seq[1])
        else:
	    cdr3[1].append('0')


# --- This will write the file
header = []  #I define the header within a tuple to maintain the order
matrix = []  # this list allows me to troubleshoot
#sdata = []
with open("../CDR3aaFrequency_TCRb.txt", 'w') as output:
    header.append(str('CDR3'))
    for i1 in sorted(uniqueD.items()[0][1][:], key = lambda x: x):
    	    header.append(i1[0])
    output.write('\t'.join(header) + '\n')
    for k, v in uniqueD.iteritems():
    	matrix.append((k, [x[1] for x in v]))
    	sdata = ((k, sorted(v, key = lambda x: x[0])))
    	output.write('%s\t%s\n' % (sdata[0], '\t'.join(x[1] for x in sdata[1])))
        #output.write('%s\t%s\n' % (k, '\t'.join(x[1] for x in v)))

## Idea - try to write something like output = key + sorted values

#Sort sorted(uniqueD.items()[0][1], key = lambda x: x[0]) - ID value pair
#Sort sorted([x[0] for x in uniqueD.items()[0][1]], key = lambda x: x) - just ID
# for k, v in sorted(uniqueD.iteritems(), key = lambda x: [x[0] for x in uniqueD.items()[0][1]]):

"""
# --- This is to write the MHI file

array = [[] for x in xrange(len(uniqueD.items()))]

count = 0
for i in array:
    count += 1
    i.append((count, uniqueD.values()[int(count -1)]))

MHIArray = []

for i in array:
    for idx, val in enumerate(i[0][1], start = 1):
        MHIArray.append([i[0][0], idx, val])

SortedMHI = sorted(MHIArray, key=itemgetter(1))
            

with open("../MHI.txt", 'w') as output:
    header = ['MHI']
    stats = [str(len(uniqueD)), str(len(fileID))]
    output.write('\t'.join(header) + '\n' + '\t'.join(stats) + '\n')
    end = ['-1', '-1', '-1']
    for i in SortedMHI:
        outputdata = [str(i[1]), str(i[0]), str(i[2])]
        output.write('\t'.join(outputdata)+'\n')
    output.write('\t'.join(end))
 output.close()
"""

