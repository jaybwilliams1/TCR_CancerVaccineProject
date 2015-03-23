
#!/user/bin/python
 
__author__ = 'Jason Williams (jaybwilliams1@uchicago.edu)'
__version__ = '0.0.1'

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
	       
----------
# --- this short bit of code will determine the number of 
# --- convergent sequenes in each patient. It's also a checkpoint
# --- because the returned value should never be negative
    for k, v in d1.items():
	d4[k] = len(v)

    convseq = []

    for k, v in d5.items():
        convseq.append([k, int(d5[k] - d4[k])])
---------------
