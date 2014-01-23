
#IMPORTS

import psycopg2
from IPython import embed
from IPython.core.debugger import Tracer
from numpy import array,empty


from usl import *

#CLASSES

store2=empty([200,200],dtype='object')

class Node:
	#Constructor
    def __init__(self, usl):
        self.usl = usl
        self.children = []

        #Children
    def add_child(self, obj):
        self.children.append(obj)

    def toStr(self,store,row,depth):
    	global store2
    	for child in self.children:
    		row,store=child.toStr(store,row,depth+1) #Won't happen if no children
    		if len(self.children)>1:
    			row=row+1
    	print store
    	Tracer()
    	store[row,depth]=self.usl
    	store2[row,depth]=self.usl
    	print store

    	print 'storing '+self.usl+' in '+str(row)+' at '+str(depth)
    	print self.usl
    	return row,store

    def worra(self):
    	print 'worra'

    def hasChild(self,uriChunk):
    	#A URI chunk has no slashes
    	for child in self.children:
    		if child.usl==uriChunk:
    			return child
    	return False



class skillTree:
	def __init__(self,node):
		self.root=node

	def printDict():
		#Transpose and print dict
		pass


	def printTree(self):
		print 'Printing tree3'
		self.store=empty([200,200],dtype='object')
		
		row,self.store=self.root.toStr(self.store,0,0)
		print self.store
		print store2

		self.myList=empty(100,dtype='object')
	def recTest(self,myList,place):
		recTest(myList,place+1)
		myList[place]='a'
		


	def hasNode(self,usl):
		pass

	def addNodeTo(self,usl,new):
		pass

	def addUSL(self,usl):
		self.r_addUSL(self.root,usl)

	def r_addUSL(self,node,usl):
		#Recursive function
		if not node.children:
			#We have reached the bottom and can add the remaining URI
			if nLevels(usl)==1:
				node.add_child(usl)
			else:
				#We're not at the bottom
				first,rem=self.splitUSL(usl)
				newNode=Node(first)
				#Tracer()()
				self.r_addUSL(newNode,rem)
				node.add_child(newNode)
		else:
			#If we have not yet reached the bottom, check if next chunk exists
			first,rem=self.splitUSL(usl)
			chOrFalse=node.hasChild(first)
			if chOrFalse:
				self.r_addUSL(chOrFalse,rem)
			else:
				newNode=Node(first)
				self.r_addUSL(newNode,rem)
				node.add_child(newNode)


	def splitUSL(self,usl):
		parts=usl.split('/')
		return (parts[1],'/'+'/'.join(parts[2:]))


				


#FUNCTIONS

def dbConn():
	connString="dbname='gq' user='gq' host='localhost' password='cathedral'"
	#DB connect
	conn = psycopg2.connect(connString)
	conn.autocommit=True;
	return conn.cursor()

