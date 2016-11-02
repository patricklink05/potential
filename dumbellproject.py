import random
import math
import string

#This python file will generate a set of points that will represent a cartoon
#dumbell.  Each function will generate a list of lists that will contain 
#[x,y,z] coordinates.  

#setting up the points which we create geometric shapes around
def cylinder(n):
	r = .125*n
	theta = random.uniform(0,2*math.pi)
	x = n*random.uniform(-1,1)
	y = r*math.cos(theta)
	z = r*math.sin(theta)
	return [x,y,z]
#this function generates a set of coordinates within a cylinder centered at 
#0,0,0 and scaled by n, then returns them
def sphere2(n):
	r = .5*n
	theta = random.uniform(0,2*math.pi)
	phi = random.uniform(0,math.pi)
	x2 = r*math.cos(theta)*math.sin(phi) + n 
	y2 = r*math.sin(theta)*math.sin(phi)
	z2 = r*math.cos(phi)
	return[x2,y2,z2]
#this generates a set of coordinates as floats within a sphere centered at 
#n,0,0 and scaled by n, then returns them
def sphere3(n):
	r = .5*n
	theta = random.uniform(0,2*math.pi)
	phi = random.uniform(0,math.pi)
	x3 = r*math.cos(theta)*math.sin(phi) - n
	y3 = r*math.sin(theta)*math.sin(phi)
	z3 = r*math.cos(phi)
	return[x3,y3,z3]



#######################################################################
if __name__ == "__main__":
	n = 4
#this is used to scale the end result, the larger the n, the larger the end shape is

	k=100
#this is used to set how many points we generate for each shape, the higher this is, the more points

	center1 = []
	center2 = []
	center3 = []
	for item1 in range(k):
		center1.append(cylinder(n))
#this loop appends the result of cylinder(n) to the first geometric center for as many times as we define as k
#print(center1)
#prints the result of the center after it has been appended to

	for item2 in range(k):
		center2.append(sphere2(n))
#this appends results of sphere2(n) to second geometric center k times
#print(center2)
#prints result of the second geometric center after it has been appended

	for item3 in range(k):
		center3.append(sphere3(n))
#this appends results of sphere3(n) to third geometric center k times
#print(center3)
#prints result of the third geometric center after it has been appended
	output = str(center1+center2+center3)
	print(output)

