name  =['baek','kim','kang','yung','park']

#정렬을 위해서 이름의 길이를 리턴.
def name_length(x):
    return len(x)

#이름 순으로 정렬
name.sort(key = name_length)

name.sort(key = lambda x : len(x))

#lambda a,b : a+b
#lambda x,y : math.sQrt(x**x+y**y)
#lambda x : x % 2 == 0
