"""
Minimal network
Problem 107
The following undirected network consists of seven vertices and twelve edges with a total weight of 243.


The same network can be represented by the matrix below.

    	A	B	C	D	E	F	G
A	-	16	12	21	-	-	-
B	16	-	-	17	20	-	-
C	12	-	-	28	-	31	-
D	21	17	28	-	18	19	23
E	-	20	-	18	-	-	11
F	-	-	31	19	-	-	27
G	-	-	-	23	11	27	-
However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243  93 = 150 from the original network.


Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.
"""

import time
ras=time.time()

f=open("/Users/isadmin/Downloads/Problem107_MinimalNetwork/network.txt")

d=[	0,	16,	12,	21,	0,	0,	0,\
	16,	0,	0,	17,	20,	0,	0,\
	12,	0,	0,	28,	0,	31,	0,\
	21,	17,	28,	0,	18,	19,	23,\
	0,	20,	0,	18,	0,	0,	11,\
	0,	0,	31,	19,	0,	0,	27,\
   0,	0,	0,	23,	11,	27, 0]

 
cost=set()
grid={}
"""
for i in range(7):
    grid[i]=[]
for i in range(7):
    for j in range(7):
        if d[i*7+j]!=0:
            grid[i].append(j)
            year=[i,j]
            year.sort()
            year=tuple(year)
            century=(int(d[i*7+j]),year)
            cost.add(century)

""" 


d=f.readlines()
 
cost={}
places=[]
possiblecost=set()
thetotal=0 
   
for num in range(0,40):
 
 
    i=d[num] 
    fox=i.split(",")
    for NUM in range(40)  :
        j=fox[NUM]
        if j !="-" :
            j=j.replace("\n","")
            if j!="-":
                thetotal+=int(j)
                if int(j) not in cost:
                    possiblecost.add(int(j))
                    cost[int(j)]=[]
                cost[int(j)].append((num,NUM))
       
print thetotal/2  
                
possiblecost=list(possiblecost)
possiblecost.sort()
 
               
 

 
 
total=0

g=0 
nodes=[2]
while  (len(nodes)!=40):
    cat=True
    for i in possiblecost:
        if not cat:
            break
        for each in cost[i]:
            a,b=each
            if a in nodes and b not in nodes:
                print a," in node ", b, " not in node"
                print "ADDING ",b
                 
                total+=i
                nodes.append(b)
                print nodes
                print "THE TOTAL is ",total
                cat=False
                break
    
    
    
     

print "THE SAVINGS ",thetotal/2-total   
            
  
 
