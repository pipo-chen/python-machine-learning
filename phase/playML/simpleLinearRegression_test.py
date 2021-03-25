import numpy as np

class SimpleLinearRegression:

	def __init__(self):
		self.a_ = None
		self.b_ = None

	def fit(self, x_train, y_train):
		#因为我们目前做的是一个特征的情况，所以判断维度 1 维
		assert x_train.ndim == 1,\
		"simple linear regressor can only solve simgle feature"
		assert len(x_train) == len(y_train),\
		"the size of x_train must == y_train"

		x_mean = np.mean(x_train)
		y_mean = np.mean(y_train)

		m = (x_train - x_mean).dot(y_train - y_mean)
		d = (x_train - x_mean).dot(x_train - x_mean)
		
		self.a_ = m / d
		self.b_ = y_mean - self.a_ * x_mean

		return self

	def predict(self, x_predict):
		#可以预测多个值的话，x_predict 传进来的应该是个向量数据集
		#先确保是个一维数组
		assert x_predict.ndim == 1,\
		"simple linear regressor can only solve simgle feature"
		assert self.a_ is not None and self.b_ is not None,\
		"must fit before predict"

		return np.array([self._predict(x) for x in x_predict])

	#完成单个预测
	def _predict(self, x_single):
		return self.a_ * x_single + self.b_

