import math
class Cylinder:
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height

    def get_height(self):
        return self.height

    def get_radius(self): 
        return self.radius    
    
    def set_radius(self,radius):
        self.radius = radius
    
  
    def set_height(self,height):
        self.height = height
    

    def get_area(self):
        base_area = self.calculate_base_area()
        surface_area = self.calculate_surface_area()
        area = 2 * base_area + surface_area
        return  area


    def calculate_base_area(self):
        return math.pi * self.radius ** 2


    def calculate_surface_area(self):
        return 2 * math.pi * self.height  * self.radius

    def calculate_volume(self):
        return self.calculate_base_area() * self.height

c = Cylinder(3,5)
print(c.get_area())
print(c.calculate_volume())                  
                   