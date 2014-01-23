import psycopg2
from matching import *
print "Starting matching"

#Params
connString="dbname='gq' user='gq' host='localhost' password='cathedral'"
tableName='treeSpec1'
#DB connect
conn = psycopg2.connect(connString)
conn.autocommit=True;
c = conn.cursor()


#Fetch from DB
c.execute("""SELECT * FROM """+tableName)
rows=c.fetchall()
for row in rows:
	print "    ",row
n=Node(5)

print "Matching over"