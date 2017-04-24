
# coding: utf-8

# 

# In[145]:

#python locAL.py <seq file> -m <match> -s <mismatch> -d <indel> -a
#python locAL.py testseqs.txt -m +1 -s -1 -d -1 -a

import sys, getopt, numpy

arguments = ["locAL", "p1seqs.txt", "-m", "1", "-s","-10", "-d", "-1", "-a"]


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


# In[146]:

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




# In[147]:

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


# In[155]:

# here we going to loop through the whole thing and go from top left to bottom right


#let's make a variable to keep track of the biggest score value:
maxScore = 0
bestLoc = (0,0)
# we want to iterate 1-10 in the 3 matrices. This is the nested for loop
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
        
        if hori[i][j] < 0:
            hori[i][j] = 0
        if vert[i][j] < 0:
            vert[i][j] = 0
        
        a = vert[i][j]
        b = hori[i][j]
        
        #print((seq1[j-1],seq2[i-1]))
        
        if(int(seq1[j-1]==seq2[i-1]) ==0):
            cScore = mismatchScore
        else:
            cScore = matchScore

        c = diag[i-1][j-1] + cScore
        
        
        if a>=b and a>=c:
            dire[i][j] = "1"
            diag[i][j]=a
        if b>=a and b>=c:
            dire[i][j] = "2"
            diag[i][j]=b
        if c>=a and c>=b:
            dire[i][j] = "3"
            diag[i][j]=c 
        if diag[i][j]<0:
            dire[i][j] = 0
            diag[i][j] = 0
        
        if(diag[i][j] >= maxScore):
            maxScore = diag[i][j]
            bestLoc = (i,j)
            
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


print('best: ', maxScore)
print(bestLoc)


# In[156]:

# run this if -a is on
#reset directional borders to zero:
d=1
while d < len(dire[0]):
	dire[0][d] = 0
	d+=1
d=1
while d < len(dire):
	dire[d][0] = 0
	d+=1


# let's write a function to find the local alignment


ali1 = "" 
print(seq1)
print(seq1[bestLoc[1]-1])

#remember seq2 is the y value but is presented first in the coordinates
ali2 = ""
print(seq2)
print(seq2[bestLoc[0]-1])




k = 0
current = bestLoc
while k == 0:
    #\print ("currentLoc: ", bestLoc, " currentDire ",dire[bestLoc])
    
    #on zero we stop
    if dire[bestLoc] == 0:
        print("stopped at: ", bestLoc)
        k=1
    #on 1 we go up. so i changes but j stays the same
    elif dire[bestLoc] == 1:
        bestLoc = (bestLoc[0]-1, bestLoc[1])
        ali1 = ali1 + "-"
        ali2 = ali2 + str(seq2[bestLoc[0]])
    #on 2 we go left so j changes but i stays constant
    elif dire[bestLoc] == 2:
        bestLoc = (bestLoc[0], bestLoc[1]-1)
        ali2 = ali2 + "-"
        ali1 = ali1 = ali1 + str(seq1[bestLoc[1]])
    #on 3 both change, yay!
    elif dire[bestLoc] == 3:
        bestLoc = (bestLoc[0]-1, bestLoc[1]-1)
        ali1 = ali1 + str(seq1[bestLoc[1]])
        ali2 = ali2 + str(seq2[bestLoc[0]])

print(dire)

print (ali1[::-1])
print (ali2[::-1])


# In[ ]:




# In[ ]:



