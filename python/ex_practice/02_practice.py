a ,b =0,1

value_a =[a+b,]

for i in range(1,20,1):
    c=a+b
    value_a.append(c)
    a=b
    b=c

print(value_a)