#파일명  : my_math.py
"""
My Math
======
"""

__all__=['fib']
#모듈 버젼
__version__ =1.0

#원주율
PI =3.1415


def fib(n):
    "피보""나치 수열 생성"
    a,b =0,1

    while b<n:
        yield b
        a,b = b,a+b