import random
import math
import numpy
import pvutil
import subprocess

##############################################################################

#Notes to self-- why is the matrix definition taking a single matrix when it
#could be better to rotate the whole "object" by passing it another object 
#instead of just the numpy.ndarray type.  

##############################################################################

#This class defines a cylinder. The attributes that the class has are self, 
#scale, number and center.  Self is agiven.  Scale is the geometric scale 
#as the proportions of the cylinder are fixed.  The number is the number of 
#points that the instance will generate and center is the center of the 
#geometric shape.  Coordinates are generated as cylindrical coordinates then
#converted to cartesian coordinates.  

class Cylinder(object):
	def __init__(self,scale,number,center,alpha=0,beta=0,gamma=0):
		self.scale = scale
		self.number = number
		self.center = center
		self.area = 2 * (.125 * scale) * 3 * 2 * scale
		self.capnumber = int(number * 4 * math.pi * (.125 * scale) * (.125 * scale) / self.area)
		self.points = []
		self.alpha = alpha
		self.beta = beta
		self.gamma = gamma
		self.speck = ""
		#self.points gets the points in a list form which is more functional than the other one which works with mathematica. 
		self.repeater()

#initializes the instance of the class which sets attributes and calls the 
#repeater method as well as prints it.

	def checkrotate(self):	
		if self.alpha or self.beta or self.gamma != 0:
			templist = []
			for coordinate in self.points:
				coordinate = numpy.array([[coordinate[0]],[coordinate[1]],[coordinate[2]]])
				newcoord = Matrixdefinition(coordinate, self.alpha, self.beta, self.gamma)
				templist.append(newcoord.newmatrix)
			self.points = templist

#This method is used to check if there is any rotation.  While there are better
#ways of doing this, including automatically rotating them, the math behind the
#matrix rotation seems incorrect so this is a method so that both the non-rotated
#and rotated self.points could be visualized.  The math seems to work in isolated
#cases in test scripts using trivial matrices but the result is that the "rotated"
#cylinder is actually a scaled down cylinder.  

	def cylindersinglepoint(self):
		#this portion generates the coordinates
		r = .125 * self.scale
		theta = random.uniform(0, 2 * math.pi)
		x = self.scale*random.uniform(-1, 1) + self.center[0]
		y = r*math.cos(theta) + self.center[1]
		z = r*math.sin(theta) + self.center[2]
		
		#this portion generates the list of coordinates left as floats so it is mutable
		cylindersinglepointlist = [x, y, z]
		self.points.append(cylindersinglepointlist)

		#this portion generates the list of coordinates as a string easier for mathematica testing as of now
		cylinderpoint = "{{{:.5f},{:.5f},{:.5f}}}".format(x, y, z)
		return cylinderpoint

#this method actually generates the individual points, as cylindrical
#coordinates and then converts them to cartesian.  It then puts those 
#coordinates in cylinderpoint as a formatted string and then returns it.

	def cylindersinglepointcap(self):
		#this portion generates the coordinates
		r = .125 * self.scale*random.uniform(0, 1)
		theta = random.uniform(0,2 * math.pi)
		x2 = self.scale*random.choice([-1, 1]) + self.center[0]
		y2 = r*math.cos(theta) + self.center[1]
		z2 = r*math.sin(theta) + self.center[2]

		#this portion generates the list of coordinates left as floats so it is mutable
		cylindersinglepointlist = [x2, y2, z2]
		self.points.append(cylindersinglepointlist)

		#this portion generates the list of coordinates as a string easier for mathematica testing as of now
		cylinderpoint = "{{{:.5f},{:.5f},{:.5f}}}".format(x2, y2, z2)
		return cylinderpoint
#this method generates the points for the ends of the cylinder

	def repeater(self):
		cylindercoordinates = []
		for i in range(self.number):
			self.cylindersinglepoint()
		for i in range(self.capnumber):
			self.cylindersinglepointcap()
		
#this method is called upon initialization and generates a point using the 
#cylindersinglepoint method then appends the point to a list of coordinates
#once it goes through the designated number of times, it joins the list as a 
#string, formats it then returns it.
	
	"""def matrixtransformation(self):
		returnedlist = []
		counter = -1
		for i in self.points:
			counter += 1
		for item in range(counter):
			matrix = numpy.array([[self.points[item][0]],
							 	  [self.points[item][1]],
							 	  [self.points[item][2]]])
			rotatedmatrix = matrixdefinition(matrix,self.alpha,self.beta,self.gamma)
			rotatedmatrixlist = [float(rotatedmatrix.matrix[0,0]),
							 	 float(rotatedmatrix.matrix[1,0]),
							 	 float(rotatedmatrix.matrix[2,0])]
			returnedlist.append(rotatedmatrixlist)
		return returnedlist"""

