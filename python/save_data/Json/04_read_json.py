#json 형식으로 변형된 데이터는 json모듈의 loads혹은 load 를 통해서 다시 불러들인다.
from pprint import pprint
import json

json_data ='''{"height": 170,"name" : "\uae40\ud558\ub098" ,"weight":60}'''
obj = json.loads(json_data) #문자열 데이터에서 로드

print('load from string:',end='')

pprint(obj)

with open('test.json','r') as f:
    obj =json.load(f)

    print('load from file :', end='')
    pprint(obj)


