#상속
#상속 예) 1년 전 만들었던 클래스에 기능을 더 추가해야한다. 방법은 2가지
# 기존 클래스인  Book 클래스 자체를 수정
#하지만 이미 다른 클래스에 많이 사용되고 있어 Book 클래스를 고치는 것은 위험.
#이런 상환에서 쓸 수 있는 대안이 상속.
#Book 클래스를 상속받아서 새로운 데이터와 메소드를 추가.
from book import Book
class Bookex(Book):
    def __init__(self,title,author,number):
        super().__init__(title,author)    #현재 객체체의 메소드는 self. #부모 클래스를 호출 super().
        self.number = number

    def printInfo(self):
        super().printInfo()
        print(" -number: {}".format(self.number))


b1 = Book(title = "The Art of computer Programming", author ="도널드 칼스")
b2 = Book(title ="Design Patterns : Elements of Reusable object_oriented Softwear", author ="The 'Gang of Four'")

e1 = Bookex(title = "The C Programming Language", author="Dennis Ritchie.Briam kernighan", number =1)

e1.printInfo()

##타입체크#############################
if issubclass(Bookex,Book):
    print("True")
else:
    print("False")
#issubclass()는 Bookex가 Book의 자식클래스인지 확인하는 함수이다.

#type또는 class가 어떤 데이터 타입인지 알기 위해서는 type()함수 또는 isinstance()함수를 쓰는 방법도 있다.
if isinstance(e1.title,):
    print("true")
else:
    print("false")


#isinstance는 어떤 객체의 타입에 대한 것으로 객체와 타입을 비교.

#insubclass는 타입간의 비교

#객체의 타입을 알기 위해서 type()함수로 클래스를 찾고,  이 클래스를 이용해서 issubclass로 비교.
