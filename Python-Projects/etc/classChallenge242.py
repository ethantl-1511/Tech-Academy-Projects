# parent
class shape:
    name = "Unknown"
    sides = None

    def info(self):
        msg = "\nShape Name: {}\nShape Sides: {}".format(self.name,self.sides)
        return msg

# child
class triangle(shape):
    name = "Triangle"
    sides = 3

    def pointy(self):
        msg = "\nLooks like an ice-cream cone!"
        return msg

class square(shape):
    name = "Square"
    sides = 4

    def boxy(self):
        msg = "\nCould probably hide in one and sneak."
        return msg


if __name__ == "__main__":
    tri = triangle()
    squ = square()
    print(tri.info())
    print(tri.pointy())
    print(squ.info())
    print(squ.boxy())