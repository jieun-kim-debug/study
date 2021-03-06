# 설치 프로그램 : SSMS (SQL server) 관계형 데이터베이스

import pymssql as ms
print("잘 접속됐지")

#1. 데이터베이스에 있는 db 연결하기
# localhost==자신의 컴퓨터를 의미
conn = ms.connect(server='localhost', user='bit2', password='1234', database='bitdb')

#1-1. connection 객체로부터 cursor() 메서드를 호출. DB 커서는 Fetch 동작을 관리하는데 사용
cursor = conn.cursor()

#1-2. cursor 실행
# iris의 모든 컬럼을 가져오겠다
# SELECT*FROM== ~로부터 검색하여 가져오겠다
cursor.execute("SELECT*FROM sonar;")

# fetchone() : 한 행을 가져오겠다
row = cursor.fetchone()

while row:
    # print(f"첫컬럼 : %s, 둘컬럼 : %s" %(row[0], row[1]))
    print(f"첫컬럼: {row[0]}, 둘컬럼: {row[1]}, 세컬럼: {row[2]}")
    row = cursor.fetchone()

#2. 커서 끊어주기
# 마지막에 항상 커서를 끊어줘야함
conn.close()
