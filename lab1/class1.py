class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y 
    def perimeter(self):
        return 2*(self.x+self.y)
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale           
rectangle = Shape(100,45)
print(rectangle.area())
print(rectangle.perimeter())
rectangle.describe("A wide rectangle")
rectangle.scaleSize(0.5)
print(rectangle.area())
