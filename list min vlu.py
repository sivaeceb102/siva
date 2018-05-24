n=int(input())
l=[]
for i in range(1,n+1):
  a=int(input())
  l.append(a)
  print(l)
  min=l[0]
for i in l:
  if(i<min):
    min=i
print (min)
