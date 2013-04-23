#Optimal Polynomial
#problem 101
#tried out polyfit an polkyval with numpy 
"""
If we are presented with the first k terms of a sequence it is impossible to say with certainty the value of the next term, as there are infinitely many polynomial functions that can model the sequence.

As an example, let us consider the sequence of cube numbers. This is defined by the generating function, 
un = n3: 1, 8, 27, 64, 125, 216, ...

Suppose we were only given the first two terms of this sequence. Working on the principle that "simple is best" we should assume a linear relationship and predict the next term to be 15 (common difference 7). Even if we were presented with the first three terms, by the same principle of simplicity, a quadratic relationship should be assumed.

We shall define OP(k, n) to be the nth term of the optimum polynomial generating function for the first k terms of a sequence. It should be clear that OP(k, n) will accurately generate the terms of the sequence for n  k, and potentially the first incorrect term (FIT) will be OP(k, k+1); in which case we shall call it a bad OP (BOP).

As a basis, if we were only given the first term of sequence, it would be most sensible to assume constancy; that is, for n  2, OP(1, n) = u1.

Hence we obtain the following OPs for the cubic sequence:

OP(1, n) = 1	1, 1, 1, 1, ...
OP(2, n) = 7n6	1, 8, 15, ...
OP(3, n) = 6n211n+6     	1, 8, 27, 58, ...
OP(4, n) = n3	1, 8, 27, 64, 125, ...
Clearly no BOPs exist for k  4.

By considering the sum of FITs generated by the BOPs (indicated in red above), we obtain 1 + 15 + 58 = 74.

Consider the following tenth degree polynomial generating function:

un = 1  n + n2  n3 + n4  n5 + n6  n7 + n8  n9 + n10

Find the sum of FITs for the BOPs.
"""

import numpy
import warnings
warnings.simplefilter('ignore', numpy.RankWarning)
def gr(n):
	return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
mm=[gr(n) for n in range(1,13)]
import numpy.ma as ma
eps = numpy.finfo(numpy.float32).eps  
x=numpy.array(range(1))
f=numpy.array(mm)
d=numpy.array(mm)
r=numpy.array(mm)

print r
total=1
for k in range(1,10):
    f=numpy.array(mm[:k+1])
    #   f=r[:k]
    
    print mm 
    x=numpy.array(range(1,k+2))
    print x,f,k
    d=numpy.polyfit(x,f,k)
    #print "COEFFICIETS ",d
    for i in range(1,k+2):
        print numpy.polyval(d,i),"  ",

   
    cat=True
    m=k+2
    while cat:
        print "<<",numpy.polyval(d,m)
        if numpy.polyval(d,m)!=r[k]:
            cat=False
            total+=numpy.polyval(d,m)
            print "total= ",total
        else:
          m+=1

    print
    print
    print
print "END TOTAL ",total
        
    
    
