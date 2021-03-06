# csv 파일 저장 경로를 알고싶으면? print(해당 data)
# iris.csv 파일에 필요없는 헤더가 있으므로 제거해주자
import numpy as np
import pandas as pd

datasets = pd.read_csv("./data/csv/iris.csv", index_col=None, header=0, sep=',')
# header = 150,4,setosa,versicolor,virginica
# index_col=None 읽기 전 파일에 index_col에 데이터가 껴있었다. 그래서 None
# header=0을 하면 첫 헤더(행)는 실 데이터로 인식 X
print(datasets.head())      # 위에서부터 5개
#    150    4  setosa  versicolor  virginica
# 0  5.1  3.5     1.4         0.2          0
# 1  4.9  3.0     1.4         0.2          0
# 2  4.7  3.2     1.3         0.2          0
# 3  4.6  3.1     1.5         0.2          0
# 4  5.0  3.6     1.4         0.2          0

# print(datasets.tail())      # 아래서부터 5개

print("======================")
print(datasets.values)      # ★항상 쓰임. 머신을 돌리기 위해서 np로 변환

aaa = datasets.values
print(type(aaa))            # <class 'numpy.ndarray'>

# np로 저장하시오
from sklearn.datasets import load_iris
iris = load_iris()
np.save('./data/iris.npy', arr=iris)
