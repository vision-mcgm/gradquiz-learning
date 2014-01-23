#Assumptions
#USLs always start with a slash and do NOT end with a slash. This means slash count = level count.

def nLevels(usl):
	return usl.count('/')

def firstLevel(usl):
	return usl.partition('/')[0]