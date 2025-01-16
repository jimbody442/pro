f = open ('todo.txt','r+')
f.seek(14,0)
f.write('x')
f.close 


#seek(offset,whence)
#seek(이동거리,기준점)을 가진다, 기준점 3가지
# 0 : 파일의 처음 위치
# 1 : 현재 위치
# 2 : 파일의 마지막 위치
