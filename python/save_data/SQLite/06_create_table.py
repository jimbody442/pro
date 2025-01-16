import sqlite3
conn = sqlite3.connect('student.db')
sql='''
 CREATE TABLE student
(
   name txt,
   no integer
   addr text
)
'''
c=conn.cursor() #객체 생성
c.execute(sql)
c.close() 
