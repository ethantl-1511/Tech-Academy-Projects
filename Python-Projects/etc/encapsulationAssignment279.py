class Protected: # class Protected
    def __init__(self): 
        self._protectedVar = 0 # protected variable
        self.__privateVar = 12 # private variable
	
    def getProtected(self): # method to print _protectedVar
        print(self._protectedVar)

    def getPrivate(self):  # method to print __privateVar
        print(self.__privateVar)
	
    def setPrivate(self, private): # a workaround to set a new value to __privateVar using a method with another variable
        self.__privateVar = private
		
obj = Protected()
obj.getProtected() # prints 0
obj._protectedVar = 34 # sets _protectedVar to 34
obj.getProtected() # prints 34

obj.getPrivate() # prints 12
obj.setPrivate(23) # sets private to 23, which also sets __privateVar to 23
obj.getPrivate() # prints 23