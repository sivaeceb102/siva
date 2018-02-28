lower=int(input("Enter the lower limit range:"))
upper=int(input("Enter the upper limit range:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