#This is a similar but different way that I wrote a method to make the rotation
#act on the set of points but it had the same issue with the mathematics behind
#it.  I believe, but have not actually measured it, that the previous, 
#checkrotate method is faster than this matrixtransformation one, but once the
#underlying math is worked out they will be evaluated.

	def partiviewize(self):
		self.speck = pvutil.Speck()
		for item in self.points:
			record = self.speck.Record(*item)
			self.speck.insert(record,0)
		self.speck = str(self.speck)
		return self.speck

#this method is used to take a list of a list and turn it into a string format 
#that partiview can read.  

class Matrixdefinition(object):
	def __init__(self,matrix,alpha,beta,gamma):
		self.matrix = matrix
		self.alpha = alpha
		self.beta = beta
		self.gamma = gamma
		self.newmatrix = []
		try:
#This is to make sure that the inputed matrix is a numpy.ndarray or else a 
#TypeError will be returned
			self.matrix is numpy.ndarray
			self.xmatrix()
			self.matrix is numpy.ndarray
			self.yrotate()
			self.matrix is numpy.ndarray
			self.zrotate()
		except TypeError:
			"Wrong type"

#This class takes 4 args excluding itself:
#	matrix = the input matrix that is to be rotated, given as a numpy.ndarray
#	alpha = the angle of rotation for the x axis
#	beta = the angle of rotation for the y axis
#	gamma = the angle of rotation for the z axis

		
	def xmatrix(self):
		xmatrix = numpy.array([[1, 0, 0],
							  [0, (math.cos(self.alpha)), -(math.sin(self.alpha))],
							  [0, (math.sin(self.alpha)), (math.cos(self.alpha))]])
		return xmatrix

#Defines the x rotational matrix

	def ymatrix(self):
		ymatrix = numpy.array([[(math.cos(self.beta)), 0, (math.sin(self.beta))],
							  [0, 1, 0],
							  [-(math.sin(self.beta)), 0, (math.cos(self.beta))]])
		return ymatrix

#Defines the y rotational matrix

	def zmatrix(self):
		zmatrix = numpy.array([[(math.cos(self.gamma)),-(math.sin(self.gamma)),0],
							  [(math.sin(self.gamma)),(math.cos(self.gamma)),0],
							  [0,0,1]])
		return zmatrix

#Defines the z rotational matrix

	def xrotate(self):
		print self.matrix
		intermediatematrixx = self.xmatrix()*self.matrix
		self.matrix = numpy.array([[intermediatematrixx[0, 0] + intermediatematrixx[0, 1] + intermediatematrixx[0, 2]], 
								  [intermediatematrixx[1, 0] + intermediatematrixx[1, 1] + intermediatematrixx[1, 2]], 
								  [intermediatematrixx[2, 0] + intermediatematrixx[2, 1] + intermediatematrixx[2, 2]]])
		self.newmatrix = [float(self.matrix[0]),float(self.matrix[1]),float(self.matrix[2])]
		return self.newmatrix

#Takes the inputed matrix and multiplies is by the x rotation matrix

	def yrotate(self):
		intermediatematrixy = self.ymatrix()*self.matrix
		self.matrix = numpy.array([[intermediatematrixy[0, 0] + intermediatematrixy[0, 1] + intermediatematrixy[0, 2]], 
								  [intermediatematrixy[1, 0] + intermediatematrixy[1, 1] + intermediatematrixy[1, 2]], 
								  [intermediatematrixy[2, 0] + intermediatematrixy[2, 1] + intermediatematrixy[2, 2]]])
		self.newmatrix = [float(self.matrix[0]),float(self.matrix[1]),float(self.matrix[2])]
		return self.newmatrix

