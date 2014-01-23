from matching import *
n=Node('root')
t=skillTree(n)
t.addUSL('/a/b/c/d')




n1=Node('1')
n2=Node('2')
n3=Node('3')
n4=Node('4')
n5=Node('5')
n6=Node('6')
n7=Node('7')
n8=Node('8')
n9=Node('9')
n10=Node('10')
n11=Node('11')

n1.add_child(n2)
n1.add_child(n5)
n2.add_child(n3)
n2.add_child(n4)

n4.add_child(n6)
n6.add_child(n7)
n6.add_child(n8)
hard=skillTree(n1)

