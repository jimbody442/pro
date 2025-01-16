number =int(input("원하는 구구단 숫자를 입력해주세요 :"))
number_list = []
#chan_num = int(number)
for i in range(1,10,1):
    print(f"{number} * {i} = {number * i}")
    number_list.append(number* i)


print(number_list)