import numpy as np

class StandardScaler:
	def __init__(self):
		self.mean_ = None
		self.scale_ = None


	def fit(self, X):
		#目前只处理 2 维
		assert X.ndim == 2,'the dim of X must == 2'
		self.mean_ = np.array([np.mean(X[:,i]) for i in range(X.shape[1])])
		self.scale_ = np.array([np.std(X[:,i]) for i in range(X.shape[1])])
		
		return self

	def transform(self, X):
		assert X.ndim == 2,'the dim of X must == 2'
		assert self.mean_ is not None and self.scale_ is not None,\
		"must fit"
		assert X.shape[1] == len(self.mean_),\
		"the feature number of X must == mean_ and std_"

		resX = np.empty(shape = X.shape, dtype = float)

		#归一化每一列
		for col in range(X.shape[1]):
			resX[:,col] = (X[:,col] - self..mean_[col] / self.scale_[col])

		return resX





