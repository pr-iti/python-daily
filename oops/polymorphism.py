# class birds:

#     def sound(self):
#         print("birds sounds like 'chirp', 'chirp' ")

# class crow(birds): #------ inheritance
#     def sound(self):
#       print("crow sounds'caw' , 'caw' ")
    

# parrot = birds()
# bird1 = crow()

# parrot.sound()
# bird1.sound()

# class circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def Area(self):
#         totalArea = (3.14*self.radius*self.radius)
#         print(f" Area of circle with radius {self.radius} is :{totalArea}")
    
#     def Perimeter(self):
#         totalperim = (2* self.radius*3.14).__floor__()
#         print(f"perimeter of circle with radius {self.radius} is :{totalperim}")

# c1 = circle(5)
# c1.Area()
# c1.Perimeter()


# class Employee:

#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
    
#     def print(self):
#         print(f"employee is in role ,{self.role}  working with department ,{self.dept} and having salary Rs. {self.salary}Pm.")

# class Engineer(Employee):

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT", 100000)


#     def show_details(self):
#         print(f"you are {self.name} and your age is {self.age} ")



# e1 = Engineer("Priti" ,20)
# e1.show_details()
# e1.print()

#----------------------------- dendur function -----------------------------------
class Order:
    def __init__(self,orderitem,price):
        self.orderitem = orderitem
        self.price = price

    def __gt__(self,order2): # dendur functions 
        return (self.price > order2.price)
    
o1 = Order("chips",40)

o2 = Order("pizza",80)
print(o1 < o2) #true