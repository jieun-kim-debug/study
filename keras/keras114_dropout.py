# 112번 파일이 과적합되었다
# 과적합 피하기 2. dropout

import numpy as np
from keras.datasets import cifar10
from keras.utils import np_utils
from keras.models import Sequential, Input, Model
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.regularizers import l1, l2, l1_l2
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
import matplotlib.pyplot as plt

#1. 데이터
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
# print(x_train.shape)        # (50000, 32, 32, 3)
# print(x_test.shape)         # (10000, 32, 32, 3)
# print(y_train.shape)        # (50000, 1)
# print(y_test.shape)         # (10000, 1)

#1-1. 데이터 전처리
# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)
# print(y_train.shape)        # (50000, 100)
# print(y_test.shape)         # (10000, 100)

#2. 모델구성
model = Sequential()

model.add(Conv2D(32, kernel_size=3, padding='same', activation='relu', input_shape=(32,32,3)))
model.add(Conv2D(32, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='same'))
model.add(Dropout(0.2))

model.add(Conv2D(64, kernel_size=3, padding='same', activation='relu'))
model.add(Conv2D(64, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='same'))
model.add(Dropout(0.2))

model.add(Conv2D(128, kernel_size=3, padding='same', activation='relu'))
model.add(Conv2D(128, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='same'))
model.add(Dropout(0.2))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(10, activation='softmax'))

# model.summary()

#3. 컴파일, 훈련
model.compile(optimizer=Adam(1e-4), loss='sparse_categorical_crossentropy', metrics=['acc'])
hist = model.fit(x_train, y_train, epochs=20, batch_size=32, validation_split=0.3)

#4. 평가, 예측
loss, acc = model.evaluate(x_test, y_test, batch_size=32)
# evaluate하면 loss, acc가 출력
print("loss: ", loss)
print("acc: ", acc)

#5. 시각화
loss = hist.history['loss']
acc = hist.history['acc']
val_loss = hist.history['val_loss']
val_acc = hist.history['val_acc']

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(loss, marker='.', c='red', label='loss')
plt.plot(val_loss, marker='.', c='blue', label='val_loss')
plt.grid()
plt.title('loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend()

plt.subplot(2,1,2)
plt.plot(acc, marker='.', c='red', label='acc')
plt.plot(val_acc, marker='.', c='blue', label='val_acc')
plt.grid()
plt.title('acc')
plt.ylabel('acc')
plt.xlabel('epoch')
plt.legend()
plt.show()

# loss:  0.7230174967765808
# acc:  0.7695000171661377
