import pvutil
from collections import namedtuple

#This python file is not a formal code but rather more of a worksheet to help
#me understand the pvutil module and understand what class and function will 
#return in reponse to certain input. 

#test = pvutil.Speck()
#record = test.Record(11,11,11)

class testclass(object):
	def __init__(self,test):
		self.test = test
		self.records = []
	def record(self):
		mesh = self.test.Mesh(colorindex = 1)
		print type(mesh)
		for item in range(10):
			record = self.test.Record(item, item + 1, item + 2)
			mesh.append(record)
			"""if item == 9:
				record = self.test.Record(1,10,"")
				print record
				mesh.insert(record,0)"""
		return mesh
test = pvutil.Speck()
testobject = testclass(test)
#print testobject.record()


#test.insert(record,0)
#print test

"""s = ""
        for r in self.records:
            s += str(r) + "\n"
        return s"""
