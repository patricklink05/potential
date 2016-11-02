import random
import math
import string
scale = 1
#this is used to scale the end result, the larger the n, the larger the end shape is
number= 100
#this is used to set how many points we generate for each shape, the higher this is, the more points

	
def cylinder(scale,number):
	cylinderlist = []
	for item in range(number):
		r = .125*scale
		theta = random.uniform(0,2*math.pi)
		x = scale*random.uniform(-1,1)
		y = scale*math.cos(theta)
		z = scale*math.sin(theta)
		cylinder1point = "{{{0},{1},{2}}}".format(x,y,z)
		cylinderlist.append(cylinder1point)
		cylinderlist2 = ",".join(cylinderlist)
	return "{{{0}}}".format(cylinderlist2)

#this function generates a set of coordinates within a cylinder centered at 0,0,0 and scaled by n, then returns them
def sphere1(scale,number):
	sphere1list = []
	for item in range(number):
		r = .5*scale
		theta = random.uniform(0,2*math.pi)
		phi = random.uniform(0,math.pi)
		x2 = r*math.cos(theta)*math.sin(phi) + scale 
		y2 = r*math.sin(theta)*math.sin(phi)
		z2 = r*math.cos(phi)
		sphere1point = "{{{0},{1},{2}}}".format(x2,y2,z2)
		sphere1list.append(sphere1point)
		sphere1list2 = ",".join(sphere1list)
	return "{{{0}}}".format(sphere1list2)
#this generates a set of coordinates as floats within a sphere centered at n,0,0 and scaled by n, then returns them
def sphere2(scale,number):
	sphere2list = []
	for item in range(number):
		r = .5*scale
		theta = random.uniform(0,2*math.pi)
		phi = random.uniform(0,math.pi)
		x3 = r*math.cos(theta)*math.sin(phi) - scale 
		y3 = r*math.sin(theta)*math.sin(phi)
		z3 = r*math.cos(phi)
		sphere2point = "{{{0},{1},{2}}}".format(x3,y3,z3)
		sphere2list.append(sphere2point)
		sphere2list2 = ",".join(sphere2list)
	return "{{{0}}}".format(sphere2list2)

cylinder1 = cylinder(scale,number)
print(cylinder1)

sphere1 = sphere1(scale,number)
#print(sphere1)

sphere2 = sphere2(scale,number)
#print(sphere2)