''' Problem Description 
Given N three-digit numbers, your task is to find bit score of all N numbers and then print the number of pairs possible based on these calculated bit score.
Rule for calculating bit score from three digit number: 
From the 3-digit number, 
extract largest digit and multiply by 11 then extract smallest digit multiply by 7 then add both the result for getting hit pairs, 
Note.-Bit score should he of 2eliges, if shove results in a edigit hit score, simply ignore most significant digit.'''
def bitscore(number):
    x=number
    b=int(x%10)
    x=int(x/10)
    c=int(x%10)
    x=int(x/10)
    s=[]
    s.append(b)
    s.append(x)
    s.append(c)
    print(s)
    g=max(s)
    l=min(s)
    d=g*11+l*7
    if d>99:
        d=str(d/100)
        t=[]
        t.append(d)
        k=[]
        k=t[0].split('.')
        d=int(k[1])
    return(d)

def eve(v):
    p=0
    for i in range(0,len(v),2):
        for j in range(2,len(v),2):
            if(i!=j):
                if(v[i]==v[j]):
                    p=p+1
    return(p)

def od(v):
    q=0
    for i in range(1,len(v),2):
        for j in range(3,len(v),2):
            if(i!=j):
                if(v[i]==v[j]):
                    q=q+1
    return(q)

n=int(input("enter no of digits : "))

a=[]
b=[]
for i in range(n):
    k=int(input('enter number : '))
    a.append(k)

for i in range(n):
    e=bitscore(a[i])
    b.append(e)
v=[]
l=[]
for i in range(len(b)):
    x=str(b[i]/10)
    v.append(x)
    l=v[i].split('.')
    v[i]=l[0]
pairs=eve(v)+od(v)

print(pairs)