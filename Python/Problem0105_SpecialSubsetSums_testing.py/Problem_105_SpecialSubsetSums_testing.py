"""
Special subset sums: testing
Problem 105
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B)  S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B)  S(C).
For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to problems 103 and 106.
"""
#year=[20,31,38,39,40,42,45]
 
sets=[]
 
 
pppp=set()


def make_set(lineSet):
    global sets
   
    global pppp
 
    num=len(lineSet)

    n=range(1,num+1)
    import itertools
    pppp=set()
    sets=[]
    

    for k in range(1,len(n)+1):
       for i in itertools.combinations(n,k):
     
           sets.append(i)
      
    
     
    for ii in range(len(sets)-1):
        i=sets[ii]
        for jj in range(ii+1,len(sets)):
            j=sets[jj]
            g=[i,j]
            g.sort()
           
            h=set(i)
            t=set(j)
        
            if h.intersection(t)==set([]):
               pppp.add(tuple(g))
    pppp=list(pppp)
  
 
            
 
def check2( n):
    global pppp
    for a,b in pppp:
      
        a1=[]
        b1=[]
        for e in a:
                
                a1.append(n[e-1])
        for e in b:
                b1.append(n[e-1])
        #print a1,sum(a1),"=?=",sum(b1),b1
        if len(a)==len(b):
           
            if sum(a1)==sum(b1):
                print a1,sum(a1),sum(b1),b1,"+++"
                return False
        if len(a)>len(b):
           
            if sum(a1)<=sum(b1):
                print a1,sum(a1),sum(b1),b1,"////"
                return False
        if len(a)<len(b):
           
 
            if sum(a1)>=sum(b1):
                print a1,sum(a1),sum(b1),b1,"PPP"
                return False

    return True
            

def Start():
    global sets
    
    global pppp
    
    global pollution
    total=0
    sets=[]
   
    count=0
    golf= open("/Users/sweber/Desktop/Problem105_SpecialSubsetSums_testing/sets.txt")
    line =golf.readlines()
    lineSet=[]
    for i in line:
         
         
        d=i.split(",")
        lin=[int(str(e)) for e in d]
        lineSet.append(lin)

  
       
    for ape in lineSet:
        count+=1
        print count," : ",ape
        make_set(ape)
  
       
        cow=check2(ape)
        #print cow
        
        if cow:
            total=total+sum(ape)
            print count," : YES total=",total
        else:
            print count, " : NO THIS SECOND TEST FAILED"
         
      
         
        sets=[]
        
     
     
        pppp=set()
    print total
        
Start()    
 
 
 
