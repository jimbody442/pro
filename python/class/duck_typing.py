#c,c++ 프로그램은 실행 전 타입을 검사, 즉 실행 전 타입이 조금이라도 맞지 않으면 실행 자체가 되지 않는다.
# 하지만 파이썬과 같은 스크립트 언어들은 타입에 대해 관대, 타입이 맞지 않더라도 실행되고 ,실행중 문제가 발생하면 그떄 에러를 낸다.

class Duck:
    def Quack(self):

        print("Quaaaaaack!")
    
    def feathers(self):
        print("The duck has white and gray feathers.")

class Person:
    def Quack(self):
        print("The person imitates a duck")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
    def name(self):
        print("John Smith")

def in_the_forest(duck):
    duck.Quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()

#이런 방식의 정의는 명확한 상속의 개념없이 상속을 구현하는 방식.
#클래스 간의 관계가 명확하지 않아서 복잡한 클래스 관계를 가져야 하는 경우에 많은 혼란을 야기
# 동적으로 타입을 체크하게 되므로 타입을 체그하는 코드가 다수 들어가게 되는 것도 문제.

# 덕 타이핑은 파이썬에서 많이 사용 x
#자바스크립트는 기본 함수이기 때문에 클래스를 사용하는 객체지향 프로그램 개념과는 거리가 멀다.
