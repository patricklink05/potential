import random
import math
import string
scale = 4
#this is used to scale the end result, the larger the n, the larger the end shape is
number=1
#this is used to set how many points we generate for each shape, the higher this is, the more points

class cylinder:
	def __init__(self,scale,number,center):
		self.scale = scale
		self.number = number
		self.center = center
	def cylinder(self,scale):
		r = .125*scale
		theta = random.uniform(0,2*math.pi)
		x = scale*random.uniform(-1,1)
		y = scale*math.cos(theta)
		z = scale*math.sin(theta)
		cylinder1point = "{{{0},{1},{2}}}".format(x2,y2,z2)
		print("{{{0}}}".format(cylinder1point))
	def repeater(self,number):
		for i in range(number):
			cylinder1coordinates = cylinder1coordinates + cylinder1point

cylinder1 = cylinder(1,10,0)
print("{{{0}}}".format(cylinder1))
#this function generates a set of coordinates within a cylinder centered at 0,0,0 and scaled by n, then returns them
def sphere2(n):
	r = .5*n
	theta = random.uniform(0,2*math.pi)
	phi = random.uniform(0,math.pi)
	x2 = r*math.cos(theta)*math.sin(phi) + n 
	y2 = r*math.sin(theta)*math.sin(phi)
	z2 = r*math.cos(phi)
	sphere1point = "{{{0},{1},{2}}}".format(x2,y2,z2)
	print("{{{0}}}".format(sphere1point))
#this generates a set of coordinates as floats within a sphere centered at n,0,0 and scaled by n, then returns them
def sphere3(n):
	r = .5*n
	theta = random.uniform(0,2*math.pi)
	phi = random.uniform(0,math.pi)
	x3 = r*math.cos(theta)*math.sin(phi) - n
	y3 = r*math.sin(theta)*math.sin(phi)
	z3 = r*math.cos(phi)
	sphere2point = "{{{0},{1},{2}}}".format(x2,y2,z2)
	print("{{{0}}}".format(sphere2point))

