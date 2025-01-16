# pickle 데이터를 오래 보관할 목적으로 변형.
#주요기능은  파이썬 객체를 직렬화해서 저장하고 다시 역직렬화해서 객체로 만드는 작업.
#pickle.dump(객체, 파일객체)
#pickle.load(파일 객체)
#dump()매개변수로 입력한 객체를 직렬화해서 파일에 저장, load()함수는 다시 복원하는 역할,

from pprint import pprint
import pickle

person1 ={
    'name' : '김하나',
    'height' : 170,
    'weight' : 60
}

person2 ={
    'name' : '이대호',
    'height' : 200,
    'weight' : 80
}

people = list(person1,person2)

#데이터를 저장한다.
with open('people.pickle','wb') as f:
    pickle.dump(people,f)

#저장된 데이터를 읽는다.
with open('people.pickle','rb') as f:
    loaded_people =pickle.load(f)

pprint(loaded_people)