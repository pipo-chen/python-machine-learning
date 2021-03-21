import numpy as np

def accuracy_socre(y_true, y_predict):
	assert y_true.shape[0] == y_predict.shape[0],\
	"the size of must y_true == y_predict"
	return sum (y_true == y_predict) / len(y_true)
	