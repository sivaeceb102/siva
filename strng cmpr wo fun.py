a=input()
b=input()
if(len(a)<len(b)):
  print (b)
elif(len(b)<len(a)):
  print (a)
elif(len(a)==len(b)):
  c=max(a and b)
  if(c in a):
    print(a)
  else:
    print(b)
