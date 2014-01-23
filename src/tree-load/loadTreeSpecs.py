import psycopg2

#Params
fname='treeSpec1.txt'
tableName='treeSpec1'
load=True

#Code

print('Loading abstract tree structure into DB...')

conn = psycopg2.connect("dbname='gq' user='gq' host='localhost' password='cathedral'")
conn.autocommit=True;
c = conn.cursor()




#Load DB:
if load:
	c.execute('DROP TABLE '+tableName)
#c.execute("""CREATE TABLE """+tableName+""" (id serial PRIMARY KEY, num integer, data varchar);""")
	c.execute("""CREATE TABLE """+tableName+""" (TRL varchar(255));""")
	with open(fname) as f:
	    content = f.readlines()
	    skillCounter=1;
	    #Loop over skills in text file
	    for line in content:
	    	if not line[0]=='#':
	    		if len(line)>1:
	    			justLine=line[0:-1]
	    			print str(skillCounter)+ ' '+str(len(justLine)) +':: '+justLine
	    			skillCounter+=1;
	    			#Load to database:
	    			statement="""INSERT INTO """ +tableName+ """ VALUES ('""" +justLine+ """');"""
	    			print '       '+statement
	    			c.execute(statement)


 #Display DB contents to check:

print "Displaying contents:"

c.execute("""SELECT * from """+tableName)
rows = c.fetchall()
for row in rows:
	print "   ", row



print('Done.')