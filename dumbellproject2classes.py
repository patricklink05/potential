import random
import math
import numpy

##############################################################################

class cylinder:
	#This class defines a cylinder. The attributes that the class has are self, 
	#scale, number and center.  Self is agiven.  Scale is the geometric scale 
	#as the proportions of the cylinder are fixed.  The number is the number of 
	#points that the instance will generate and center is the center of the 
	#geometric shape.  Coordinates are generated as cylindrical coordinates then
	#converted to cartesian coordinates.  
	def __init__(self,scale,number,center,alpha,beta,gamma):
		self.scale = scale
		self.number = number
		self.center = center
		self.alpha = alpha
		self.beta = beta
		self.gamma = gamma
		self.area = 2*(.125*scale)*3*2*scale
		self.capnumber = int(number*4*math.pi*(.125*scale)*(.125*scale)/self.area)
		print(self.repeater())
	#initializes the instance of the class which sets attributes and calls the 
	#repeater method as well as prints it.
	def cylindersinglepoint(self):
		r = .125*self.scale
		theta = random.uniform(0,2*math.pi)
		x = self.scale*random.uniform(-1,1) + self.center[0]
		y = r*math.cos(theta) + self.center[1]
		z = r*math.sin(theta) + self.center[2]
		#print("{{{0},{1},{2}}},".format(x,y,z))
		rotatingmatrix = matrixdefinition(numpy.array([[x],[y],[z]]),self.alpha,self.beta,self.gamma)
		x = "{:.5f}".format(rotatingmatrix.matrix[0,0])
		y = "{:.5f}".format(rotatingmatrix.matrix[1,0])
		z = "{:.5f}".format(rotatingmatrix.matrix[2,0])
		cylinderpoint = "{{{0},{1},{2}}}".format(x,y,z)
		return cylinderpoint
	#this method actually generates the individual points, as cylindrical
	#coordinates and then converts them to cartesian.  It then puts those 
	#coordinates in cylinderpoint as a formatted string and then returns it.
	def cylindersinglepointcap(self):
		r = .125*self.scale*random.uniform(0,1)
		theta = random.uniform(0,2*math.pi)
		x = self.scale*random.choice([-1,1]) + self.center[0]
		y = r*math.cos(theta) + self.center[1]
		z = r*math.sin(theta) + self.center[2]
		rotatingmatrix = matrixdefinition(numpy.array([[x],[y],[z]]),self.alpha,self.beta,self.gamma)
		x = "{:.5f}".format(rotatingmatrix.matrix[0,0])
		y = "{:.5f}".format(rotatingmatrix.matrix[1,0])
		z = "{:.5f}".format(rotatingmatrix.matrix[2,0])
		cylinderpoint = "{{{0},{1},{2}}}".format(x,y,z)
		return cylinderpoint
	def repeater(self):
		cylindercoordinates = []
		for i in range(self.number):
			cylindercoordinates.append(self.cylindersinglepoint())
		for i in range(self.capnumber):
			cylindercoordinates.append(self.cylindersinglepointcap())
		cylinderstring = ",".join(cylindercoordinates)
		return "{{{0}}}".format(cylinderstring)
	#this method is called upon initialization and generates a point using the 
	#cylindersinglepoint method then appends the point to a list of coordinates
	#once it goes through the designated number of times, it joins the list as a 
	#string, formats it then returns it.


 
class matrixdefinition:
	#This class takes 4 args excluding itself:
	#	matrix = the input matrix that is to be rotated, given as a numpy.ndarray
	#	alpha = the angle of rotation for the x axis
	#	beta = the angle of rotation for the y axis
	#	gamma = the angle of rotation for the z axis
	#The purpose of the class is to rotate an inputed matrix and return it as the
	#post rotation matrix. 
	def __init__(self,matrix,alpha,beta,gamma):
		self.matrix = matrix
		self.alpha = alpha
		self.beta = beta
		self.gamma = gamma
		self.xrotate()
		self.yrotate()
		self.zrotate()
	def xmatrix(self):
		xmatrix = numpy.array([[1,0,0],[0,(math.cos(self.alpha)),-(math.sin(self.alpha))],[0,(math.sin(self.alpha)),(math.cos(self.alpha))]])
		return xmatrix
	def ymatrix(self):
		ymatrix = numpy.array([[(math.cos(self.beta)),0,(math.sin(self.beta))],[0,1,0],[-(math.sin(self.beta)),0,(math.cos(self.beta))]])
		return ymatrix
	def zmatrix(self):
		zmatrix = numpy.array([[(math.cos(self.gamma)),-(math.sin(self.gamma)),0],[(math.sin(self.gamma)),(math.cos(self.gamma)),0],[0,0,1]])
		return zmatrix
	def xrotate(self):
		intermediatematrixx = self.xmatrix()*self.matrix
		self.matrix = numpy.array([[intermediatematrixx[0,0]+intermediatematrixx[0,1]+intermediatematrixx[0,2]],[intermediatematrixx[1,0]+intermediatematrixx[1,1]+intermediatematrixx[1,2]],[intermediatematrixx[2,0]+intermediatematrixx[2,1]+intermediatematrixx[2,2]]])
		#print(intermediatematrix)
		return self.matrix
	def yrotate(self):
		intermediatematrixy = self.ymatrix()*self.matrix
		self.matrix = numpy.array([[intermediatematrixy[0,0]+intermediatematrixy[0,1]+intermediatematrixy[0,2]],[intermediatematrixy[1,0]+intermediatematrixy[1,1]+intermediatematrixy[1,2]],[intermediatematrixy[2,0]+intermediatematrixy[2,1]+intermediatematrixy[2,2]]])
		#print(intermediatematrix)
		return self.matrix
	def zrotate(self):
		intermediatematrixz = self.zmatrix()*self.matrix
		self.matrix = numpy.array([[intermediatematrixz[0,0]+intermediatematrixz[0,1]+intermediatematrixz[0,2]],[intermediatematrixz[1,0]+intermediatematrixz[1,1]+intermediatematrixz[1,2]],[intermediatematrixz[2,0]+intermediatematrixz[2,1]+intermediatematrixz[2,2]]])
		#print(intermediatematrix)
		return self.matrix

class sphere:
#This class defines a sphere. The attributes that the class has are self, 
#scale, number and center.  Self is agiven.  Scale is the geometric scale 
#as the proportions of the sphere are fixed.  The number is the number of 
#points that the instance will generate and center is the center of the 
#geometric shape.  Coordinates are generated as spherical coordinates then
#converted to cartesian coordinates.  	
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
c = cylinder(scale,number,centertest,0,0,0)
#s = sphere(scale,number,sphere1center)
#s2 = sphere(scale,number,sphere2center)