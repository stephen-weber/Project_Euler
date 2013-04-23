"""
Repunit divisibility
Problem 129
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.


Answer:
1000023
Completed on Sun, 7 Apr 2013, 19:18


"""

#
# R(k)= (10^k-1)/9 in general
#

#
# R(k)=0 mod p
# (10^k-1)/9 = 0 mod p
# (10^k-1)   = 0 mod 9*P
#
# or  10^k   = 1 mod 9*P
#
# 
import time
ras=time.time()
maxim=0
these=[]
n=1000001
while True:
  if n%5==0 :
        n=n+2
  A=2
  dog=True
  while dog:
      
     if pow(10,A,9*n)==1:
        #print"...","       number of repunits:",A,"  divisible by:",n
        dog=False
     else:
         A+=1
     
  
  if A>maxim :
      maxim=A
      print "repunits are at a maximum of  ",maxim
  if A>1000000:
       
           break
  n+=2


print "the least divisor is ",n
print
print "This took ",time.time()-ras
