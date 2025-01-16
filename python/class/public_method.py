class Rectangle(object):
    def __init__(self,w,h):
        self.width = w
        self.height = h

    def getArea(self):
        return self.width * self.height
    
    def setWidth(self, w):
        self.width = max(10,min(100,self.width)) 
        if max == True:
            print("변경되었습니다.")
        else:
            print("값이 커서 변경이 불가합니다.")


r1 = Rectangle(10,10)
r1.setWidth(1000)
print("area : {}".format(r1.getArea()))


#코드의 setWidth() 메소드는 가로의 길이의 범위를 10~100까지로 제한하고 있다.
# 이 방법은 좋긴는 하지만 뭔가 사용 방법에 대해서 있어서 불편하다.
# 기존 변수에값을 설정하듯, 사용하면서 데이터를 검증하는 그런 의도로 만들어진 것이 "property"

#property.py 참고.