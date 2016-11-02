import math
import pvutil
import subprocess

class Sphere(object):
#This class defines a sphere. 
#The it takes 5 arguements--
#	self
#	number - the number of points generated, not the exact amount but the
#			 amount generated is proportional to this number.
#	center - [x,y,z] coordinate of the center of the object.  Must be a
#			 list of floats or ints.
#	r - radius of the sphere.
#	q - the charge of the point charge. While it is not as useful currently
#		this has potential uses in other application.
	def __init__(self,number,center,r,q):
		self.number = number
		self.center = center
		self.thetainterval = math.pi / (self.number)
		self.phiinterval = math.pi / self.number
		self.points = []
		self.charge = q
		self.r = r
		self.repeater()	
	#initializes the instance of the class which sets attributes and calls the 
	#repeater method as well as prints it.

	def spheresinglepoint(self,n_,m_):
		theta = 0 + n_ * self.thetainterval
		phi = -math.pi + m_ * self.phiinterval
		x2 = self.r * math.cos(theta) * math.sin(phi) + self.center[0] 
		y2 = self.r * math.sin(theta) * math.sin(phi) + self.center[1]
		z2 = self.r * math.cos(phi) + self.center[2]
		spheresinglepointlist = [x2, y2, z2]
		self.points.append(spheresinglepointlist)
	#this method generates the individual points, as spherical coordinates and 
	#then converts them to cartesian.  It then puts those coordinates in 
	#spherepoint as a formatted string and then returns it.

	def repeater(self):
		spherecoordinates = []
		n = 0
		m = 0
		while self.phiinterval * (m) < 6.30:
			self.spheresinglepoint(n,m)
			n += 1
			if 3.13< n * self.thetainterval < 3.15:
				n = 0
				m +=1

	def partiviewize(self):
		self.speck = pvutil.Speck()
		for item in self.points:
			record = self.speck.Record(*item)
			self.speck.insert(record,0)
		self.speck = str(self.speck)
		return self.speck
	##this method is called upon initialization and generates a point using the 
	#spheresinglepoint method then appends the point to a list of coordinates
	#once it goes through the designated number of times, it joins the list as a 
	#string, formats it then returns it.

##############################################################################

if __name__ == "__main__":

	scale = 4
	#number = 30
	center2 = [10,20,0]
	centertest = [-10,20,0]
	center6 = [-20,10,0]
	center8 = [-20,-10,0]
	center3 = [-10,-20,0]
	center4 = [10,-20,0]
	center7 = [20,-10,0]
	center5 = [20,10,0]
	origin = [0,0,0]


	q = 1.6 * math.pow(10,-9)
	k = 8.99 * math.pow(10,9)

	r = 1
	number = 50
	f = open("/Users/patricklink/Digital Universe/data/pythontest/dumbellspeck.speck","w")

	r = 1 
	number = 200
	for i in range(1,3):
		r = k * q / i
		s = Sphere(number,origin,r,q)
		number /= 2
		f.write(s.partiviewize())

	"""r = 1
	number = 50
	for i in range(1,3):
		r = k * q / i
		s = Sphere(scale,number,centertest,r,q)
		number /= 2
		print number
		f.write(s.partiviewize())
		#print s.partiviewize()

	r = 1 
	number = 50
	for i in range(1,3):
		r = k * q / i
		s = Sphere(scale,number,center6,r,q)
		number /= 2
		f.write(s.partiviewize())

	r = 1 
	number = 50
	for i in range(1,3):
		r = k * q / i
		s = Sphere(scale,number,center8,r,q)
		number /= 2
		f.write(s.partiviewize())

	r = 1 
	number = 50
	for i in range(1,3):
		r = k * q / i
		s = Sphere(scale,number,center3,r,q)
		number /= 2
		f.write(s.partiviewize())


	r = 1 
	number = 50
	for i in range(1,3):
		r = k * q / i
		s = Sphere(scale,number,center4,r,q)
		number /= 2
		f.write(s.partiviewize())

	r = 1 
	number = 50
	for i in range(1,3):
		r = k * q / i
		s = Sphere(scale,number,center7,r,q)
		number /= 2
		f.write(s.partiviewize())

	r = 1 
	number = 50
	for i in range(1,3):
		r = k * q / i
		s = Sphere(scale,number,center5,r,q)
		number /= 2
		f.write(s.partiviewize())

	r = 1
	number = 50
	for i in range(1,3):
		r = k * q / i
		s = Sphere(scale,number,centertest,r,q)
		number /= 2
		print number
		f.write(s.partiviewize())"""

	f.close()
	#print s.partiviewize()

	subprocess.Popen(["cd; Digital\ Universe/./partiview Digital\ Universe/./data/pythontest/dumbell.cf"], shell=True)



