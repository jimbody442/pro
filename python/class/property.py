class Rectangle(object):
    def __init__(self,w,h):
        self._width = w
        self._height = h
    
    def getArea(self):
        return self._width * self._height
    
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,w):
        self._width = max(10,min(100,self._width))

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,h):
        self._height = max(10,min(100,self._height))
    

r1 = Rectangle(10,10)
    
r1.width =100
print("Rectangle({},{})".format(r1.width,r1.height))
print(r1.width)
print(r1.height)
print("area: {}".format(r1.getArea()))