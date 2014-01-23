def toStr(self,store,row,depth):
    	for child in self.children:
    		row,store=child.toStr(store,row+1,depth+1) #Won't happen if no children
    	store[row,depth]=self.usl
    	return row,store