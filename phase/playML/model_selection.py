import numpy as np

def train_test_split(x, y, test_size = 0.2, seed = None):

	assert x.shape[0] == y.shape[0], \
	"the size of x must == y"
	assert 0.0 <= test_size <= 1.0,\
	"test_size must be valid"
	
	if seed:
		np.random.seed(seed)

	shuffle_indexes = np.random.permutation(len(x))
	test_size = (int)(len(x) * test_size) #有可能是浮点 
	test_indexes = shuffle_indexes[:test_size]
	train_indexes = shuffle_indexes[test_size:]


	x_train = x[train_indexes]
	y_train = y[train_indexes]
	x_test = x[test_indexes]
	y_test = y[test_indexes]

	return x_train, x_test, y_train, y_test