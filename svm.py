import math
import svm

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
		label[itr] =-1
	else:
		label[itr] =1
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

trained = svm.train(lebel,x,'-t 0')



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
		label_test[itr] =-1
	else:
		label_test[itr] =1
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

[prediction,accuracy,values]= svm.predict(label_test,x_test,trained) 
