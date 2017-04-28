
# coding: utf-8

# Question 1:

# In[1]:



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


# In[20]:

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


# In[ ]:




# In[21]:

#to find the max score

#initialize all them

#vert = insertion
vert = numpy.empty((len(seq2)+1, len(seq1)+1))
vert[:] = 0

d = 1
while d < len(vert):
	vert[d][0] = indel*d
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
	hori[0][d] = indel*d
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
	diag[0][d] = indel*d
	d+=1
d=1
while d < len(diag):
	diag[d][0] = indel*d
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


#run the script until we good


# In[22]:

(1==1)==1


# In[23]:


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
            vert[i][j] = a + indel
        elif b>=a:
            vert[i][j] = b + indel
        
        
        #Horizontal
        a = hori[i][j-1]
        b = diag[i][j-1]
        
        if a>=b:
            hori[i][j] = a + indel
        elif b>=a:
            hori[i][j] = b + indel

        #diag
        
        
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
            diag[i][j] =0
        
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
#print(seq1)
#print(seq1[bestLoc[1]-1])

#remember seq2 is the y value but is presented first in the coordinates
ali2 = ""
#print(seq2)
#print(seq2[bestLoc[0]-1])




k = 0
current = bestLoc

while k == 0:
    #print ("currentLoc: ", bestLoc, " currentDire ",dire[bestLoc])
    
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


print('Best Score: ', maxScore)
print ('Length: ', len(ali1))
print (ali1[::-1])
print (ali2[::-1])



# In[ ]:




# Question 2
# 

# In[2]:

#Let's rewrite the above program into a function so we can input our randomly generated sequences
print ("done")

def getLocAL(seq1, seq2, matchS, mismatchS, indel):
    matchScore = matchS
    mismatchScore =  mismatchS
    indel = int(indel)
    
    
    vert = numpy.empty((len(seq2)+1, len(seq1)+1))
    vert[:] = 0

    d = 1
    while d < len(vert):
        vert[d][0] = indel*d
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
        hori[0][d] = indel*d
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
        diag[0][d] = indel*d
        d+=1
    d=1
    while d < len(diag):
        diag[d][0] = indel*d
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
                vert[i][j] = a + indel
            elif b>=a:
                vert[i][j] = b + indel


            #Horizontal
            a = hori[i][j-1]
            b = diag[i][j-1]

            if a>=b:
                hori[i][j] = a + indel
            elif b>=a:
                hori[i][j] = b + indel

            #diag


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
    #print(seq1)
    #print(seq1[bestLoc[1]-1])

    #remember seq2 is the y value but is presented first in the coordinates
    ali2 = ""
    #print(seq2)
    #print(seq2[bestLoc[0]-1])




    k = 0
    current = bestLoc
    while k == 0:

        #on zero we stop
        if dire[bestLoc] == 0:
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

    return (len(ali1))


# In[3]:

#now let's make a nice random DNA generator
#imports

import random



#inputs

numberSeq = 200
sizeSeq = 1000


seqs = []


seqCt = 0

#nucleotide counts
aCt=0
tCt=0
cCt=0
gCt=0

while seqCt < numberSeq:
    nucCt = 0
    currentSeq = ""
    while nucCt < sizeSeq:
        r = random.random()
        if r<(1/4):
            currentSeq = currentSeq + "A"
            aCt+=1
        elif r <(1/2):
            currentSeq = currentSeq + "T"
            tCt+=1
        elif r <(3/4):
            currentSeq = currentSeq + "C"
            cCt+=1
        else:
            currentSeq = currentSeq + "G"
            gCt+=1
        nucCt += 1
        
        
    seqs.append(currentSeq)
    seqCt+= 1
    
print ("Nuceotide freq: A: ", aCt, " T: ",tCt, " C: ", cCt, " G: ", gCt)

print(len(seqs))


# In[4]:

#now let's write a program to run our new method 500 times, 
#using a pair of random DNA from our reandomly generated set'


#first loop through our set

randDNAcount = 0
p1 = []
p2 = []
p3 = []
p4 = [] 
while randDNAcount < (len(seqs)/2):
    p1.append(getLocAL(seqs[randDNAcount], seqs[len(seqs)-1-randDNAcount], 1, -20, -20))
    p2.append(getLocAL(seqs[randDNAcount], seqs[len(seqs)-1-randDNAcount], 1, -10, -10))
    p3.append(getLocAL(seqs[randDNAcount], seqs[len(seqs)-1-randDNAcount], 1, -.5, -.5))
    p4.append(getLocAL(seqs[randDNAcount], seqs[len(seqs)-1-randDNAcount], 1, -.33, -.33))
    print(randDNAcount)
    randDNAcount+=1
    
    


# In[33]:




# In[9]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.xlabel('length')
plt.ylabel('frequency')
plt.grid(True)


n, bins, patches = plt.hist(p1,25, normed=1, facecolor='green', alpha=0.75)



# In[11]:

plt.xlabel('length')
plt.ylabel('frequency')
plt.grid(True)
n, bins, patches = plt.hist(p2,25, normed=1, facecolor='green', alpha=0.75)


# In[7]:

n, bins, patches = plt.hist(p3,25, normed=1, facecolor='green', alpha=0.75)


# In[8]:

n, bins, patches = plt.hist(p4,25, normed=1, facecolor='green', alpha=0.75)


# In[12]:

randDNAcount = 0
p5 = []
p6 = []

while randDNAcount < (len(seqs)/2):
    p5.append(getLocAL(seqs[randDNAcount], seqs[len(seqs)-1-randDNAcount], 1, -1, -1))
    p6.append(getLocAL(seqs[randDNAcount], seqs[len(seqs)-1-randDNAcount], 1, -2, -2))
    print(randDNAcount)
    randDNAcount+=1


# In[15]:

n, bins, patches = plt.hist(p5,25, normed=1, facecolor='green', alpha=0.75)


# In[16]:

n, bins, patches = plt.hist(p6,25, normed=1, facecolor='green', alpha=0.75)


# In[17]:

means = [numpy.mean(p1),numpy.mean(p2),numpy.mean(p3),numpy.mean(p4),numpy.mean(p5),numpy.mean(p6)]

print(means)


# In[21]:

plt.plot([-20, -10, -.5, -.33, -1,-2], means)


# In[22]:


means = [numpy.mean(p1),numpy.mean(p2),numpy.mean(p6),numpy.mean(p5),numpy.mean(p3),numpy.mean(p4)]
plt.plot([-20, -10, -2, -1, -.5,-.33], means)


# In[ ]:



