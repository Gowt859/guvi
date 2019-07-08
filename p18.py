g1,g2=map(int,input().split())
for j in range(g1+1,g2):
    s=0
    a=j
    while(a>0):
        c=a%10
        s+=c**3
        a//=10
    if(j==s):
        print(j,end=" ")
