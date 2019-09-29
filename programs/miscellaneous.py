# description: to create multi dictionary including dictionary, list and set
def mdict():
	a={}
	n1=int(input('enter number of elements to outer dict'))
	for i in range(n1):
		key=input('enter the outer key')
		type=int(input('enter dict to add dict\nlist to add list\nset to add set'))
		
		# other method to code type==1

		# if type == 1:
		# 	n2=int(input('enter number of key value pairs for inner dict'))
		# 	if n2==1:
		# 		value=input('enter value')
		# 		a[key]=value
		# 	if n2>1:
		# 		b={}
		# 		for j in range(n2):
		# 			key1=input('enter inner key')
		# 			value1=input('enter value')
		# 			b[key1]=value1
		# 		a[key]=b
		#print(a)

		if type==2:
			c=[]
			n3=int(input('enter the number of elements for list'))
			for k in range(n3):
				e=int(input('enter list element'))
				c.append(e)
			a[key]=c
		#print(a)

		if type==3:
			d=set()
			n4=int(input('enter the number of elements to be added'))
			for l in range(n4):
				e1=(input('enter the set element'))
				d.add(e1)
			a[key]=d
		print(a)

		if type==1:
			d1={}
			c1=int(input('enter no of key value pairs'))
			for m in range(c1):
				ckey=input('enter key')
				cvalue=input('enter value')
				d1[ckey]=cvalue
			a[key]=d1
			print(a)
		else:
			f=input('enter single value')
			a[key]=d
			print(a)
mdict()

###########################################################
# creating multilist including elements as integer, float, list

def mlist():
	a=[]
	n=int(input('enter the number of elements for outer list : '))
	for i in range(n):
		n1=int(input('enter the number of elements to be added : '))
		#print('aaaa')
		if n1==1:
			n2=int(input('type 1 for integer value     2 for float value : '))
			if n2==1:
				e=int(input('enter integer value : '))
			if n2==2:
				e=float(input('enter the float value : '))
			a.append(e)
			#print(a)
		if n1>1:
			n3=int(input('press 3: for list\n      4: for set : '))
			if n3==3:
				b=[]
				#n4=int(input('enter the number of elements to be added for inner list'))
				for j in range(n1):
					e1=int(input('enter the list element : '))
					b.append(e1)
					print(b)
				a.append(b)
				#print(a)
			if n3==4:
				c=set()
				#n5=int(input('enter the number of elements to be added for inner set'))
				for k in range(n1):
					e2=int(input('enter the set element : '))
					c.add(e2)
					print(c)
				a.append(c)
	print(a)


if __name__=="__main__":
	mlist()

####################################################

# creating dynamic multilist(hetrogenius list) including integer, float, list, set, dictionary

def mlist():
	a=[]
	n=int(input('enter the number of elements for outer list : '))
	for i in range(n):
		n1=int(input('enter the number of elements to be added : '))
		
		# to insert intege or float
		if n1==1:
			n2=int(input('type 1 for integer value     2 for float value : '))
			if n2==1:
				e=int(input('enter integer value : '))
			if n2==2:
				e=float(input('enter the float value : '))
			a.append(e)
		
		# to insert list, set, or dictionary
		if n1>1:
			n3=int(input('Press   3: for list\n\t4: for set\n\t5: for dictionary : '))
			if n3==3:
				b=[]
				#n4=int(input('enter the number of elements to be added for inner list'))
				for j in range(n1):
					e1=int(input('enter the list element : '))
					b.append(e1)
					print(b)
				a.append(b)
				#print(a)
			if n3==4:
				c=set()
				#n5=int(input('enter the number of elements to be added for inner set'))
				for k in range(n1):
					e2=int(input('enter the set element : '))
					c.add(e2)
					print(c)
				a.append(c)
			if n3==5:
				d={}
				for l in range(n1):

					n4=int(input('enter the number of key value pairs for inner dictionary : '))
					key=input('enter the outer dictionary key : ')
					if n4==1:
						value=input('enter the value : ')
						d[key]=value
					if n4>1:
						d1={}
						for m in range(n4):
							key1=input('enter the key : ')
							value1=input('enter the value : ')
							d1[key1]=value1
						d[key]=d1
				a.append(d)
	print(a)


