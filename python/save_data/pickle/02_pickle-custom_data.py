import pickle

class Book:
    """책 정보들을 파일이 저장하는 클래스"""

    def __init__(self,category):
        self.category = category
        self.books =[]

    def addBook(self, book_title):
        if book_title not in self.books:
            self.books.append(book_title)

    def getBook(self):
        state = self.__dict____.copy()
        #여기서 필요없는 데이터 삭제 가능.
        return state
    
    def __setstatus__(self,state):
        self.__dict__.update(state)

if __name__ =='main':
    #Book객체를 만든다.
    book = Book('mybook')
    book.addBook('book1')
    book.addBook('book2')
    print(book.getBooks())

    #객체를 바이너리 데이터로만들고
    pickled_data = pickle.dumps(book)

    #다시 객체화
    new_book = pickle.loads(pickled_data)

    #기존 데이터와 동일한 데이터의 객체
    print(book.getBook())