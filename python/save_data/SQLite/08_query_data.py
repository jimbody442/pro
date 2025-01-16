import sqlite3
conn= sqlite3.connect('student.db')
sql='select*from student'
c = conn.cursor()
c.execute(sql)

#하나의 데이터만
print(c.fetchone())

#10개의 데이터를
for s in c.fetchmany(10):
    print(s)

#모든 데이터를 가져온다
for s in c.fetchall():
    print(s)


#데이터를 조회하기 위해서는 Cursor 객체에 fetchone 혹은 fetchmany, fatchall 등을 사용.
#API역할.
#fetchone은 하나씩 데이터를 가져오고,  fetchmany는 일정 개수의 데이터를 리스트로 리턴
#fetchall은 모두가져온다.
