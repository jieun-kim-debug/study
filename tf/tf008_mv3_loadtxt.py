# mv? multi variable

import tensorflow as tf
import numpy as np

#1-1. 그래프 수준의 난수 시드 설정
tf.set_random_seed(777)

#1-2. 데이터(loadtxt) / delimiter : 구분자
dataset = np.loadtxt('./data/csv/data-01-test-score.csv', delimiter=',', dtype=np.float32)
x_data = dataset[:, 0:-1]
y_data = dataset[:, [-1]]

#1-3. feed_dict에 feed 될 텐서를 위한 placeholder 설정
x = tf.placeholder(tf.float32, shape=[None, 3])
y = tf.placeholder(tf.float32, shape=[None, 1])

#2. 모델 구성
# random_normal 정규분포로부터의 난수값 반환
# w, b는 인풋과 아웃풋 값을 기반으로 변경이 되며 인공지능은 바로 w를 예측하는 것이 핵심이기에 변수로 선언하여 구현
# 행렬 곱 연산 : (4,3)*(4,1)==(3,1)
w = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# matmul 행렬연산해주는 함수, 활성화 함수 linear가 h에 포함
h = tf.matmul(x, w) + b

#2-1. cost 손실 함수 정의
cost = tf.reduce_mean(tf.square(h-y))

#2-2. cost를 최소화하는 옵티마이저 정의. minimize(cost)=cost가 가장 적을 때 구하라
opt = tf.train.GradientDescentOptimizer(learning_rate=4e-5)
train = opt.minimize(cost)

#3. 훈련(with문 X)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, h_val, _ = sess.run([cost, h, train], feed_dict={x:x_data, y:y_data})
    if step%10==0:
        print(step, "cost: ", cost_val, "\n 예측값 : \n", h_val)
