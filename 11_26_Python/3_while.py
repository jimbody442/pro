while True:
    print("input your name : ")
    name = input()
    if name != 'jone':
        continue
    print('hello, jone. what is the password?: ')
    
    password = input()
    if password == 'swordfish':
        break
print('Access granted')