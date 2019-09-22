list=[]
temp=0
a=int(input("Enter number of 100 notes:"))
b=int(input("Enter number of 200 notes:"))
c=int(input("Enter number of 500 notes:"))
d=int(input("Enter number of 1000 notes:"))
N=int(input("Enter max limit"))
x=int(input("Enter amount"))

max_amount=100*a+200*b+500*c+1000*d
if x>max_amount:
	print("0")
	exit()
for i in range(a+1):
	for j in range(b+1):
		for k in range(c+1):
			for l in range(d+1):
				temp=100*i+200*j+500*k+1000*l
				tot=i+j+k+l
				if temp==x and tot<N+1:
					list.append(tot)
print(max(list))
