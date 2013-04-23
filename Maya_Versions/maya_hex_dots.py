from maya.cmds import  *
import math
select(all=True)
delete()
circle(n="g",nr=[0,1,0],s=6,d=1)
planarSrf(n="hex",d=3,ko=0,rn=1,po=1,tol=.01)
rename("hex")
setAttr("nurbsTessellate1.uNumber",2)
setAttr("nurbsTessellate1.vNumber",2)
delete(ch=True)
delete("g") 
select("hex.e[7]",r=True)
delete()
select("hex.e[1]",r=True)
delete()
select("hex",r=True)
polyExtrudeFacet(thickness=.2)

polyBevel(offset=.03)
rot=0
length=3**.5#4*math.sin(math.pi/6)
radius=0 
k=1
r=1
y=.2
t=7
p=0
xx=0
zz=0
xxx=0
zzz=0 
lastone=0
face=0
select("hex",r=True)
duplicate()
 
root=0
 
for i in range(2,20):
    angle=math.pi*2/6/r
 
    if i>t:
        lastone=i
        r=r+1
        t+=6*r
        face=angle
      
    radius=length*r
     
     
    if (i-lastone)%r==0:
          
         face+=angle*r
         print i,"...",r,"  ",face
         xx=radius*math.cos(rot-(r)*angle)
         zz=radius*math.sin(rot-(r)*angle) 
         rot-=angle 
         x=radius*math.cos(rot)
         z=radius*math.sin(rot) 
     
 
         xxx= (xx-x) /r 
         zzz= (zz-z) /r
    else:
        print i,"___",face
        rot-=angle 
        x+=xxx
        z+=zzz
  
   
   
    select("hex",r=True)
    duplicate()
    
    move(x,0,z)
 
 

   