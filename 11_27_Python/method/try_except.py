def spam(divideBy):
    try:
        return 42/divideBy
    except:
        print('Error : Invalid argument')


print(spam(2))
print(spam(10))
print(spam(0))
print(spam(1))


def spam(divideBy):
    return 42/divideBy

try:
    print(spam(2))
    print(spam(10))
    print(spam(0)) # 아래의 print를 실행하지 않고 except후 종료
    print(spam(1))
except:
    print('Error : Invalid argument')