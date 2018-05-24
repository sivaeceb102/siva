N=int(input())
l=[]
for i in range(1,N+1):
  a=int(input())
  l.append(a)
  print(l)
  max=l[0]
for i in l:
  if(i>max):
    max=i
print (max)
