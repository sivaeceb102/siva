m=float(input("enter the first number:"))
n=float(input("enter the second number:"))
s=int(input("select any operator: \n 1]add \n 2]sub \n 3]mul \n 4]div \n 5]rem \n 6]squ \n 7]pwr \n"))
if(s==1):
  print (m+n)
elif (s==2):
  print (m-n)
elif (s==3):
  print (m*n)
elif (s==5):
  print (m%n)
elif (s==6):
  print (m**2)
elif (s==7):
  print (m**n)
elif (s==4):
    if (n==0):
        print ("exception")
    else:
        print (m/n)
else:
  print("invalid") 
