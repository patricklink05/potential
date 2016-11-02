import random
import math
import string

#This file is an improvement on dumbell.py as it generates the [x,y,z]
#points on the surface of the geometric shapes rather than inside of it. 
#It also now generates points on the caps of the cylinder. The points
#are also now printed out as a string so that they could be contained
#within curly brackets as the plotting software (Wolfram Mathematica)
#used for testing requires this format.  It also allows for variable
#centers rather than a fixed center based on some constant that affects
#the scale. It also writes the coordinates to a text file

#Note: The original project was to create a cartoon dumbell, but this file
#digresses beyond this to more potential geometric shapes
	
def cylinder(scale,number,center):
	cylinderlist = []
	area = 2*(.125*scale)*3*2*scale
	capnumber = int(number*4*math.pi*(.125*scale)*(.125*scale)/area)
	for item in range(capnumber):
		r = .125*scale*random.uniform(0,1)
		theta = random.uniform(0,2*math.pi)
		x = scale*random.choice([-1,1]) + center[0]
		y = r*math.cos(theta) + center[1]
		z = r*math.sin(theta) + center[2]
		cylinderpoint2 = "{{{0},{1},{2}}}".format(x,y,z)
		cylinderlist.append(cylinderpoint2)
	for item in range(number):
		r = .125*scale
		theta = random.uniform(0,2*math.pi)
		x = scale*random.uniform(-1,1) + center[0]
		y = r*math.cos(theta) + center[1]
		z = r*math.sin(theta) + center[2]
		cylinderpoint = "{{{0},{1},{2}}}".format(x,y,z)
		cylinderlist.append(cylinderpoint)
		cylinderstring = ",".join(cylinderlist)
	return "{{{0}}}".format(cylinderstring)
	print(capnumber)
#this function generates a set of coordinates within a cylinder centered at 
#0,0,0 and scaled by n, then returns them

def sphere(scale,number,center):
	spherelist = []
	for item in range(number):
		r = .5*scale
		theta = random.uniform(0,2*math.pi)
		phi = random.uniform(0,math.pi)
		x2 = r*math.cos(theta)*math.sin(phi) + center[0]
		y2 = r*math.sin(theta)*math.sin(phi) + center[1]
		z2 = r*math.cos(phi) + center[2]
		spherepoint = "{{{0},{1},{2}}}".format(x2,y2,z2)
		spherelist.append(spherepoint)
		spherestring = ",".join(spherelist)
	return "{{{0}}}".format(spherestring)

#this generates a set of coordinates as floats within a sphere centered at 
#n,0,0 and scaled by n, then returns them

##############################################################################

scale = 1
#this is used to scale the end result, the larger the n, the larger the end 
#shape is
number= 100
#this is used to set how many points we generate for each shape, the higher 
#this is, the more points

center1 = [1,0,0]
center2 = [-1,0,0]
center3 = [1,2,2]
origin = [0,0,0]
#lists of [x,y,z] coordinates used as centers for the geometric objects

cylinderone = cylinder(scale,number,origin)
print(cylinderone)
#calls and prints the cylinder coordinates
sphereone = sphere(scale,number,center1)
print(sphereone)
#calls and prints the first sphere coordinates
spheretwo = sphere(scale,number,center2)
print(spheretwo)
#calls and prints the second sphere coordinates
spherethree = sphere(scale,number,center3)
print(spherethree)
#calls and prints the third sphere coordinates

f = open("dumbellcoordinates","w")
f.write(sphereone+spheretwo+spherethree)
f.close()
#opens a file called dumbell coordinates and writes the coordinates for the
#points to it.
