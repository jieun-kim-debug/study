import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential, Model
from keras.layers import Input, Dense, Dropout, LSTM
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# diabets 당뇨병. 회귀모델

#1. 데이터
diabets = load_diabetes()
x = diabets.data
y = diabets.target
# print(x[0])         # 10개 컬럼 
# print(y)            # 여러가지 값. 회귀모델
# print(x.shape)      # (442,10)
# print(y.shape)      # (442, )

#1-1. 데이터 전처리
scaler = StandardScaler()
x = scaler.fit_transform(x)
# print(x[0])      

x = x.reshape(-1,5,2)
# print(x.shape)          # (442,5,2)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=99, train_size=0.6)

#2. 모델
input1 = Input(shape=(5,2))
dense1 = LSTM(300)(input1)
dense1 = Dense(7000)(dense1)
dense1 = Dropout(0.3)(dense1)
dense1 = Dense(3000)(dense1)
dense1 = Dense(100)(dense1)
dense1 = Dropout(0.1)(dense1)
output1 = Dense(1)(dense1)

model = Model(inputs=input1, outputs=output1)

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mse'])
early_stop = EarlyStopping(monitor='loss', patience=5, mode='auto')
modelpath = './model/{epoch:02d}-{val_loss:.4f}.hdf5'
checkpoint = ModelCheckpoint(filepath=modelpath, monitor='val_loss', save_best_only=True, mode='auto')
tb_hist = TensorBoard(log_dir='graph', histogram_freq=0, write_graph=True, write_images=True)
hist = model.fit(x_train, y_train, epochs=5000, batch_size=1, validation_split=0.2, callbacks=[early_stop, checkpoint, tb_hist])

#4. 평가, 예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1)
y_pred = model.predict(x_test)

#RMSE 구하기
def RMSE(y_test, y_pred):
    return np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE: ", RMSE(y_test, y_pred))

#R2 구하기
r2 = r2_score(y_test, y_pred)
print("R2: ", r2)

loss = hist.history['loss']
mse = hist.history['mse']
val_loss = hist.history['val_loss']
val_mse = hist.history['val_mse']

#5. 시각화
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(loss, marker='.', c='red', label='loss')
plt.plot(val_loss, marker='.', c='blue', label='val_loss')
plt.title('loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend()

plt.subplot(2,1,2)
plt.plot(mse, marker='.', c='red', label='mse')
plt.plot(val_mse, marker='.', c='blue', label='val_mse')
plt.title('mse')
plt.ylabel('mse')
plt.xlabel('epoch')
plt.legend()

plt.show()

# 튜닝
# epochs=25,batch=1,노드=LSTM300,7000,drop0.3,3000,100,drop0.1
#RMSE:  69.13308050970282
#R2:  0.2085840755892715

# epochs=25,batch=1,노드=LSTM300,4420,drop0.3,3000,1000,drop0.1
#RMSE:  61.93509959704539
#R2:  0.3648056197960856

