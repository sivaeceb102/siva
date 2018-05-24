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
  midle=(l[k//2 + k//2-1])/2
else:
  midle=(l[k//2])
print(midle)
