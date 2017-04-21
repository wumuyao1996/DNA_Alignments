
# coding: utf-8

# 

# In[18]:

#python locAL.py <seq file> -m <match> -s <mismatch> -d <indel> -a

import sys, getopt, numpy

arguments = ["locAL", "testseqs.txt", "-m", "1", "-s","-10", "-d", "-1", "-a"]


file = arguments[1]
matchScore = int(arguments[3])
mismatchScore =  int(arguments[5])
indel = int(arguments[7])
findA = False
if '-a' in arguments: 
	findA = True
	#print('found -a')

print ('Number of arguments:', len(arguments), 'arguments.')
print ('Argument List:', str(arguments))
print ('file:', str(file))
print ('matchScore:', str(matchScore))
print ('mismatchScore:', str(mismatchScore))
print ('indel:', str(indel))
print ('findA:', str(findA))


# In[19]:

data = open(file, "r")


check = False
counter = 0
seq1 = []
seq2 = []
for line in data:
	if 'seq' in line:
		check = True
	elif check == True and counter == 0:
		for char in line:
			if char != '\n':
				seq1.append(char)

		counter +=1
	elif check == True and counter == 1:
		for char in line:
			if char != '\n':
				seq2.append(char)

print ('seq1', seq1)

print ('seq2', seq2)


# In[28]:

#to find the max score

#initialize all them

#vert = insertion
vert = numpy.empty((len(seq1)+1, len(seq2)+1))
vert[:] = numpy.NAN

d = 1
while d < len(vert):
	vert[d][0] = mismatchScore-d+1
	d+=1

d=1
while d < len(vert[0]):
	vert[0][d] = -float("inf")
	d+=1

vert [0][0] = 0


#hori = deletion
hori = numpy.empty((len(seq1)+1, len(seq2)+1))
hori[:] = numpy.NAN
d=1
while d < len(hori[0]):
	hori[0][d] = mismatchScore-d+1
	d+=1
    
d=1
while d < len(hori[0]):
	hori[d][0] = -float("inf")
	d+=1
hori[0][0]=0

#diag = match or mismatch
diag = numpy.empty((len(seq1)+1, len(seq2)+1))
diag[:] = numpy.NAN
d=1
while d < len(diag[0]):
	diag[0][d] = mismatchScore-d+1
	d+=1
d=1
while d < len(diag[0]):
	diag[d][0] = mismatchScore-d+1
	d+=1
diag [0][0] = 0

#score for scorekeeping
score = numpy.empty((len(seq1)+1, len(seq2)+1))
score[:] = numpy.NAN

d=1
while d < len(score[0]):
	score[0][d] = 0
	d+=1
d=1
while d < len(score[0]):
	score[d][0] = 0
	d+=1
score [0][0] = 0

#1 = Vert, 2 = Horiz, 3 = diag
directional = numpy.empty((len(seq1)+1, len(seq2)+1))
d=1
while d < len(dire[0]):
	dire[0][d] = 2
	d+=1
d=1
while d < len(dire[0]):
	dire[d][0] = 1
	d+=1
print ("Vertical")
print (vert)

print ("Horizontal")
print (hori)

print ("Diagonal")
print (diag)

print ("Score")
print (score)

print ("Direction")
print (dire)

#run the script until we good


# In[ ]:




# In[ ]:




# In[ ]:



