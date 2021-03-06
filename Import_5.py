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
   
   
def counttuples(listoftuples):
	count = 0
	for i in listoftuples:
		if i !='0':
			count += 1
	return count
		
# -----  This code extracts all CDR3 aa sequences and makes a list  --------
def main(argv):
    for name in glob.glob(argv[1]+'/*.txt'):
        d2[name[:]] = file_len(name)
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
	    for name in glob.glob(argv[1]+'/*.txt'):
		    d1[name[(len(argv[1])):-4]] = defaultdict(int)
		    with open(name, 'rb') as files:
			    row = files.next()
		            for row in files:
			        row = row.strip().split('\t')
			        k, v = row[4], row[0]
			        d1[name[(len(argv[1])):-4]][k] += int(v)
			    

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


# --- This will write the file
    header = []  #I define the header within a tuple to maintain the order
    matrix = []  # this list allows me to troubleshoot
    with open(argv[2]+'CDR3aaFrequency_TCRb.csv', 'w') as output:
        header.append(str('CDR3'))
        for i1 in sorted(uniqueD.items()[0][1][:], key = lambda x: x):
    	    header.append(i1[0])
    	header.append('Zrec')
        output.write(','.join(header) + '\n')
        for k, v in uniqueD.iteritems():
    	    matrix.append((k, [x[1] for x in v]))
    	    
            sdata1 = k
            sdata2 = [x[1] for x in sorted(v, key = lambda x: x[0])]
            sdata3 = int((counttuples([x[1] for x in v])))
    	    sdata = (sdata1, sdata2, sdata3)

            output.write(str(k) + ',' + 
    	    ','.join(i for i in sdata2) + ',' +
    	    (str(sdata3)) +
    	    '\n')

    	    #output.write((str(sdata[0]) + '\t'.join(([x[1] for x in sdata[1]])) + '\t'.join(str(sdata[2])))+ '\n')
    	    #output.write('%s\t%s\n' % (sdata[0], '\t'.join(x[1] for x in sdata[1]) + '\t'.join(sdata[2])))
    	    
    	    
# print [x[1] for x in uniqueD.values()[0]]

if (__name__ == "__main__"):
	status = main(sys.argv)
	sys.exit(status)

