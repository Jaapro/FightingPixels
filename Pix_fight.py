#Fighting pixels by Jaap Saers
#
#based on a gif I found, pixels fighting is a cellular automaton with simple rules I guessed based on the gif: 
#Enjoy

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#prompt user for dimensions of the board and the number of ones
userwidth = int(input("How wide should the grid be?"))
userheight = int(input("How high should the grid be?"))
iters = int(input("How many iteratrions should the game run?"))

shape = [userheight, userwidth]

def make_board(shape): #shape should be a 2d array [height,width] and ones is the number of 1's on the board
    board = np.zeros(shape, dtype=np.int)
    board[0:userheight, 0:int(round(0.5*userwidth))] = 1
    return board

a = make_board(shape)

toprow = [0]
botrow = [userheight-1]
leftcol = [0]
rightcol = [userwidth-1]


#function that takes in a grid of zeroes and ones like a from above as gridstate and applies rules which is returned as a grid b
def PixFight(gridstate):
	b = gridstate
	rows, cols = a.shape
	for i in range(1, rows-1):
	    for j in range(1, cols-1):
	        state = a[i, j]
	        neighbors = a[i-1:i+2, j-1:j+2]
	        k = np.sum(neighbors) - state # calculate sum of 0 and 1 around the central (state) pixel
	        k = float(k/8)
	        p = np.random.uniform(0, 1)#generate random number between 0 and 1
	        if k >= p:
	        	b[i, j] = 1
	        else:
	        	b[i, j] = 0

#top row
	for i in toprow:
		for j in range(1, cols-1):
			state = a[i,j]
			neighbors = a[i:i+2, j-1:j+2]
			k = np.sum(neighbors) - state
			k = float(k/5)
			p = np.random.uniform(0, 1)
			if k >= p:
				b[i, j] = 1
			else:
				b[i, j] = 0

#bottom row
	for i in botrow:
		for j in range(1, cols-1):
			state = a[i, j]
			neighbors = a[i-1:i+1, j-1:j+2]
			k = np.sum(neighbors) - state
			k = float(k/5)
			p = np.random.uniform(0, 1)
			if k >= p:
				b[i, j] = 1
			else:
				b[i, j] = 0

#left column
	for i in range(1, rows-1):
		for j in leftcol:
			state = a[i, j]
			neighbors = a[i-1:i+2, j:j+2]
			k = np.sum(neighbors) - state
			k = float(k/5)
			p = np.random.uniform(0, 1)
			if k >= p:
				b[i, j] = 1
			else:
				b[i, j] = 0
#right column
	for i in range(1, rows-1):
		for j in rightcol:
			state = a[i, j]
			neighbors = a[i-1:i+2, j-1:j+1]
			k = np.sum(neighbors) - state
			k = float(k/5)
			p = np.random.uniform(0, 1)
			if k >= p:
				b[i, j] = 1
			else:
				b[i, j] = 0

#top left
	for i in toprow:
		for j in leftcol:
			state = a[i,j]
			neighbors = a[i:i+2, j:j+2]
			k = np.sum(neighbors) - state
			k = float(k/3)
			p=np.random.uniform(0, 1)
			if k >= p:
				b[i, j] = 1
			else:
				b[i, j] = 0

#top right
	for i in toprow:
		for j in rightcol:
			state = a[i,j]
			neighbors = a[i:i+2, j-1:j+1]
			k = np.sum(neighbors) - state
			k = float(k/3)
			p=np.random.uniform(0, 1)
			if k >= p:
				b[i, j] = 1
			else:
				b[i, j] = 0

#bottom right
	for i in botrow:
		for j in rightcol:
			state = a[i,j]
			neighbors = a[i-1:i+1, j-1:j+1]
			k = np.sum(neighbors) - state
			k = float(k/3)
			p=np.random.uniform(0, 1)
			if k >= p:
				b[i, j] = 1
			else:
				b[i, j] = 0

#bottom left
	for i in botrow: 
		for j in leftcol:
			state = a[i,j]
			neighbors = a[i-1:i+1, j:j+2]
			k = np.sum(neighbors) - state
			k = float(k/3)
			p=np.random.uniform(0, 1)
			if k >= p:
				b[i, j] = 1
			else:
				b[i, j] = 0
	return b

ims = [] #empty list to store images
fig = plt.figure(0)
pixratio = [] #empty list to store the number of 1's in each generation relative to total pixels

for x in range(iters):
	
	print("Run number " + str(x))
	fig.suptitle('Fighting Pixels', fontsize=14, fontweight='bold')
	txt = plt.text(0,0,"Generation: " + str(x))   #add a counter for each 
	im = plt.imshow(a, cmap='Blues', interpolation='none', animated=True)
	ims.append([im, txt])

	pixsum = np.sum(a)/(userwidth*userheight)
	pixratio.append([pixsum])

	#have initial grid "a" and apply rules and store in b
	b = PixFight(a)
	a = b 	
	x = x + 1

#animate images from ims
ani = animation.ArtistAnimation(fig, ims, interval=50, repeat=True, repeat_delay = 1000)

#plt.show() ##turn this on to plot in console

f = r"C:\Users\JP\Documents\Programming\python\pixels_fighting\ " + str(userheight) + "x" + str(userheight) + " grid " + str(iters) + " iters" +   ".gif"
writergif = animation.PillowWriter(fps=15) 
ani.save(f, writer=writergif)

f2 = r"C:\Users\JP\Documents\Programming\python\pixels_fighting\ " + str(userheight) + "x" + str(userheight) + " grid " +  str(iters) + " iters plot" +   ".png"

plt.figure(1)
plt.plot(pixratio)
plt.ylabel('#ones / total pixels')
plt.savefig(f2)
#plt.show()



