#1. 데이터
import numpy as np
x = np.array([range(1,101), range(311,411), range(100)])
y = np.array(range(711,811))

x = np.transpose(x)
y = np.transpose(y)
print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    # x,y, random_state=99, shuffle=True,
    x,y, train_size=0.6
)       

# print(x_train)
# print(x_val)
# print(x_test)

#2. 모델구성
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

model.add(Dense(5, input_dim = 3))
model.add(Dense(1000))
model.add(Dense(10))
model.add(Dense(9000))
model.add(Dense(1))

#3. 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mse']) 
model.fit(x_train, y_train, epochs=5000, batch_size=1,
            validation_split=0.3)
            # validation_split=0.3 / train_size=60 / 60% X 30% = 18%
            # 즉, train=42%, val=18%의 비율로 훈련됨
           
#4. 평가, 예측
loss, mse = model.evaluate(x_test, y_test)

print("loss : ", loss)
print("mse : ", mse)

y_predict = model.predict(x_test)
print(y_predict)

# RMSE 구하기
from sklearn.metrics import mean_squared_error

def RMSE(y_test, y_predict): 
    return np.sqrt(mean_squared_error(y_test, y_predict)) 
            
print("RMSE : ", RMSE(y_test, y_predict))

#R2 구하기
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict) 
print("R2 : ", r2)

# 조건에 맞게 하이퍼파라미터튜닝
# 1) R2<=0.5
# 2) layer>=5
# 3) node>=10
# 4) epochs>=30
# 5) batch_size<=8

# epochs=30, 히든레이어=5, 노드=500,1000,10,100,9000,1., batch_size=8
#R2 : 0.999994

# epochs=20, 히든레이어=5, 노드=500,1000,10,100,9000,1., batch_size=8
#R2 : 0.997

# epochs=10, 히든레이어=5, 노드=500,1000,10,100,9000,1., batch_size=8
#R2 : 0.90

# epochs=5, 히든레이어=5, 노드=500,1000,10,100,9000,1., batch_size=8
#R2 : -25

# epochs=5, 히든레이어=5, 노드=500,1000,10,100,9000,1., batch_size=8
#R2 : 0.999995

# epochs=30, 히든레이어=5, 노드=500,1000,10,100,30,1., batch_size=8
#R2 : 0.999994

# epochs=30, 히든레이어=5, 노드=(10)x5,1, batch_size=8
#R2 : 0.73(1) / -0.27(2) / 0.99(3)

# epochs=30, 히든레이어=10, 노드=(10)x5,1, batch_size=8
#R2 : 0.98(1) / -3.70(2)
