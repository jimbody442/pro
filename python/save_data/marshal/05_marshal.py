from pprint import pprint

import marshal

person1 ={
    'name' : 'kimhana',
    'height' : 170,
    'weight' : 60
}

person2 ={
    'name': "Jangyeage",
    'height' : 165,
    'weight' : 55
}

people = [person1,person2]

#데이터를 저장
with open('people.marshal','wb')as f:
    marshal.dump(people,f)

#저장된 데이터를 읽는다.
with open('people.marshal','rb') as f:
    loaded_people = marshal.load(f)

pprint(loaded_people)

#marshal은 다양한 데이터를 저장할 수 있기보다는 일부 데이터를 빠르게 저장하기 위한 것으로 목표로 한다.
#pickle이 지원하는 사용자 객체를 저장하는 기능도 제공하지 않는다.
