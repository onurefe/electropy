import math as mt
import matplotlib.pyplot as plt
import numpy as np

def poly(value, weights, degree):
	result = 0.0
	vpow = np.vectorize(mt.pow)

	for i in range(degree + 1):
		result = result + weights[i] * vpow(value, degree - i)
	
	return result	

vcos = np.vectorize(mt.cos)
theta = np.linspace(0.0, mt.pi, 180)
cosinetheta = vcos(theta)
degree = 6
weights = np.polyfit(theta, cosinetheta, degree)
print(weights)
plt.plot(theta, cosinetheta, theta, poly(theta, weights, degree), theta, cosinetheta - poly(theta, weights, degree))
plt.show()
