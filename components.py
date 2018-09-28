# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name=name
        self.bio=bio
        self.age=age


class Club():
    
    
    def __init__(self, name, description):
        # your code goes here!
        self.name=name
        self.description=description
        self.members=[]
        self.president=""
        
        


    def assign_president(self, person):
        # your code goes here!
        exist=False
        while exist==False:
            for member in self.members:
                if member.name == person.name:
                    exist=True
                    self.president=person.name
        if exist==False:
            print("President must be a member first")




    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        avage=0.0
        for member in self.members:
            if self.president==member.name:
                print("- %s (%s years old, President) - %s\n" %(member.name, member.age, member.bio ))
                avage+=member.age
            else:
                print("- %s (%s years old) - %s\n" %(member.name, member.age, member.bio ))
                avage+=member.age
        avage=avage/len(self.members)
        print("Average age in this club: %s" %avage)
        print("\n----------------------------------\n")


