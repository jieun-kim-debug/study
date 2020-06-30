# 고차함수(map)
# 파이썬에서는 다른 함수를 인수로 취급하는 함수가 있다. 이를 고차함수
# 리스트의 각 요소에 함수를 적용하려면 map()함수 이용

#ex) for문 사용 예시
# a = [1,-2,3,-4,5]
# new = []
# for i in a:
#     new.append(abs(i))
# print(new)  # [1, 2, 3, 4, 5]

#ex) map() 함수 예시
# a = [1,-2,3,-4,5]
# list(map(abs, a))
# map()함수의 사용법
# 반복자 iterator는 여러 요소를 순차적으로 추출하는 기능을 가진 클래스
# map(적용하려는 함수, 배열)
# 리스트에 저장하려면, list(map(적용하려는 함수, 배열))
# for 루프를 사용하는 경우보다 수행 시간을 단축. 방대한 요소를 가진 배열에 함수 적용시키는 경우에 사용

import re

time_list = [
    "2006/11/26_2:40",
    "2009/1/16_23:35",
    "2014/5/4_14:26",
    "2017/8/9_7:5",
    "2020/1/5_22:15"
]

#1. time_list에서 시간만 필요하다.
#2. 리스트 안을 보니 문자열로 구성. 문자열은 [/_:] 기호로 복잡하게 구성됨
#3. 여러 기호로 분할하는 re.split() 함수를 사용하자
#4. re.split()함수를 바로 time_list에 적용할 수 없으니 순차적으로 적용하자
#5. 람다를 이용하여 문자열에서 '시'를 추출하는 함수 작성
hour_sp = lambda x : int(re.split("[/_:]", x)[3])   # 문자열에서 시간을 나타내야 하므로 int 형변환

# 위에서 만든 함수를 이용하여 각 요소에서 '시'만 꺼내 배열로 만드시오
hour = list(map(hour_sp, time_list))       
# list(map(적용할 함수, 배열))
# 여기서 배열은 문자열로 된 리스트 time_list

# print(hour) # [2, 23, 14, 7, 22]
