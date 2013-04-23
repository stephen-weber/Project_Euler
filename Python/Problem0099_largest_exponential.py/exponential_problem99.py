d=open("/Users/sweber/Desktop/largest_exponential_problem99/base_exp.txt")

f=d.readlines()

import math
total=0
highestline=0
line=0
for i in f:
    u=i.replace("\n","")
    p=u.split(",")
    a=int(p[0])
    b=int(p[1])
     
    line=line+1
    g=b*math.log(a)
    if g>total:
        total=g
        highestline=line

print highestline
    

       
