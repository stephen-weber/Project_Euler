import time
ras=time.time()

import pickle
import copy
m=6
#words[4]=["care","race"]
answer=[]
#words[14]=["fffuthhiiqqqww"]
maxnum=0
top=int((10**(m))**.5) -1

bottom=int((10**(m-1))**.5)
print top
print bottom
print "...."
 
 
print
word_list={}
case=[]
numbers=[]
wod=[]
laws=set()
 
#words=pickle.load(open("/Users/isadmin/Documents/pythonCode/words.dic","rb"))
words={1: [], 2: ['NO', 'ON'], 3: ['ACT', 'CAT', 'DOG', 'GOD', 'EAT', 'TEA', 'HOW', 'WHO', 'ITS', 'SIT', 'NOW', 'OWN'], 4: ['CARE', 'RACE', 'DEAL', 'LEAD', 'EARN', 'NEAR', 'EAST', 'SEAT', 'FILE', 'LIFE', 'FORM', 'FROM', 'HATE', 'HEAT', 'ITEM', 'TIME', 'MALE', 'MEAL', 'MEAN', 'NAME', 'NOTE', 'TONE', 'POST', 'SPOT', 'STOP', 'RATE', 'TEAR', 'SHUT', 'THUS', 'SIGN', 'SING', 'SURE', 'USER'], 5: ['ARISE', 'RAISE', 'BOARD', 'BROAD', 'EARTH', 'HEART', 'LEAST', 'STEAL', 'NIGHT', 'THING', 'PHASE', 'SHAPE', 'QUIET', 'QUITE', 'SHEET', 'THESE', 'SHOUT', 'SOUTH', 'THROW', 'WORTH'], 6: ['CENTRE', 'RECENT', 'COURSE', 'SOURCE', 'CREDIT', 'DIRECT', 'DANGER', 'GARDEN', 'EXCEPT', 'EXPECT', 'FORMER', 'REFORM', 'IGNORE', 'REGION'], 7: [], 8: ['CREATION', 'REACTION'], 9: ['INTRODUCE', 'REDUCTION'], 10: [], 11: [], 12: [], 13: [], 14: []}

def create_words():
    global word_list
    global m
    for i in words[m]:
        word_list[i]=[]
    

        
def create_numbers():
    global numbers
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
         #print r
         numbers.append([r,tuple(answer)])
         yield [r,tuple(answer)]
          



def acceptable_words():
    global m
    global words
    global word_list
    global numbers
    for r,ans  in create_numbers():
            num=r
            cat=True
            for rr in range(len(words[m])):
                   gg=words[m][rr]
                   #print gg
                                      
                             
                   q=[w for w in gg]   
                   q=set(q)
                   #print q
                   answer=[]
                   for i in q:
                        h=gg.count(i)
                        n=[]
                        for p in range(h):
                             k=gg.index(i,p)
                             n.append(k)        
                        answer.append(tuple(n))
                   answer.sort()
                   #print  "answer",answer,num[1]
                   answer=tuple(answer)
                   
                    
                   if answer==ans:
                       #print  "answer",answer,num[1]
                       word_list[gg].append([r,q])

                   
            
            if check_words():
                    break
            

def check_words():
    global words
    global m

    for a in range(len(words[m])-1):
        for b in range(a+1,len(words[m])):
       
            answer,z1,z2=loop_words(words[m][a],words[m][b])
            if not answer:
                break
            else:
                print words[m][a],z1,"...",words[m][b],z2
                return True


def loop_words(word1,word2):
    global m
    global word_list
     
    for a,aa in word_list[word1]:
        for b,bb in word_list[word2]:
            sameletters=aa.intersection(bb)
            if not check_letters(word1,word2,sameletters,a,b):
                break
            else:
                return True,a,b
    return False,0,0
                
def check_letters(word1,word2,sameletters,a,b):
    for letter in sameletters:
                 
                if a[word1.index(letter)]!=b[word2.index(letter)]:
                    return False
    return True
    
            
                

#words[4]=["care","race"]
create_words()
create_numbers()
acceptable_words()
check_words()
    












     
