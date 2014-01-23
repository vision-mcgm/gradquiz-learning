
from matching import *
print "Starting matching"

#Params
c=dbConn()
tableName='treeSpec1'


#Fetch from DB
c.execute("""SELECT * FROM """+tableName)
rows=c.fetchall()
for row in rows:
	print "    ",row
n=Node(5)

print "Matching over"