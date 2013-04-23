"""
Hexagonal tile differences
Problem 128
A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles, starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise direction.

New rings are added in the same fashion, with the next rings being numbered 8 to 19, 20 to 37, 38 to 61, and so on. The diagram below shows the first three rings.


By finding the difference between tile n and each its six neighbours we shall define PD(n) to be the number of those differences which are prime.

For example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 1, and 13. So PD(8) = 3.

In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, hence PD(17) = 2.

It can be shown that the maximum value of PD(n) is 3.

If all of the tiles for which PD(n) = 3 are listed in ascending order to form a sequence, the 10th tile would be 271.

Find the 2000th tile in this sequence.


Answer:
14516824220
Completed on Sat, 20 Apr 2013, 07:32

"""
import time
ras=time.time()

xxx=100000000  

import time
ras=time.time()
import random
pill=0
import itertools

        
 
def is_Prime(n):
    #Miller-Rabin test for prime
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
  
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True
r=0
num=0 
pd=3 #for 1 and 2 and 8 see check below

def number_primes_in_hex():
    global num
    global r
    global pill
    
    r=2
    
    t=set()
    global pd
    check=[]
    p=8
    n=3*r**2-3*r+2
    while pd<2001:
             
            check=[]
            if p==n+6*r:
                
                r+=1
                 
                
                n=3*r**2-3*r+2
            num=6*r #number in ring
            
 

##            if p>n and p<(n+r):
##                check=[(-num+6),(-num+5),(+num),(+num+1)]

##            elif p>(n+r) and p <(n+2*r):
##                check=[(-num+5),(-num+4),(+num+1),(+num+2)]
 
##            elif p>(n+2*r) and p < (n+3*r):
##                check=[(-num+4),(-num+3),(+num+2),(+num+3)]
 
##            elif p>(n+3*r) and p < (n+4*r):
##               check=[(-num+3),(-num+2),(+num+3),(+num+4)]
 
##            elif p>(n+4*r) and p < (n+5*r):
##              
##               check=[(-num+2),(-num+1),(+num+4),(+num+5)]
## 
##            elif p>(n+5*r) and p < (n+num-1):
##                
##               check=[(-num+1),(-num),(+num+5),(+num+6)]
            if p==n:
                check=[(+num),(+num+1),(+2*num+5),(+num-1),(-num+6)]
                 
               
##            elif p==(n+r):
##                check=[(-num+5),(+num),(+num+1),(num+2)]
##            elif p==(n+2*r):
##                check=[(-num+4),(+num+1),(+num+2),(+num+3)]
##            elif p==(n+3*r):
##                check=[(-num+3),(+num+2),(+num+3),(+num+4)]

            elif p==(n+num-1):
                
                check=[(-num+1),(-2*num+7),(-num),(+num+5),(+num+6)]
                
            
##            elif p==(n+5*r):
##         
##                check=[(-num+1),(+num+4),(+num+5),(+num+6)]
##            elif p==(n+4*r):
##                check=[(-num+2),(+num+3),(+num+4),(+num+5)]
##        


            t=0
            
            for item in check:
                y=abs(item)
                if is_Prime(y):
                    t+=1
         
                
            
            
            if t==3:
                  pd+=1

                  print pd,":","this is one ",p,time.time()-pill
                  pill=time.time()
            #print p,":",r,n,offset,check
         
        


                
#number_primes_in_hex()        
""" 
given r n=(0,6*r-1)

corners  n%r==0

"""
"""
            
        if p==1:
            check=[2,3,4,5,6,7]
        elif p==2:
            check=[9,8,19,7,1,3]
        elif p==3:
            check=[9,2,1,4,11,10]
        elif p==4:
            check=[3,1,5,13,12,11]
        elif p==5:
            check=[4,1,6,15,14,13]
        elif p==6:
            check=[1,7,17,16,15,5]
        elif p==7:
            check=[1,2,19,18,17,16,6]
        else:
"""

def in_hex():
    global num
    global r
    global pill
    
    r=2
    
    t=set()
    global pd
    check=[]
    p=8
    n=3*r**2-3*r+2
    while pd<2000:
              
            
            num=6*r #number in ring
            p+=6*r-1
              
            check=[(-num+1),(-2*num+7),(-num),(+num+5),(+num+6)]

           
            t=0
            
            for item in check:
                y=abs(item)
                if is_Prime(y):
                    t+=1
            
            if t==3:
                  pd+=1

                  #print pd,":",p
                 
  
            
              #number in ring
            p+=1
            r+=1
            num=6*r
 

            check=[(+num),(+num+1),(+2*num+5),(+num-1),(-num+6)]
                
             
          
            t=0
            
            for item in check:
                y=abs(item)
                if is_Prime(y):
                    t+=1
            
            if t==3:
                  pd+=1

                  #print pd,":", p
    print pd,":", p," in  ",time.time()-ras
           
               
in_hex()
