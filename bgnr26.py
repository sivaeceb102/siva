n=int(input())
l=[]
for i in range(1,n+1):
  a=int(input())
  l.append(a)
  l.sort()
  print(l)
k=len(l)
median=0
if(k%2==0):
  median=(l[k//2 + k//2-1])/2
else:
  median=(l[k//2])
print(median)
