import time
ras=time.time()

import pickle
import copy
m=1

anagrams={}
bottom=0
 
number_list={}

algorithm={}

#words=pickle.load(open("/Users/sweber/Downloads/anagram/words.dic","rb"))

#horse=['NO', 'ON', 'ACT', 'CAT', 'DOG', 'GOD', 'EAT', 'TEA', 'HOW', 'WHO', 'ITS', 'SIT', 'NOW', 'OWN', 'CARE', 'RACE', 'DEAL', 'LEAD', 'EARN', 'NEAR', 'EAST', 'SEAT', 'FILE', 'LIFE', 'FORM', 'FROM', 'HATE', 'HEAT', 'ITEM', 'TIME', 'MALE', 'MEAL', 'MEAN', 'NAME', 'NOTE', 'TONE', 'POST', 'SPOT', 'STOP', 'RATE', 'TEAR', 'SHUT', 'THUS', 'SIGN', 'SING', 'SURE', 'USER', 'ARISE', 'RAISE', 'BOARD', 'BROAD', 'EARTH', 'HEART', 'LEAST', 'STEAL', 'NIGHT', 'THING', 'PHASE', 'SHAPE', 'QUIET', 'QUITE', 'SHEET', 'THESE', 'SHOUT', 'SOUTH', 'THROW', 'WORTH', 'CENTRE', 'RECENT', 'COURSE', 'SOURCE', 'CREDIT', 'DIRECT', 'DANGER', 'GARDEN', 'EXCEPT', 'EXPECT', 'FORMER', 'REFORM', 'IGNORE', 'REGION', 'CREATION', 'REACTION', 'INTRODUCE', 'REDUCTION']
 
words={1: [], 2: ['NO', 'ON'], 3: ['ACT', 'CAT', 'DOG', 'GOD', 'EAT', 'TEA', 'HOW', 'WHO', 'ITS', 'SIT', 'NOW', 'OWN'], 4: ['CARE', 'RACE', 'DEAL', 'LEAD', 'EARN', 'NEAR', 'EAST', 'SEAT', 'FILE', 'LIFE', 'FORM', 'FROM', 'HATE', 'HEAT', 'ITEM', 'TIME', 'MALE', 'MEAL', 'MEAN', 'NAME', 'NOTE', 'TONE', 'POST', 'SPOT', 'STOP', 'RATE', 'TEAR', 'SHUT', 'THUS', 'SIGN', 'SING', 'SURE', 'USER'], 5: ['ARISE', 'RAISE', 'BOARD', 'BROAD', 'EARTH', 'HEART', 'LEAST', 'STEAL', 'NIGHT', 'THING', 'PHASE', 'SHAPE', 'QUIET', 'QUITE', 'SHEET', 'THESE', 'SHOUT', 'SOUTH', 'THROW', 'WORTH'], 6: ['CENTRE', 'RECENT', 'COURSE', 'SOURCE', 'CREDIT', 'DIRECT', 'DANGER', 'GARDEN', 'EXCEPT', 'EXPECT', 'FORMER', 'REFORM', 'IGNORE', 'REGION'], 7: [], 8: ['CREATION', 'REACTION'], 9: ['INTRODUCE', 'REDUCTION'], 10: [], 11: [], 12: [], 13: [], 14: []}

 


def create_words():
    global number_list
    global m
    for i in words[m]:
        number_list[i]=[]
 

def algorithm_list():
    global m
    global words
    

    for rr in range(len(words[m])):
           gg=words[m][rr]
            
           q=[w for w in gg]   
           q=set(q)
           answer=[]
           for i in q:
                h=gg.count(i)
                n=[]
                for p in range(h):
                     k=gg.index(i,p)
                     n.append(k)        
                answer.append(tuple(n))
           answer.sort()
           answer=tuple(answer)
           algorithm[gg]=[q,answer]
 
     

def make_anagrams():
    global words
    global m
    flush={}
    for i in words[m]:
        x=[r for r in i]
        x.sort()
        flush[i]=x
        anagrams[i]=[]
    for i in range(len(words[m])):
        y=flush[words[m][i]]
        for j in range(len(words[m])):
            if i!=j:
                if flush[words[m][j]]==y:
                    anagrams[words[m][i]].append(words[m][j])   
    
 
 
        
def create_numbers():
    global top
    global bottom
    for xx in xrange(top,bottom-1,-1):
         f=xx*xx
         r=str(f)
         q=[w for w in r]
         answer=[]
         for i in q:
              h=r.count(i)
              n=[]
              for p in range(h):
                   k=r.index(i,p)
                   n.append(k)      
              answer.append(tuple(n))  
         answer.sort()
         yield [r,tuple(answer)]
          


 

 
def create_number_lists():
    global m
    global words
    global number_list
    weird=set()
    for i in words[m]:
        weird.add(algorithm[i][1])
   
    for num,ans  in create_numbers():
        
        if ans in weird:
       
            for gg in words[m]:
                 
                    kitten=algorithm[gg][1]
                    if kitten==ans:
                           number_list[gg].append([num,algorithm[gg][0]])


                                     
         

def check_words():
    global words
    global m
    global anagrams
     
    for a in range(len(words[m])):
        if words[m][a] in anagrams:
            
            for b in anagrams[words[m][a]]:
           
                answer,z1,z2=loop_words(words[m][a],b)
                if not answer:
                    break
                else:
                    print words[m][a],z1,"...",b,z2
                    return True


def loop_words(word1,word2):
  
    global number_list
     
    for numA,lettersA in number_list[word1]:
        for numB,lettersB in number_list[word2]:
                sameletters=lettersA.intersection(lettersB)
                print lettersA,lettersB,sameletters
             
                if not check_letters(word1,word2,sameletters,numA,numB):
                    break
                else:
                    return True,numA,numB
    return False,0,0
                
def check_letters(word1,word2,sameletters,numA,numB):
    for letter in sameletters:
                #print word1,numA,letter,numA[word1.index(letter)]
                #print word2,numB,letter,numB[word2.index(letter)]
                #print "."
                if numA[word1.index(letter)]!=numB[word2.index(letter)]:
                    return False
        
    return True
    
            
                
"""
#words[4]=["care","race"]
create_words()
algorithm_list()
create_numbers()
acceptable_words()
check_words()
"""

def run():
    global m
    global top
    global bottom
    for m in range(1,10):
        print ".........................................................."
        print "WE ARE AT Length of ",m
        print words[m]
         
        
        top=int((10**(m))**.5)  

        bottom=int((10**(m-1))**.5)-1
        
        number_list.clear()
        algorithm.clear()
        anagrams.clear()
         
        create_words()
        algorithm_list()
        make_anagrams()
 
         
        create_number_lists()
         
  
        check_words()
         
 


 

 

run()

print time.time()-ras
