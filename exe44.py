class Parent (object):
    def override(self):
        print("PARENT override()")
    def implicit(self):
        print("PARENT Implicit()")
    def alterred(self):
        print("PARENT altered()")
class Child(Parent):
    def override(self):
         print("CHILD BEFORE PARENT altered()")
         super(Child,self).alterred()
         print("CHILD,AFTER PARENT altered()")
#initializes objects dad and son and defines them to Parent & Child class respectfully
dad = Parent()
son = Child()
# Calls Parent's implicit() function
dad.implicit()
# Calls Parent's  implicit() function
son.implicit()
#Calls Parent's  override function
dad.override()
#Ovrrides the Parent's overide function
son.override()
#Calls the  Parent's alterred function
dad.alterred()
# Calls the Childs alterred function the calls the parent's alterred function
son.alterred()
