import math

def naive(total):
	f = open('../data/train','r')
	line = f.readline()

	# Hash of nonspam words
	Ham ={}
	#number of nonspam emails
	nham =0
	hamWords =0

	#hash of spam words
	Spam ={}
	#number of spam emails
	nspam =0
	spamWords=0

	#nu
#	total = 3000;

	while(line):
		
		email = line.split(' ')
		if(email[1]=='ham'):
			i=2
			while(i<len(email)-1):
				word = email[i]
				count= int(email[i+1])
				if(Ham.has_key(word)==True):
					Ham[word] = Ham[word]+count
				else:
					Ham[word]=count
				i+=2
				hamWords+=count
			nham+=1
			
		else:
			i=2
			while(i<len(email)-1):
				word = email[i]
				count= int(email[i+1])
				if(Spam.has_key(word)==True):
					Spam[word] = Spam[word]+count
				else:
					Spam[word]=count
				i+=2
				spamWords+=count
			nspam+=1
		line = f.readline()
		total-=1
		if(total==0):
			break
	f.close()

	dict = len(Spam)+len(Ham)+763



	ftest = open('../data/test','r')
	line = ftest.readline()
	val =1
	error =0

	while(line):
		email = line.split(' ')
		i=2
		pham =0.0
		pspam=0.0
		
		while(i<len(email)-1):
				
				word = email[i]
				count= int(email[i+1])
				if(Ham.has_key(word)==True):
					val = float(Ham[word]+1)/(dict+hamWords)
				else:
					val = float(1)/(dict+hamWords)
				
				pham = pham+ count*(math.log(val))
				i+=2
		#pham = pham+math.log(float(nham)/(nham+nspam))
		i=2			
		while(i<len(email)-1):
				word = email[i]
				count= int(email[i+1])
				if(Spam.has_key(word)==True):
					val = float(Spam[word]+1)/(dict+spamWords)
				else:
					val = float(1)/(dict+spamWords)
				pspam = pspam+ count*(math.log(val))
				i+=2
		
		if(email[1]=='ham' and pspam > pham):
			error+=1
		if(email[1]=='spam' and pspam < pham):
			error+=1
		line = ftest.readline()
	
	arr = Ham.items()
	brr = Spam.items()
	i =0
	top ={}
	for i in range(len(arr)):
		if(Spam.has_key(arr[i][0])):
			ratio = Spam[arr[i][0]]/Ham[arr[i][0]]
			top[arr[i][0]] = ratio
	arr= top.items()
	arr.sort(key=lambda tup: tup[1])
	#print arr
	#print Spam['Mier']
	return (1000-error)/10
	
train =1000

while(train<10000):
	print train,'\t',naive(train)
	train+=1000
	
