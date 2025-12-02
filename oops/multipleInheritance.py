class first:

    welcome ="welcome to class first"

class second:
    greet = "welcome to the class second"

class third(first,second): #---------------- multiple inheritance ------------
     
     def __init__(self):
         print("this is from third class", first.welcome," and" ,second.greet)


t1 = third()

