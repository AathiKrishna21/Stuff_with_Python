s=input("Enter name 1: ")
ss=input("Enter name 2: ")
f=['F','L','A','M','E','S']
s=list(s)
ss=list(ss)
li=s.copy()
for i in li:
    if(i in ss):
       ss.remove(i)
       s.remove(i)
l=len(s)+len(ss)
n=0
c=0
m=''
for i in range(1,len(f)):
    while(c<l):
        m=f[n]
        c=c+1
        n=n+1
        if(n>=len(f)):
            n=0        
    f.remove(m) 
    c=0 
    if(n!=0):
        n=n-1

st= ''.join(f)        
if st=="F":         
    print("Your relationship is : FRIENDSHIP")  
elif st=="L":         
    print("Your relationship is : LOVE")          
elif st=="A":         
    print("Your relationship is : AFFECTION")  
elif st=="M":         
    print("Your relationship is : MARRIAGE")  
elif st=="E":         
    print("Your relationship is : ENEMY")  
elif st=="S":         
    print("Your relationship is : SISTER")                  