import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
a = np.array(range(1,11))
size = 5               

# LSTM 모델을 완성하시오

def split_x(seq, size):
    aaa=[]
    for i in range(len(seq)-size+1):
        subset = seq[i : (i+size)]
        # seq[0:5] == [1,2,3,4,5]
        # seq[1:6] == [2,3,4,5,6]
        # seq[2:7] == [3,4,5,6,7]
        # seq[3:8] == [4,5,6,7,8]
        # seq[4:9] == [5,6,7,8,9]
        # seq[5:10] == [6,7,8,9,10]
        aaa.append([item for item in subset])
        # aaa = [[1,2,3,4,5]
        #        [2,3,4,5,6]
        #        [3,4,5,6,7]
        #        [4,5,6,7,8]
        #        [5,6,7,8,9]
        #        [6,7,8,9,10]]
    # print(type(aaa))
    return np.array(aaa)

dataset = split_x(a, size)

print(dataset)
print(dataset.shape)
print(type(dataset))        # numpy.ndarray
# 왜? split_x 함수에서 리턴을 np.array로 했기 때문에

x = dataset[:, 0:4]     # [행, 열] = [: all 모든 값, 0:4] 
y = dataset[:, 4]
#  [0][1][2][3][4]
# [[ 1  2  3  4  5]
#  [ 2  3  4  5  6]
#  [ 3  4  5  6  7]
#  [ 4  5  6  7  8]
#  [ 5  6  7  8  9]
#  [ 6  7  8  9 10]]

print(x)
# [[1 2 3 4]
#  [2 3 4 5]
#  [3 4 5 6]
#  [4 5 6 7]
#  [5 6 7 8]
#  [6 7 8 9]]
print(y)
# [ 5  6  7  8  9 10]

x = np.reshape(x, (6,4,1))
# x = x.reshape(6,4,1)과 같은 표현

#2. 모델구성
model = Sequential()
model.add(LSTM(8, input_shape=(4,1)))
model.add(Dense(3))
model.add(Dense(1))
model.add(Dense(3))
model.add(Dense(2))
model.add(Dense(4))
model.add(Dense(2))
model.add(Dense(1))

#3. 실행
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=5, mode='auto')

model.compile(loss = 'mse', optimizer='adam', metrics=['mse'])
model.fit(x,y, epochs=1000, batch_size=1, verbose=1,
         callbacks=[early_stopping])
# model.fit의 batch_size와 x데이터의 batch_size는 다르다
# x데이터의 batch_size는 총 6행으로 자르겠다는 의미이고
# model.fit의 batch_size는 그 6행을 하나씩 자르겠다는 의미
# ex)  1/2/3/4/5
#      2/3/4/5/6
#      3/4/5/6/7
#      4/5/6/7/8
#      5/6/7/8/9
#      6/7/8/9/10

#4. 평가, 예측
loss, mse = model.evaluate(x,y, batch_size=1)
y_predict = model.predict(x)

print('loss: ', loss)
print('mse: ', mse)
print('y_predict: \n', y_predict)
