import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from collections import Counter
from .metrics import accuracy_socre

#先是类名
class KNNClassifier:

	def __init__(self, k):
		#初始化 knn 分类容器
		assert k>= 1 ,'k must be valid'
		self.k = k
		self.x_train = None
		self.y_train = None

	#根据训练数据集 x_train 和 y_train 训练 kNN 分类器，没有啥具体作用
	def fit(self, x_train, y_train):
		#最后，也可以相应的增加一些判断1.判断 x 与 y 行数 2. 判断 k 要小于样本数
		assert x_train.shape[0] == y_train.shape[0],\
		'the size of x_train must be equal to the size of y_train'
		assert self.k <= x_train.shape[0],\
		'the size of x_train must be at least k.'

		self.x_train = x_train
		self.y_train = y_train
		#return 主要是为了遵守 scikit-learn 的封装规则
		return self

	def predict(self, X_predict):
		#predict 之前必须要先 fit
		assert self.x_train is not None and self.y_train is not None, \
		'must fit before predict!'

		#传进来的列数，必须要和特征集的列数一致 传进来多少个测试样例是无关的
		assert X_predict.shape[1] == self.x_train.shape[1],\
		'the feature number of X_predict must be equal to x_train'

		y_predict = [self._predict(x) for x in X_predict]
		#遵从 scikit-learn 标准，将返回的结果保存到一个数组里
		return np.array(y_predict)


	#定义一个私有函数 只对一个向量进行预测
	def _predict(self, x):
		#先判断单个预测点 x 的合法性
		assert x.shape[0] == self.x_train.shape[1],\
		'the feature number of x must be equal to x_train'

		#实现我们原先欧拉距离的计算和统计
		distances = [sqrt(np.sum((each_x_train - x) ** 2)) for each_x_train in self.x_train]
		nearest = np.argsort(distances)

		topK_y = [self.y_train[i] for i in nearest[:self.k]]
		votes = Counter(topK_y)

		return votes.most_common(1)[0][0]

	def score(self, x_test, y_test):
		y_predict = self.predict(x_test)
		return accuracy_socre(y_test, y_predict)







