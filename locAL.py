
# coding: utf-8

# 

# In[76]:

#python locAL.py <seq file> -m <match> -s <mismatch> -d <indel> -a

import sys, getopt, numpy

arguments = ["locAL", "testseqs.txt", "-m", "1", "-s","-1", "-d", "-1", "-a"]


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


# In[77]:

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


# In[ ]:




# In[78]:

#to find the max score

#initialize all them

#vert = insertion
vert = numpy.empty((len(seq2)+1, len(seq1)+1))
vert[:] = 0

d = 1
while d < len(vert):
	vert[d][0] = indel-d+1
	d+=1

d=1
while d < len(vert[0]):
	vert[0][d] = -float("inf")
	d+=1

vert [0][0] = 0


#hori = deletion
hori = numpy.empty((len(seq2)+1, len(seq1)+1))
hori[:] = 0
d=1
while d < len(hori[0]):
	hori[0][d] = indel-d+1
	d+=1
    
d=1
while d < len(hori):
	hori[d][0] = -float("inf")
	d+=1
hori[0][0]=0

#diag = match or mismatch
diag = numpy.empty((len(seq2)+1, len(seq1)+1))
diag[:] = 0
d=1
while d < len(diag[0]):
	diag[0][d] = indel-d+1
	d+=1
d=1
while d < len(diag):
	diag[d][0] = indel-d+1
	d+=1
diag [0][0] = 0

#score for scorekeeping
score = numpy.empty((len(seq2)+1, len(seq1)+1))
score[:] = numpy.NAN

d=1
while d < len(score[0]):
	score[0][d] = 0
	d+=1
d=1
while d < len(score):
	score[d][0] = 0
	d+=1
score [0][0] = 0

#1 = Vert, 2 = Horiz, 3 = diag

dire = numpy.empty((len(seq2)+1, len(seq1)+1))
d=1
while d < len(dire[0]):
	dire[0][d] = 2
	d+=1
d=1
while d < len(dire):
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


x3 = numpy.empty((3, 2))
print (x3.shape)
print (x3)

#run the script until we good


# In[83]:

#here we going to loop through the whole thing and go from top left to bottom right



# we want to iterate 1-10 in the 3 matrices.
i = 1
while i < len(diag):
    j=1
    while j < len(diag[i]):
        #print ('current i and j: ', i , ' ', j)
        #we gotta manipulate each matrix we're working with
        
        #Vertical
        a = vert[i-1][j]
        b = diag[i-1][j]
        
        if a>=b:
            vert[i][j] = a + mismatchScore
        elif b>=a:
            vert[i][j] = b + mismatchScore
        
        
        #Horizontal
        a = hori[i][j-1]
        b = diag[i][j-1]
        
        if a>=b:
            hori[i][j] = a + mismatchScore
        elif b>=a:
            hori[i][j] = b + mismatchScore
        #diag
        
        a = vert[i][j]
        b = hori[i][j]
        
        print((seq1[j-1],seq2[i-1]))
        
        if(int(seq1[j-1]==seq2[i-1]) ==0):
            cScore = mismatchScore
        else:
            cScore = matchScore

        c = diag[i-1][j-1] + cScore
        
        if a>=b and a>=c:
            dire[i][j] = "1"
            print("a")
            diag[i][j]=a
        if b>=a and b>=c:
            dire[i][j] = "2"
            print("b")
            diag[i][j]=b
        if c>=a and c>=b:
            dire[i][j] = "3"
            print("c")
            diag[i][j]=c 
            
        j+=1

    i+=1

print('vertical: ')
print(vert)
print('horizontal: ')
print(hori)
print('diagonal: ')
print(diag)

print('Directional: ')
print(dire)

      


# In[ ]:




# In[ ]:



