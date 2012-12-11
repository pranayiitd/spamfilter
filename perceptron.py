import math

def mult(a,b):
	mul=0
	for i in range(len(a)):
		mul=mul+a[i]*b[i]
	return mul

def add(a,b):
	for i in range(len(a)):
		a[i]=a[i]+b[i]
	return a

def norm(a):
	sum=0
	for i in range(len(a)):
		sum=sum+a[i]*a[i]
	return math.sqrt(sum)

label ={}
x ={}
f = open('../data/train','r')
line = f.readline()
itr =0
total = 1000;
Total = total
max_len =0
while(line):
	itr=itr+1
	email = line.split(' ')
	if(email[1]=='ham'):
		label[itr] =1
	else:
		label[itr] =0
	i=2
	arr= []
	while(i<len(email)-1):
		word = email[i]
		count= int(email[i+1])
		arr.append(count)
		i+=2
	x[itr] = arr
	if(len(arr)>max_len):
		max_len=len(arr)
	
	line = f.readline()
	total-=1
	if(total==0):
		break
	
f.close()

w=[0]*max_len
converge = False
while(converge!=True):
	delta_w =[0]*max_len
	while(itr>0):
		out = mult(x[itr],w)
		o=0
		if(out>0):
			o=1
		for j in range(len(x[itr])):
			delta_w[j] = delta_w[j]+0.1*(label[itr]-o)*(x[itr][j])
		w= add(w,delta_w)
		if(norm(delta_w) <0.01):
			converge = True
		
		itr-=1
	itr = Total
#print len(w),max_len


label_test ={}
x_test ={}
ftest = open('../data/test','r')
line = ftest.readline()
itr =0
max_len =0
while(line):
	itr=itr+1
	email = line.split(' ')
	if(email[1]=='ham'):
		label_test[itr] =1
	else:
		label_test[itr] =0
	i=2
	arr= []
	while(i<len(email)-1):
		word = email[i]
		count= int(email[i+1])
		arr.append(count)
		i+=2
	x_test[itr] = arr
	
	line = ftest.readline()
	
ftest.close()
error =0

while(itr>0):
	out = mult(x_test[itr],w)
	o=0
	if(out>0):
		o=1
	if(o!=label_test[itr]):
		error+=1
	itr-=1
print error
