def hello(name):
    print('Hello'+ name)


hello('Alice')
hello('bob')

#None
#return문이 없는 모든 함수 정의 끝에는 return None이 추가 되어있다.
spam = print("Hello")
print (None == spam)

#print 문 자동 줄바꿈
print("hello world")
print("bob")

print("hello world ", end='')
print("bob")

#sep 키워드 : 구문 문자열을 삽입
print('cat', 'dog', 'mice')
print('cat', 'dog', 'mice', sep = ',')
