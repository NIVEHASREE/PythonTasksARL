'''class Gparent:
    def display(self):
        print("Display from gparent class")

class Parent(Gparent):
    def inherited_message(self):
        print("Inherited by child class")

class Child(Parent):
    pass
    
obj=Child()
obj.display()
print(Child.mro())'''

#[<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.Gparent'>, <class 'object'>]

class Gparent:
    def display(self):
        print("Display from gparent class")

class Parent:
    def inherited_message(self):
        print("Inherited by child class")

class Child(Gparent,Parent):
    pass
    
obj=Child()
obj.display()
print(Child.mro())

#[<class '__main__.Child'>, <class '__main__.Gparent'>, <class '__main__.Parent'>, <class 'object'>]