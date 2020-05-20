# 자료형
#★가장중요★
# 1.리스트

a = [1,2,3,4,5]
b = [1,2,3, 'a', 'b']
# 리스트 안에는 서로 다른 자료형을 써도 무방
# 반면에 numpy는 딱 한가지 자료형만 써야함
print(b)            #[1,2,3,'a','b']    

print(a[0] + a[3])  #5
# print(b[0] + b[3]) # 타입에러
#보통 데이터는 b처럼 오픈되기 때문에 공부
print(type(a))      #<class 'list'>
print(a[-2])        #4
print(a[1:3])       #[2,3]   #1번째 인덱스부터 3번째 인덱스 '전'까지

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[1])         #2
print(a[-1])        #['a', 'b', 'c']    #리스트 덩어리 취급
print(a[-1][1])     #b      #[-1]==리스트 안에 [1]==1번째 인덱스

#★가장중요★
#1-2. 리스트 슬라이싱
a = [1,2,3,4,5]
print(a[:2])        #[1,2]

#1-3. 리스트 더하기
a = [1,2,3]
b = [4,5,6]
print(a+b)          #[1,2,3,4,5,6]
# 머신의 입장 = 리스트에 리스트를 더해서 더 큰 리스트가 됨
# numpy의 입장 = 사람처럼 계산 / [7,8,9] _하지만 같은 타입만 계산할 수 있음

c = [7,8,9,10]
print(a+c)          #[1,2,3,7,8,9,10]
print(a*3)          #[1,2,3,1,2,3,1,2,3]        #a*3==a+a+a이므로 한 리스트 안에 3번 더해짐

# print(a[2]+ 'hi') # 타입에러
print(str(a[2]) + 'hi') #3hi    # 형변환

f = '5'
# print(a[2]+f) # 타입에러
print(a[2]+int(f))      #8

# 리스트 관련 함수      # 초기화 하지 않는 함수
a = [1,2,3]
a.append(4) #appen=덧붙이다 #리스트 안에 추가
print(a)    #[1,2,3,4]

# ★가장 중요★
# a = a.append(5) # 문법오류 #append는 초기화 X!!!!!!!
# print(a)      #none
a.append(5)
print(a)        [1,2,3,4,5]

a = [1,3,4,2]
a.sort()    #sort도 초기화 X
print(a)    #[1,2,3,4]

a.reverse() #reverse도 초기화 X
print(a)    #[4,3,2,1]

#index도 초기화 X
print(a.index(3))   #1      # ==a[3]
print(a.index(1))   #3      # ==a[1]

#insert도 초기화 X
a.insert(0, 7)      #0번째 인덱스에 7을 삽입
print(a)            #[7,4,3,2,1]

a.insert(3,3)       #3번째 인덱스에 3을 삽입
print(a)            #[7,4,3,3,2,1]

#remove도 초기화 X
a.remove(7)         
print(a)            #[4,3,3,2,1]

a.remove(3)         
print(a)            #[4,3,2,1]