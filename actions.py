# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Khalid"
my_age = 23
my_bio = "Passionate for electronics"
myself = Person(my_name, my_bio, my_age)

def introduction():
	print("Hello, %s. Welcome to our portal." % my_name)
	options()

def options():
	# your code goes here!
	print("\nWould you like to:\n1) Create a new club.\nor:\n2) Browse and join clubs.\nor:\n3) View existing clubs.\nor:\n4) Display members of club.\nor:\n-1) Close application.")
	option=input()
	if option == "1":
		create_club()
	elif option == "2":
		join_clubs()
	elif option == "3":
		view_clubs()
		options()
	elif option == "4":
		view_club_members()
	elif option=="-1":
		exit()
	else:
		print("Invalid Input")
		options()

def create_club():
	# your code goes here!
	name=input("Pick a name for your awesome new club: ")
	description=input("What is your club about?\n")
	name=Club(name,description)
	clubs.append(name)
	print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop):")
	print("-----------------------------------")
	counter=1
	enroll=False
	for member in population:
		print("[%s] %s" %(counter,member.name))
		counter+=1
	while True:
		try:
			rec=int(input())
			if rec!=int(-1) and rec<=len(population):
				for member in name.members:
					if population[rec-1] == member:
						print("Member already enrolled in club")
						enroll=True
				if enroll==False:
					name.recruit_member(population[rec-1])
			elif rec==int(-1):
				name.recruit_member(myself)
				name.assign_president(myself)
				print("Here's your club: \n%s\n%s\nMembers:" %(name.name,name.description))
				name.print_member_list()
				break
		except:
			print("You must input a number within range")
	options()

		
	


	

def view_clubs():
	# your code goes here!
	for club in clubs:
		print("\nNAME: %s\nDESCRIPTION: %s\nMEMBERS: %s" %(club.name,club.description,len(club.members)))
	print("\n----------------------------------\n")
	

def view_club_members():
	# your code goes here!
	view_clubs()
	exist=False
	choice=input("\nEnter the name of the club whose members you'd like to see: ")
	for club in clubs:
		if club.name.lower()==choice.lower():
			club.print_member_list()
			exist=True
			break
	if exist==False:
		print("Club name invalid please make sure you type is correctly")
	options()

	

def join_clubs():
	# your code goes here!
	view_clubs()
	exist=False
	enroll=False
	choice=input("\nEnter the name of the club you'd like to join: ")
	for club in clubs:
		if club.name.lower()==choice.lower():
			for member in club.members:
				if my_name == member.name:
					print("You are already enrolled in this club")
					enroll=True
					exist=True
			if enroll== False:
				club.recruit_member(myself)
				print("%s just joined %s" %(myself.name,club.name))
				exist=True
				break
	if exist==False:
		print("Club name invalid please make sure you type is correctly")
	options()


def application():
	introduction()
	# your code goes here!
	
