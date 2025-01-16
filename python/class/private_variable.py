#자바나 c++에는 비공개 변수 메소드 존재.
#이런 속성을 캡슐화라고하고 객체지향 프로그램의 중요한 특징을 다룬다.
# 변수 혹은 메소드의 이름을 지을 때 "_"를 앞에 사용하는 것.
# 예) _private_var 이런 변수나 메소드는 특별한 언급없이 변경될 수 있다,.
#만약 "__" 같이 두 개의 언더바를 사용하면 특수한 비공개 변수로 지정되어서 내부적으로 이름이 변경된다.

class Mapping:
    def __init__(self,iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self,iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        #provides new signature for update()
        #but does not break __init__()
        for item in zip(keys,values):
            self.items_list.append(item)

    #__update라는 변수는 update() 메소드를 복사한 것.
    #복사한 __update는 실재로 실행될때는 _Mapping_update처럼 클래스 이름이 포함된 이름으로 변경.
    #이러한 것을 이름변경(네임 맨글링)이라고하는데 이런 기법은 자식 클래스에서 동일한 이름을 사용할 수 없도록 하는데 목적.

    #__update() 메소드를 __init__에서 사용.
    # 자식클래스에서 update메소드를 재정의한다고 해도 Mapping의 기존 update메소드를 사용 가능.