"""import random
import math

def sphere2(n):
	r = .5*n
	theta = random.uniform(0,2*math.pi)
	phi = random.uniform(0,math.pi)
	x2 = r*math.cos(theta)*math.sin(phi) + n 
	y2 = r*math.sin(theta)*math.sin(phi)
	z2 = r*math.cos(phi)
	a = "{{{0},{1},{2}}}".format(x2,y2,z2)
	print("{{{0}}}".format(a))
sphere2(1)"""

import numpy
import math
#x = numpy.array([[2,1,1],[1,1,1],[1,1,1]])
#print(numpy.dot(x,x))

"""def matrixdefinition(theta):
	xmatrix = numpy.array([[1,0,0],[0,math.cos(theta),-math.sin(theta)],[0,math.sin(theta),math.cos(theta)]])
	ymatrix = numpy.array([[math.cos(theta),0,math.sin(theta)],[0,1,0],[-math.sin(theta),0,math.cos(theta)]])
	return xmatrix
print(matrixdefinition(0))"""

class matrixdefinition:
	def __init__(self,matrix,alpha,beta,gamma):
		self.matrix = matrix
		self.alpha = alpha
		self.beta = beta
		self.gamma = gamma
		self.xrotate()
		self.yrotate()
		self.zrotate()
		#print(self.ymatrix()*self.matrix)
		print(self.matrix)
	def xmatrix(self):
		xmatrix = numpy.array([[1,0,0],[0,round((math.cos(self.alpha)),10),-round((math.sin(self.alpha)),10)],[0,(math.sin(self.alpha)),round((math.cos(self.alpha)),10)]])
		#print xmatrix
		return xmatrix
	def ymatrix(self):
		ymatrix = numpy.array([[round((math.cos(self.beta)),10),0,round((math.sin(self.beta)),10)],[0,1,0],[-round((math.sin(self.beta)),10),0,round((math.cos(self.beta)),10)]])
		return ymatrix
	def zmatrix(self):
		zmatrix = numpy.array([[round((math.cos(self.gamma)),10),-round((math.sin(self.gamma)),10),0],[round((math.sin(self.gamma)),10),round((math.cos(self.gamma)),10),0],[0,0,1]])
		return zmatrix
	def xrotate(self):
		intermediatematrixx = self.xmatrix()*self.matrix
		#print intermediatematrixx
		self.matrix = numpy.array([[intermediatematrixx[0,0]+intermediatematrixx[0,1]+intermediatematrixx[0,2]],[intermediatematrixx[1,0]+intermediatematrixx[1,1]+intermediatematrixx[1,2]],[intermediatematrixx[2,0]+intermediatematrixx[2,1]+intermediatematrixx[2,2]]])
		#print self.matrix
		return self.matrix
	def yrotate(self):
		intermediatematrixy = self.ymatrix()*self.matrix
		#print intermediatematrixy
		self.matrix = numpy.array([[intermediatematrixy[0,0]+intermediatematrixy[0,1]+intermediatematrixy[0,2]],[intermediatematrixy[1,0]+intermediatematrixy[1,1]+intermediatematrixy[1,2]],[intermediatematrixy[2,0]+intermediatematrixy[2,1]+intermediatematrixy[2,2]]])
		#print self.matrix
		return self.matrix
	def zrotate(self):
		intermediatematrixz = self.zmatrix()*self.matrix
		#print intermediatematrixz
		self.matrix = numpy.array([[intermediatematrixz[0,0]+intermediatematrixz[0,1]+intermediatematrixz[0,2]],[intermediatematrixz[1,0]+intermediatematrixz[1,1]+intermediatematrixz[1,2]],[intermediatematrixz[2,0]+intermediatematrixz[2,1]+intermediatematrixz[2,2]]])
		#print self.matrix
		return self.matrix


class testclass:
	def __init__(self):
		print self.testmatrix()
		self.testmatrix()
	def testmatrix(self):
		matrix = matrixdefinition(numpy.array([[2],[1],[1]]),math.pi/3,0,0)
		print matrix


c = testclass()

#testmatrix = matrixdefinition(numpy.array([[2],[1],[1]]),math.pi/3,0,0)
#print(type(round(2.222,2)))
#print(math.cos(math.pi/3))
#print(numpy.array([[1],[2],[3]]))
#print(testmatrix.matrix[0,0])
#print(type(float(testmatrix.matrix[0,0])))


"""matrix1 = matrixdefinition(math.pi,math.pi,math.pi)
#print(matrix1.xmatrix())
testpointmatrix = numpy.array([[1],[2],[3]])
#print(testpointmatrix)
newmatrix = matrix1.xmatrix()*testpointmatrix
testpointmatrix = numpy.array([[newmatrix[0,0]],[newmatrix[1,1]],[newmatrix[2,2]]])
print(testpointmatrix)"""


