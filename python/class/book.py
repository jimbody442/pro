class Book(object):
    """책 클래스.
    
    이 클래스는 책 정보를 위한 데이터이다.
    
    """
    

    def __init__(self, title, author):
        """초기화.
        |name| 매개변수를 받아서 객체 멤버 변수 name에 저장
        """
        self.title =title
        self.author = author
        self.borrowed = False

    def borrow(self):
        """책을 대여한다.
        
        책을 대여한다, 멤버 변수 borrowed 변수에
        현재상태를 기록한다.
        """
        self.borrow =True

    def takeBook(self):
        """책을 반납한다
        """

        self.borrow=False

    def printInfo(self):
        log =[]
        log.append("Book:")
        log.append(f"-title : {self.title}")
        log.append("-author :{}".format(self.author))
        log.append("-borrowed : {}".format(self.borrowed))
        print('\n'.join(log))


b1 = Book(title="The Art of Computer Programming", author="도널드 크누스")

b2 = Book(title ="Design Patterns : Elements of Reusable object_oriented Softwear", author ="The 'Gang of Four'")

b1.printInfo()

b2.printInfo()