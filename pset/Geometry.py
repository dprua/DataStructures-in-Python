
class Point:
    # your code here
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def halfway(self,point):
        a = (point.x + self.x) / 2
        b = (point.y + self.y) / 2
        return Point(a,b)
    def midpoint(a,b):
        return Point((a.x+b.x)/2,(a.y+b.y)/2)
    def reflect_x(self):
        return Point(self.x,-self.y)
    def slope_to_origin(self):
        dx = self.x - 0.0
        dy = self.y - 0.0
        return dy/dx
    pass

class Square:
    def __init__(self,line):
        self.line = line
    def perimeter(self):
        return 4*self.line
    def area(self):
        return self.line * self.line

class Circle:
    def __init__(self,r=0):
        self.r = r
    def radius(self):
        return self.r
    def diameter(self):
        return 2*self.r
