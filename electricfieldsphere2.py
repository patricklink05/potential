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
		self.thetainterval = float(math.pi) / (self.number)
		self.phiinterval = float(math.pi) / self.number
		self.points = []
		self.charge = q
		self.r = r
		self.numcircles = 0
		self.pointspercircle = 0
		self.repeater()	
	#initializes the instance of the class which sets attributes and calls the 
	#repeater method as well as prints it.

	def spheresinglepoint(self,n_,m_):
		theta = -math.pi + n_ * self.thetainterval
		phi = 0 + m_ * self.phiinterval
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
		while self.phiinterval * (m) < 3.15:
			self.spheresinglepoint(n,m)
			self.numcircles = m + 1
			self.pointspercircle = n + 1
			if 6.26< n * self.thetainterval < 6.30:
				n = 0
				m +=1
			else:
				n += 1 
			
	def partiviewize(self):
		self.speck = pvutil.Speck()
		mesh_init = self.speck.Record("mesh -c 1 -s wire {", " ", " ")
		self.speck.append(mesh_init)
		rec_init = self.speck.Record(self.pointspercircle, self.numcircles, " ")
		self.speck.append(rec_init)
		for item in self.points:
			record = self.speck.Record(*item)
			self.speck.append(record)
		mesh_close = self.speck.Record("}", " ", " ")
		self.speck.append(mesh_close)
		self.speck = str(self.speck)
		return self.speck
	##this method is called upon initialization and generates a point using the 
	#spheresinglepoint method then appends the point to a list of coordinates
	#once it goes through the designated number of times, it joins the list as a 
	#string, formats it then returns it.



##############################################################################

def createspheres(numlayers,listcenters,numpoints):
	k = 8.99 * math.pow(10,9)
	q = 1.6 * math.pow(10,-9)
	z_ = listcenters
	f = open("/Users/patricklink/Digital Universe/data/pythontest/dumbellspeck.speck","w")
	r = 1
	for sph in range(0,len(z_)):
		for i in range(0,numlayers):
			r = k * q / (i + 1)
			s = Sphere(numpoints,listcenters[sph],r,q)
			f.write(s.partiviewize())
	f.close()

##############################################################################

if __name__ == "__main__":
	createspheres(10,[[0,0,0],[10,10,10]],75)
	subprocess.Popen(["cd; Digital\ Universe/./partiview Digital\ Universe/./data/pythontest/dumbell.cf"], shell=True)
