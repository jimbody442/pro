#매개변수.
#객체의 멤버 변수를 변수로서 바로 노출 가능.
#외부에서 변수의 값을 변경 가능, 하지만 만약 멤버 변수의 값이 10~100사이의 int 값이어야한다면
class Rectangle(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def getArea(self):
        return self.width * self.height
    
r1 = Rectangle(10,10)

r1.width = 1000

print("area : {}".format(r1.getArea()))

#중간에서 r1의 width의 값을 1000으로 변경했다.
#하지만 변경된 값이 올바른 범위인지 모른다, 이런 일을 방지하기 위해 함수를 만들어야 한다.
#public_method.py 참고
