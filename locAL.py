#python locAL.py <seq file> -m <match> -s <mismatch> -d <indel> -a

import sys, getopt, numpy

arguments = sys.argv


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



#diag = match or mismatch
diag = numpy.empty((len(seq1)+1, len(seq2)+1))
diag[:] = numpy.NAN


#score for scorekeeping
score = numpy.empty((len(seq1)+1, len(seq2)+1))
score[:] = numpy.NAN


#1 = Vert, 2 = Horiz, 3 = diag
directional = numpy.empty((len(seq1)+1, len(seq2)+1))





print (numpy.shape(vert))
print (vert)






#run the script until we good







