class Point:
    # your code here
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Point({}, {})'.format(self.x, self.y)
        #return 'A point at ({}, {})'.format(self.x, self.y)
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)
    def __add__(self,other):
        if isinstance(other,Point):
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Point(x,y)
    def __radd__(self,other):
        x = self.x + other
        y = self.y + other
        return Point(x,y)
    def __mul__(self,other):
        if isinstance(other, Point):
            num1 = self.x*other.x + self.y*other.y
            return num1
        else:
            x = self.x * other
            y = self.y * other
            return Point(x,y)
    def __rmul__(self,other):
        x = self.x * other
        y = self.y * other
        return Point(x,y)
        
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
    def __str__(self):
        #return '{} x {} Square'.format(self.line,self.line)
        return 'Square({})'.format(self.line)
    def __repr__(self):
        return 'Square({})'.format(self.line)
    def __iadd__(self,other):
        if isinstance(other, Square):
            self.line = self.line + other.line
            return self
        else:
            self.line = self.line + other
            return self
    def __isub__(self,other):
        if isinstance(other, Square):
            self.line = self.line - other.line
            return self
        else:
            self.line = self.line - other
            return self
    def perimeter(self):
        return 4*self.line
    def area(self):
        return self.line * self.line

class Circle:
    def __init__(self,r=0):
        self.__radius = r
    def __str__(self):
        #return 'A circle with a radius of {}cm'.format(self.__radius)
        return 'Circle({})'.format(self.__radius)
    def __repr__(self):
        return 'Circle({})'.format(self.__radius)
    def __add__(self,other):
        if isinstance(other, Circle):
            r = self.__radius + other.__radius
            return Circle(r)
        else:
            r = self.__radius + other
            return Circle(r)
    def __radd__(self,other):
        r = self.__radius + other
        return Circle(r)
    def __mul__(self,other):
        if isinstance(other, Circle):
            r = self.__radius * other.__radius
            return Circle(r)
        else:
            r = self.__radius * other
            return Circle(r)
    def __rmul__(self,other):
        r = self.__radius * other
        return Circle(r)
    def radius(self):
        return self.__radius
    def diameter(self):
        return 2*self.__radius
