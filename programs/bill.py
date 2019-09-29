# generates bill for restaurent

class rest:
	def menu():
		print("-----Menu-----")
		print("Dosa")
		print("Idli")
		print("Puri")
		print("Vada")
		

	def choice():
		print("enter 1 for next order  2: for bill")
		option=int(input("enter your option"))

		if option==1:
			print("please choose again")
			rest.disp()
		elif option--2:
			print("thank you for comming")
			rest.bill()

	def disp():
		dosa = 20
		idli = 10
		vada = 30
		rest.menu()

		item=input("Enter item name: ")
		n=int(input("Enter quantiiy"))

		if item=="dosa":
			price=n*dosa
			print(price)
			rest.choice()
		elif item=="idli":
			price=n*idli
			print(price)
			rest.choice()
		elif item=="vada":
			price=n*vada
			print(price)
			rest.choice()

	def bill():
		total=0
		total=total

oa=rest()
oa.choice()











