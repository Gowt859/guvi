g1=int(input())
lst=list(map(int,input().split()))[:g1]
lst.sort()
print(*lst,end=" ")
