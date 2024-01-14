## Animals is-a object (yes,sort of confusing) look st thr extra credit
#class Animal (object):
#    def __init__(self,name):
#        self.name = name
#    def add_name(cls,Name2):
#        name2 = cls.name +" "+ str(input("what is your second name? >>"))
#        print(f"Okay {name2} welcom to kcb Bank Kenya")

## class dog is_a Animal
#class Dog(Animal):
#    def __init__ (self,name):
        ##dog has a name
#        self.name = name

## Cat is an Animal
#class Cat (Animal):
#    def __init__(self,name):
        ## cat has a name
#        self.name = name

#    def change_name(cils,Name):
#        Cname = cils.name.capitalize()
#        split_name =  list(Cname)
#        print(Cname)
#        print(f"The first letter in your cats name is {split_name[0]}")






## Person is_a object

#class Person(object):

#    def __init__(self,name):
        ##Person has a name
#        self.name = name
        ## Person has-a pet of some kind
#        self.pet = Cat("satan").__init__(name)

#    def print_name(cls,name):
#        Name = cls.name
#        print(Name)

## Employee is_a person
#class Employee (Person):
#    def __init__(self,name,salary):
        ## employee has a name and salary hmm what is this strange magic ???
#        super(Employee,self).__init__(name)
        ## Employee has - a salary
#        self.salary = salary
        ##frank has a cat named satan


## Fish is an object
class Fish(object):
    def __init__(self,name):
        self.name = name
        print(f"Hellow my name is {name}")


class distace_swam(Fish):

    name = int(input("> What is your name ? "))
    print(f"Hellow {name} so you want flipper to swim {distance} meters)

    def __init__ (self,distance,):
            self.distance = distance
            pass

    print(f"Hellow {name} so you want flipper to swim {distance} meters ?")

    def swim(cls,distance2):
        cls.distance2 = distance2

            if 0 <= cls.distance2 <= 10 :
                print (f"""
                \tFlipper is not a baby fish man
                \tHe can swim more than {cls.distance2} meters""")

            elif 10 <= cls.distance2 <= 50 :

                 if cls.distance2 % 2 == 0 :
                     print ("flipper stepped on a land mine he's dead ")

                 else : print("flipper is tired he wants a well desserved rest !!!! ")

            else :
                 print(f"flipper just swam {cls.distance2} meters ,get him something to eat now man ")



    ## salmon is a FIsh
#class Salmon(Fish):
 #  def __init__():

## Halibut is a Fish

#class Halibut(Fish):
#    pass

#over is a Dog
#rover = Dog("rover")

 ## satan is a Cat
#satan = Cat("satan")
#satan.add_name("satan")

## mary is a Person
#mary = Person("Mary")
#print(mary.pet)


 ##frank is an employee with asalary of 120000
#frank.print_name("frank")


 ## frank has a Dog named rover
#frank.pet = rover

#flipper is afish
flipper = Fish("flipper")
flippers_swam = distace_swam(50)




 ##crouse is a Salmon
#cruose = Salmon()

 ## harrry is_a Halibut
#harry = Halibut()
