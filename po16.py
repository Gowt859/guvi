g1,g2=map(int,input().split())
for j in range(g1,g2):
    if j>1:
        for i in range(2,j):
            if j%i==0:
                break
        else:
            print(j,end=" ")