if __name__=="__main__":
	mlist()	

##########################################################
# removes repeated words from sentence

def repeat(s):
	a = []
	b = ' '

	for i in range(len(s)):
		if s[i] != ' ':
			b += s[i]
			# if i == len(s)-1:
			# 	a.append(b)
		if s[i] == ' ':
			a.append(b)
			b = ' '
	for j in range(len(a)):
		if j+1 < len(a):
			if a[j] != a[j+1]:
				print(a[j], end = '')
		else:
			print(a[j])

repeat('hi hi hi i i i am am ram ram')

###############################################
# to sort list elements

# a = [1,4,5,3,2]
def sort(a):
	for i in range(len(a)):
		

		for j in range(i+1, len(a)):

			if a[i] > a[j]:
				temp = a[i]
				a[i] = a[j]
				a[j] = temp
				
			# else:
			# 	j+=1

			# i+=1

	print(a)


a = []	
l = int(input('Enter length of list: '))
for k in range(l):
	e= int(input('Enter a list random number for list: '))

	a.append(e)
	# sort(a) this sorts list element when entered and stores at sorted position
print('Sorted list is: ')
sort(a)

##############################################
# find comman and uncomman elements between two list

def comp_list():
	a = ['a', 'b', 'c']
	b = ['b', 'd']

	com = []
	ucom = []

	for i in range(len(a)):
		for j in range(len(b)):
			if a[i] == b[j]:
				com.append(a[i])
				break
			else:
				ucom.append(a[i])
				break

	print(com)
	print(ucom)
comp_list()

####################################################

def tweet():
	n = int(input('Enter no. of test case: '))
	a = []
	for i in range(n):
		n1 = int(input('Enter no. of input for test case: '))
		b = []
		for j in range(n1):
			tc = input('Enter test input: ')
			b.append(tc)
		b.sort()
		print(b)
		
	m = []
	for k in range(len(b)):
		if k != len(b)-1:
			if b[k] != b[k+1]:
				m.append(b[k])
		else:
			m.append(b[k])
	print(m)
		
	count = []
	c = 0
	for l in range(len(m)):
		for l1 in range(len(b)):
			if m[l] == b[l1]:
				c += 1
		count.append(c)
		c = 0
	print(count)

	e = max(count)
	print(e)

	for p in range(len(count)):
		if e == count[p]:
			print(m[p], count[p])

		# for p in range(len(count)):
		# 	if count[p] > count[p+1]:
		# 		high = count[p]
		# 	else:

tweet()

##############################################
# factorial series using user defined iter and next

class p2:
	def __init__(self,m): # initialize maximum limit for series
		self.max = m

	def __iter__(self): # initialize series from 0
		self.i = 0 # start series from 0, self.i = 1 will start series from 1
		return self

	def __next__(self):
		if self.i <= self.max:
			result = self.fact(self.i)
			self.i += 1
			return result
		raise StopIteration

	def fact(self,n):
		if n <=1:
			return 1
		else:
			return n * self.fact(n-1)

n = int(input('Enter length of factorial series'))
ob = p2(n)
ob1 = p2.__iter__(ob)
for i in range(n):
	print(p2.__next__(ob1))

######################################
# class decoration
import time
def deco(cls):
	time.sleep(2)
	print('control entered into Decorator')
	time.sleep(2)
	print('cls contains',cls)
	time.sleep(2)
	def inner():
		time.sleep(2)
		print('control entered to inner')
		time.sleep(2)
		print('before object creation task is getting executed')
		time.sleep(2)
		obj=cls()
		time.sleep(2)
		print('control came back from',cls)
		time.sleep(2)
		print('after object creation is getting executed')
		return obj
	time.sleep(5)
	print('control is going out of decorator')
	print('address in inner is',inner)
	return inner

@deco
class A:
	pass

obj=A()
print('statements after class decorator')
print('after decorator')