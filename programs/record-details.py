
s_id=['a01','a02','a03']
s_pwd=['01','02','03']
a_uname='ps'
a_pwd=1234
d={}

def home():
	l=input('want to login as ADMIN or STUDENT')
	if l=='admin':
		a_login()
	elif l=='student':
		s_login()

###############################################################
# Description: this function provides functionalitys to admin,# 
#  it includes login, insert, update and delete the records   #
###############################################################
  
def a_login():
	u_name=input('enter user name')
	u_pwd=int(input('enter passward'))
	if u_name==a_uname:
		if u_pwd==a_pwd:
			print('you have successfully loggedin as ADMIN')
			admin()
	else:
		print('please enter valid user name and passward')
		
#   ask admin what function want to perform
def admin():
	action=input('enter add to add details of students\ndelete to remove record of student\nor press q to exit')
	if action=='add':
		add_s_details()
		cont()
	if action=='delete':
		delete()
		cont()	
	if action=='q':
		print('control is going back to home function')
		home()

		
#   ask admin continue with action		
def cont():
	c=input('Do you want to continue')
	if c=='yes':
		admin()
	elif c=='no':
		print('control is going back to home function ')
		home()


#   to add records of students
def add_s_details():
	n=int(input('How many records you want to add'))
	# d={} defined 
	for i in range(n):
		key=input('enter name of student')
		d1={}
		for j in range(2):
			key1=input('enter field name')
			value1=input('enter value')
			d1[key1]=value1
		d[key]=d1
		print('record added successfully')
		print(d)


#   function to delete records of students	
def delete():
	n=int(input('enter number of records you want to remove'))
	for i in range(n):
		key=input('enter name of the student for which you want to delete the record')
		d.pop(key)
		print('record deleted successfully')
	print(d)


#################################################################
# Description: this function provides functionalitys to student,# 
#  it includes login and view the record                        #
#################################################################

def s_login():
	s_name=input('enter user name')
	s_pass=input('enter passward')
	for i in range(len(s_id)):
		if s_name==s_id[i] and s_pass==s_pwd[i]:
			print('You have successfully loggedin as student')
			student()
		else:
			print('please enter valid id passward')



#   ask student what function to perform
def student():
	action=input('enter disp to display records\n q to exit')
	if action=='disp':
		display()
		s_cont()
	elif action=='q':
		home()
	else:
		print('please enter valid option')


#  function to display records of students
def display():
	key=input('enter name to display the records')
	print(d.get(key))

#   ask admin continue with action	
def s_cont():
	c=input('Do you want to continue')
	if c=='yes':
		student()
	elif c=='no':
		print('control is going back to home function ')
		home()


if __name__=="__main__":
	home()
	