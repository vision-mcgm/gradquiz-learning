import psycopg2
from IPython import embed
from IPython.core.debugger import Tracer
from numpy import array,empty

class Test:

	def __init__(self):
		self.myList=empty(100,dtype='object')
		#self.recursiveLoad(self.myList,0)
		#finalList=self.recursiveLoad(self.myList,0)
		#print finalList

		#print self.myList
		self.B=B()
		self.B.BRecursiveLoad(self.myList,0)
		print self.myList

	def recursiveLoad(self,myList,place):
		myList[place]='a'
		self.myList=myList
		print 'storing in '+str(place)
		if place<10:
			self.recursiveLoad(myList,place+1)




	def recursiveLoad2(self,myList,place):
		myList[place]='a'
		print 'storing in '+str(place)
		if place<10:
			myList=self.recursiveLoad(myList,place+1)
		return myList




class B:
	def __init__(self):
		pass

	def BRecursiveLoad(self,myList,place):
		myList[place]='a'
		print 'storing in '+str(place)
		if place <10:
			myList=self.BRecursiveLoad(myList,place+1)
		return myList




