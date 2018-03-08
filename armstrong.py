num=int(input("enter the input: "))
sum=0
temp=num
while temp>0:
	digi = temp%10
	sum += digi ** 3
	temp //=10
if num == sum:
	print("yes")
else:
	print("no")
	