#Takes the inputed matrix and multiplies is by the y rotation matrix
	def zrotate(self):
		intermediatematrixz = self.zmatrix()*self.matrix
		self.matrix = numpy.array([[intermediatematrixz[0, 0] + intermediatematrixz[0, 1] + intermediatematrixz[0, 2]], 
								  [intermediatematrixz[1, 0] + intermediatematrixz[1, 1] + intermediatematrixz[1, 2]], 
								  [intermediatematrixz[2, 0] + intermediatematrixz[2, 1] + intermediatematrixz[2, 2]]])
		self.newmatrix = [float(self.matrix[0]),float(self.matrix[1]),float(self.matrix[2])]
		return self.newmatrix

#Takes the inputed matrix and multiplies is by the z rotation matrix

"""def matrixtransformation(listofpoints,number,alpha,beta,gamma):
	returnedlist = []
	for i in range(number):
		matrix = numpy.array([[listofpoints[i][0]],
							 [listofpoints[i][1]],
							 [listofpoints[i][2]]])
		rotatedmatrix = matrixdefinition(matrix,alpha,beta,gamma)
		rotatedmatrixlist = [float(rotatedmatrix.matrix[0,0]),
							 float(rotatedmatrix.matrix[1,0]),
							 float(rotatedmatrix.matrix[2,0])]
		returnedlist.append(rotatedmatrixlist)
	return returnedlist"""

class Sphere(object):
	def __init__(self,scale,number,center):
		self.scale = scale
		self.number = number
		self.center = center
		print(self.repeater())	

#initializes the instance of the class which sets attributes and calls the 
#repeater method as well as prints it.

	def spheresinglepoint(self):
		r = .5*self.scale
		theta = random.uniform(0,2*math.pi)
		phi = random.uniform(0,math.pi)
		x2 = r*math.cos(theta)*math.sin(phi) + self.center[0] 
		y2 = r*math.sin(theta)*math.sin(phi) + self.center[1]
		z2 = r*math.cos(phi) + self.center[2]
		spherepoint = "{{{0},{1},{2}}}".format(x2,y2,z2)
		return spherepoint

#this method generates the individual points, as spherical coordinates and 
#then converts them to cartesian.  It then puts those coordinates in 
#spherepoint as a formatted string and then returns it.

	def repeater(self):
		spherecoordinates = []
		for i in range(self.number):
			spherecoordinates.append(self.spheresinglepoint())
		spherestring = ",".join(spherecoordinates)
		return "{{{0}}}".format(spherestring)

##this method is called upon initialization and generates a point using the 
#spheresinglepoint method then appends the point to a list of coordinates
#once it goes through the designated number of times, it joins the list as a 
#string, formats it then returns it.

##############################################################################

def mathematicaize(listofpoints,number,capnumber):
	mathematicalist = []
	for i in range(number+capnumber):
		mathematicastring = "{{{:.5f},{:.5f},{:.5f}}}".format(listofpoints[i][0],listofpoints[i][1],listofpoints[i][2])
		mathematicalist.append(mathematicastring)
	newmathematicastring = ",".join(mathematicalist)
	newmathematicastring = "{{{0}}}".format(newmathematicastring)
	print newmathematicastring

#A function that will take a list of lists and turn them into a string that 
#has curly braces instead of square brackets

def partiviewize(listofpoints):
	speck = pvutil.Speck()
	for item in listofpoints:
		record = speck.Record(*item)
		speck.insert(record,0)
	print speck

#A function that will take a list of lists as an arg and using a module written by 
#Keith Davis, Director of the Digital Visualization Theater, University of 
#Notre Dame, turn that list of lists into a speck file format.

##############################################################################


if __name__ == "__main__":

	scale = 4

	#this is used to scale the end result, the larger the n, the larger the end 
	#shape is

	number=100

	#this is used to set how many points we generate for each shape, the higher 
	#this is, the more points

	centertest = [0,0,0]
	sphere1center = [-4,0,0]
	sphere2center = [4,0,0]

	#this is used to set the center of the geometric objects

	c = Cylinder(scale,number,centertest,math.pi/2,math.pi/2,math.pi/2)


	#This writes the speck object to a speck file which is used by partiview
	#to open up and plot coordinates

	f = open("/Users/patricklink/Digital Universe/data/pythontest/dumbellspeck.speck","w")
	f.write(c.partiviewize())
	c.checkrotate()
	f.write(c.partiviewize())
	f.close()

	#This opens the .cf config file containing the written speck file using bash
	#subprocess.Popen(["cd; Digital\ Universe/./partiview Digital\ Universe/./data/pythontest/dumbell.cf"], shell=True)

	print c.points
