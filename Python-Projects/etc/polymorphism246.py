# parent
class dice:
    name = "Unknown" # Attribute
    sides = None

    def info(self): # Info Method
        print("\nShape Name: {}\nShape Sides: {}".format(self.name,self.sides))
        return

# child class 1
class d4(dice): 
    name = "D4"
    sides = 4
    otherName = "Prism" # New d4 attribute

    # Changed method, added more to print
    def info(self):
        print("\nShape Name: {}\nShape Sides: {}\nOther name: {}".format(self.name,self.sides,self.otherName))
        return 

# child class 2
class circle(dice):
    name = "Circle"
    radius = 3.14
    isDie = False

    def info(self):
        print("\nShape Name: {}\nShape Radius: {}\nIs a circle a die? {}".format(self.name,self.radius, self.isDie))
        return

# invoking methods
is_dice = dice()
is_dice.info()

is_also_dice = d4()
is_also_dice.info()

is_not_dice = circle()
is_not_dice.info()