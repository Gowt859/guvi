g1=int (input())
sum=0
s=g1
while s>0:
  digit=s%10
  sum+=digit**3
  s//=10
if g1==sum:
    print("yes")
else:
    print("no")      
