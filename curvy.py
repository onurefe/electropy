import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import math as mt

def plotCurve(weights_x, weights_y, weights_z, degree, min_value, max_value, points):
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1, projection='3d')
	
	t = np.linspace(min_value, max_value, points)
	
	xt = poly(t, weights_x, degree)
	yt = poly(t, weights_y, degree)
	zt = poly(t, weights_z, degree)
	ax.scatter(xt, yt, zt, marker='o')
	
	ax.set_xlabel('X axis')
	ax.set_ylabel('Y axis')
	ax.set_zlabel('Z axis')
	plt.show()

def poly(x, weights, degree):
	result = 0.0
	vpow = np.vectorize(mt.pow)
	
	for i in range(degree + 1):
		result = result + weights[i] * vpow(x, i)
	
	return result

