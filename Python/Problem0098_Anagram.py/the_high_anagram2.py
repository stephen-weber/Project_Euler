import time
ras=time.time()

import pickle
import copy
m=1 

#words=pickle.load(open("/Users/sweber/Downloads/anagram/words.dic","rb"))

#horse=['NO', 'ON', 'ACT', 'CAT', 'DOG', 'GOD', 'EAT', 'TEA', 'HOW', 'WHO', 'ITS', 'SIT', 'NOW', 'OWN', 'CARE', 'RACE', 'DEAL', 'LEAD', 'EARN', 'NEAR', 'EAST', 'SEAT', 'FILE', 'LIFE', 'FORM', 'FROM', 'HATE', 'HEAT', 'ITEM', 'TIME', 'MALE', 'MEAL', 'MEAN', 'NAME', 'NOTE', 'TONE', 'POST', 'SPOT', 'STOP', 'RATE', 'TEAR', 'SHUT', 'THUS', 'SIGN', 'SING', 'SURE', 'USER', 'ARISE', 'RAISE', 'BOARD', 'BROAD', 'EARTH', 'HEART', 'LEAST', 'STEAL', 'NIGHT', 'THING', 'PHASE', 'SHAPE', 'QUIET', 'QUITE', 'SHEET', 'THESE', 'SHOUT', 'SOUTH', 'THROW', 'WORTH', 'CENTRE', 'RECENT', 'COURSE', 'SOURCE', 'CREDIT', 'DIRECT', 'DANGER', 'GARDEN', 'EXCEPT', 'EXPECT', 'FORMER', 'REFORM', 'IGNORE', 'REGION', 'CREATION', 'REACTION', 'INTRODUCE', 'REDUCTION']
#numbers=pickle.load(open("/Users/sweber/Downloads/anagram/numbers.dec","rb"))

words={1: [], 2: ['NO', 'ON'], 3: ['ACT', 'CAT', 'DOG', 'GOD', 'EAT', 'TEA', 'HOW', 'WHO', 'ITS', 'SIT', 'NOW', 'OWN'], 4: ['CARE', 'RACE', 'DEAL', 'LEAD', 'EARN', 'NEAR', 'EAST', 'SEAT', 'FILE', 'LIFE', 'FORM', 'FROM', 'HATE', 'HEAT', 'ITEM', 'TIME', 'MALE', 'MEAL', 'MEAN', 'NAME', 'NOTE', 'TONE', 'POST', 'SPOT', 'STOP', 'RATE', 'TEAR', 'SHUT', 'THUS', 'SIGN', 'SING', 'SURE', 'USER'], 5: ['ARISE', 'RAISE', 'BOARD', 'BROAD', 'EARTH', 'HEART', 'LEAST', 'STEAL', 'NIGHT', 'THING', 'PHASE', 'SHAPE', 'QUIET', 'QUITE', 'SHEET', 'THESE', 'SHOUT', 'SOUTH', 'THROW', 'WORTH'], 6: ['CENTRE', 'RECENT', 'COURSE', 'SOURCE', 'CREDIT', 'DIRECT', 'DANGER', 'GARDEN', 'EXCEPT', 'EXPECT', 'FORMER', 'REFORM', 'IGNORE', 'REGION'], 7: [], 8: ['CREATION', 'REACTION'], 9: ['INTRODUCE', 'REDUCTION'], 10: [], 11: [], 12: [], 13: [], 14: []}
number_list=pickle.load(open("/Users/sweber/Downloads/anagram/number_list.dec","rb"))
algorithm=pickle.load(open("/Users/sweber/Downloads/anagram/algorithm.dec","rb"))
anagrams=pickle.load(open("/Users/sweber/Downloads/anagram/anagrams.dec","rb"))

#anagrams[4]={'CARE':['RACE'],'RACE':['CARE']}
 
def check_words():
    global number_list
    global anagrams
    global m
    maximumValue=0
    aword1=""
    aword2=""
    value1=0
    value2=0
 
    for word1 in anagrams[m]:
         
            
            for word2 in anagrams[m][word1]:
                 
                             
                            
                            
                            C= [r[0] for r in number_list[word1]]
                            R= [r[0] for r in number_list[word2]]
  
                            if not number_list[word1]:
                                break
                            else:
                                if not number_list[word2]:
                                    break
                                else:
                                    c=number_list[word1][1][1]
                                    r=number_list[word2][1][1]
                                    
              
                                    
                                    sameletters=c.intersection(r)
                                    for numC in C:
                                         
                                            
                                        for numR in R:
                                            

                                            #print numC,numR,"        ",
                                            cat=True
                                             
                                            popcorn=[]
                                            for i in sameletters :
                                                 
                                                g =word1.index(i)
                                                base=numC[g]
                                                if base in popcorn:
                                                    cat=False
                                                else:
                                                    popcorn.append(base)
                                            popcorn=[]
                                            for i in sameletters:
                                                g=word2.index(i)
                                                base=numR[g]
                                                if base in popcorn:
                                                    cat=False
                                                else:
                                                    popcorn.append(base)
                                            
                                            for i in sameletters:
                                                g=word1.index(i)
                                                h=word2.index(i)
                                                if numC[g]!=numR[h]:
                                                    cat=False
                                         
                                            if cat:
                                                
                                                if numC>maximumValue:
                                                    maximumValue=numC
                                                    aword1=word1
                                                    aword2=word2
                                                    value1=numC
                                                    value2=numR
                                                if numR>maximumValue:
                                                    maximumValue=numR
                                                    aword1=word1
                                                    aword2=word2
                                                    value1=numC
                                                    value2=numR
                                                 
                                                
                                                    
                                                    
    return maximumValue  #aword1,value1,"   ",aword2,value2
                                   
                                                     
maxSquare=0            
 
def run():
    global m
    global top
    global bottom
    global maxSquare
    maxSquare=0
    for m in range(2,10):
     
       
         g=check_words()
          
         if int(g)>int(maxSquare):
             maxSquare=int(g)
    
  
    print maxSquare


run()

 

 
print time.time()-ras
