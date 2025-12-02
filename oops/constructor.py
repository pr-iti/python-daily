# '''
# __init__()

# '''
# #automatically calls methods after object is created

# class Car:

#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
    

# c1 = Car("audi","red")
# print(c1)
# print(c1.brand)
# print(c1.color)

# # properties of class vs  instance property 
# class Person:
#   species = "Human" # Class property
  
#   # default constructor
#   def __init__(self):
#     pass
  

#   # parameterized constructor 
#   def __init__(self, name):
#     self.name = name # Instance property
  
#   def __str__(self): # use of this 
#      return f"{self.name} and {self.age}"

#   def birthday_age(self):
#      self.age += 1


# p1 = Person("Emil")
# p2 = Person("Tobias")

# #--- add the  new property outside the class
# p1.age = 35
# p2.grade = "A"
# print(p1)

# print("age after the birthday is :-",p1.birthday_age()) # use of methods modifying properties
# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)
# #----------------------------
# print(p1.age)
# print(p2.grade)

class Student:

    marks = []
    
    @staticmethod  # decorator
    def name():
       return  "hello priti"
     
    def __init__(self,name,phy,chem,geo):
      self.name = name
      self.phy = phy
      self.chem = chem 
      self.geo = geo

    def average_marks(self):
       avg =(( int(self.chem)+int(self.phy)+ int(self.geo)) /3).__floor__()
       return avg
    
s1 = Student("priti",89,98,87)
print("this is the average mark :-" ,s1.average_marks())
