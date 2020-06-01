import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Dropout
from keras.datasets import mnist
from keras.callbacks import EarlyStopping
# mnist 손글씨로 된 7만장의 데이터

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(x_train[0])
# print("y_train: ", y_train[0])

# print(x_train.shape)        # (60000, 28, 28)
# print(x_test.shape)         # (10000, 28, 28)
# print(y_train.shape)        # (60000,)
# print(y_test.shape)         # (10000,)

# plt.imshow(x_train[0], 'gray')
# plt.imshow(x_train[0])    # 랜덤색깔
# print(x_train[0].shape)
# plt.imshow(가로, 세로)==가로, 세로를 넣어주면 이미지를 출력
# plt.show()

# 0~9까지(손글씨 숫자) 10개로 분류
# 분류모델로 쓰려면 one-hot 인코딩을 사용해서 2차원으로 변환

# 데이터 전처리 1. one-hot 인코딩
from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
# print(y_train.shape)        # (60000, 10)

# 데이터 전처리 2. 정규화
x_train = x_train.reshape(60000,28,28,1).astype('float32')/255
x_test = x_test.reshape(10000,28,28,1).astype('float32')/255

from keras.models import load_model
model = load_model('./model/model_test01.h5')
model.add(Dense(40, name='new1'))
model.add(Dense(30, name='new2'))
model.add(Dense(10, name='new3', activation='softmax'))

model.summary()

# 85번 save 모델 load한 후 레이어 3개 추가한 결과값
# loss:  2.370083384513855
# acc:  0.011300000362098217

#4. 평가, 예측
loss, acc = model.evaluate(x_test, y_test, batch_size=100)

print("loss: ", loss)
print("acc: ", acc)

'''
loss = hist.history['loss']
val_loss = hist.history['val_loss']
acc = hist.history['acc']
val_acc = hist.history['val_acc']

# print('acc: \n', acc)
# print('val_acc: \n', val_acc)
# print('loss_acc: \n', loss_acc)

### 시각화
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))          # 가로 10인치, 세로 6인치
# subplot(2,1,1)==2행 1열의 첫번째 그림
plt.subplot(2, 1, 1)                
plt.plot(hist.history['loss'], marker='.', c='red', label='loss')
plt.plot(hist.history['val_loss'], marker='.', c='blue', label='val_loss')
# plt.plot(hist.history['acc'])
# plt.plot(hist.history['val_acc'])
plt.grid()                                # 모눈종이처럼 보이게
plt.title('loss')
plt.ylabel('loss')
plt.xlabel('epoch')
# plt.legend(['loss', 'val loss'])        # legend==엑셀의 범주(?)와 비슷
plt.legend(loc='upper right')             # loc=location / 명시 안해주면 빈 자리에 자동으로 표시
plt.show()

# subplot(2,1,2)==2행 1열의 2번째 그림
plt.subplot(2, 1, 2)                    
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
# plt.plot(hist.history['acc'])
# plt.plot(hist.history['val_acc'])
plt.grid()                              # 모눈종이처럼 보이게
plt.title('acc')
plt.ylabel('acc')
plt.xlabel('epoch')
plt.legend(['loss', 'val acc'])        # legend==엑셀의 범주(?)와 비슷
plt.show()
'''
