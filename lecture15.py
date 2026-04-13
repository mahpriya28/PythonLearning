#inheritance

#polymorphism
class Shape:
    def area(self):
        print("calculating area..")
        
class Circle(Shape):
    def area(self):
        print("Area of the Circle")

class Square(Shape):
    def area(self, s):
        print("Area of the Square")

shape = [Circle(), Square()]
for s in shape:
    if isinstance(s, Circle):
        s.area()
    elif isinstance(s, Square):
        s.area(4)