# class Car:

#     def start(self):
#         self.clutch = True # hides the data and shows the only essential ones
#         self. accelerator = True
#         print("car started")
    
#     def stop(self):

#         self.breakGear = True
#         self.stopEngine = True
#         print("car Stopped ")


# c1 = Car()

# c1.start()
# c1.stop()

# class Account:
    
#     def __init__(self,balance,account):
#         self.account = account
#         self.balance = balance


#     def Debit(self,amount):
#         self.balance -= amount
#         print("after debit" ,self.balance)

#     def credit(self,amount):
#         self.balance += amount
#         print("after credit" ,self.balance)
    
#     def NetBalance(self):
       
#         print("total balance" ,self.balance)

# user1 = Account(100000,"saving")

# user1.Debit(50)
# user1.credit(500)
# user1.NetBalance()
# user1.Debit(40)
# user1.credit(590)
# user1.NetBalance()
# # -------------------------------
# print('\n',"for user2-------- ")

# user2 = Account(100000,"saving")

# user2.Debit(500)
# user2.credit(5000)
# user2.NetBalance()


class greet:
     
    __name =" "   # make attributes private by aading double underscore(__) before the variable name

    def __hello(self,name):    #methods private by aading (__) before the method name
        self.name  = name 
        print("hello !!", self.name)

    def welcome(self,name):
        self.__hello(name) 

greet1 =greet()
greet1.welcome("priti")
greet1.__hello("radhika") # results error 