a=(int(input("enter the year:")))
if a<0:
    print("invalid")
elif a%4 ==0:
    print("the year is leap")
else:
    print("the year is not leap")
