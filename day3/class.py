class Employee:
    def __init__(self,name):
        self.__name=name
e1=Employee("dhanu")
#print(e1.name)   [name mangled] Error: AttributeError: 'Employee' object has no attribute 'name'
print(e1._Employee__name) #accessing mangled name
print(dir(e1))   #shows all attributes of the class of the obj

class Student:
    def __init__(self):
        self._age = 20

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value     
obj = Student()
obj.age = 30
print(obj.age)

#enum
from enum import Enum

class Animal(Enum):
    DOG = 1
    LION =2
print(Animal.DOG.value)
print(Animal(2).name)
print(Animal['DOG'].value)
sounds = {
    Animal.DOG.name: "bark",
    Animal.LION.name: "roar"
}
for i,val in sounds.items():
  print(i,val)
