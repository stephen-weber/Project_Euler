from maya.cmds import  *
import math
select(all=True)
delete()
circle(n="g",nr=[0,1,0],s=6,d=1)
planarSrf(n="hex",d=3,ko=0,rn=1,po=1)
delete("g") 
select("hex.e[7]",r=True)
delete()
select("hex.e[1]",r=True)
delete()
select("hex",r=True)
polyExtrudeFacet(thickness=.2)
select(all=True)
polyBevel(offset=.03)
rot=math.pi/6
length=3**.5#4*math.sin(math.pi/6)
 
k=1
r=1
y=0
t=7
p=0
xx=0
zz=0
xxx=0
zzz=0 
for i in range(2,60):
    if (i-1)%(t)==0:
        print i
        k=k+1
        r+=1
        y-=.5
         
        t+=6*r
        length=3**.5*k
     
     
    rot=math.pi/(3*r)
    select("hex",r=True)
    duplicate()
    if i%r==0:
        x=length*math.cos(i*rot )
        z=length*math.sin(i*rot )
        xx=length*math.cos((i+r)*rot)
        zz=length*math.sin((i+r)*rot)
        xxx=(xx-x)/r
        zzz=(zz-z)/r
    else:
        x+=xxx
        z+=zzz
        
        
     
    #print math.cos(t/6*math.pi/180) 
    if (i-1)%t==0:
      rotate (0, i*rot*180/math.pi,0)
      p=i*rot*180/math.pi
    else:
 
        rotate(0,p,0)
    if r>1 and (i-1)%t==0:
        x-=math.cos(math.pi/6/r)
        y-=math.sin(math.pi/6/r)
    move(x,0,z)

    
    

 


 