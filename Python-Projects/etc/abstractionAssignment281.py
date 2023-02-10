from abc import ABC, abstractmethod

class Magic(ABC): # class Magic
    def words(self, word): 
        print("Abra-", word)

    # abstract method for letters
    @abstractmethod 
    def letters(self,word):
        pass # pass arguments, which will come next

class MoreMagic(Magic): # child class MoreMagic
    def letters(self,word): # this method will essentially be passed into the abstract method
        print("Did {} work?".format(word))

obj = MoreMagic()
obj.words("ka-da-bra") # will be printed into def words
obj.letters("it") # will be printed into MoreMagic def letters, but gets passed to Magic def letters
