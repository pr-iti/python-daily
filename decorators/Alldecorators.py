
class textile:

    name = 'Wooden'
    
    @staticmethod 
    def __init__(self,name):  #------------- used for simple method change within the class methods-----------------
        self.name = name

    @classmethod
    def Classname(self , name):  # ------------- used for class level  properties -----
        self.name = name

    @property #-------------- to make any attribute dynamic------------
    def percentage(self):
        return  str((self.phy + self.chem + self.math) /3)
    

