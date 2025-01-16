def add(*args):
    total =0
    for i in args:
        total +=i
    return total

vals =[1,2]     #리스트로 만들어진 데이터
add(*vals)      # 3,add(1,2)

vals =(1,2,3,4,5,6,7,8,9,10) # 튜플로 만들어진 데이터
add(*vals)


def print_argsa(**kws):
    print(kws)

vals = { 'p3': '3', 'p1': '1', 'p2': '2'}
print_argsa(**vals)