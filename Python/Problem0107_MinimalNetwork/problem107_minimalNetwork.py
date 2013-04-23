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
f=open("/Users/sweber/Desktop/Problem107_MinimalNetwork/network.txt")

d=f.readlines()
grid={}
walk={}
cost=set()
 
for i in range(40):
    grid[i]=[]
for num in range(0,40):
    i=d[num] 
    fox=i.split(",")
    for NUM in range(40)  :
        j=fox[NUM]
        if j !="-" :
            j=j.replace("\n","")
            if j!="-":
                year=[num,NUM]
                year.sort()
                year=tuple(year)
                century=(int(j),year)
                cost.add(century)
                
                
                
                walk[(num,NUM)]=j
                
                grid[num].append(NUM)


cost=list(cost) 

 
                
def connected(t):
    connect=set()
    neighbors=[r for r in grid[t]]
    while neighbors:
        m=neighbors.pop()
        connected[t].add(m)
        for a in grid[m]:
            if a not in connected[t]:
                neighbors.append(a)
    return connected

 
cost.sort(reverse=True)


def add_to_list(cost_list,removed_list,value):
    newcostlist=[r for r in cost_list]
    new_removed_list=[r for r in removed_list]
    new_grid=[r for r in grid]
    g=newcostlist.pop()
    new_removed_list.append(g)
    value=sum(new_removed_list)
     
        
        
