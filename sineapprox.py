import math as mt
import matplotlib.pyplot as plt
import numpy as np

def poly(value, weights, degree):
	result = 0.0
	vpow = np.vectorize(mt.pow)

	for i in range(degree + 1):
		result = result + weights[i] * vpow(value, degree - i)
	
	return result	

vsin = np.vectorize(mt.sin)
theta = np.linspace(0.0, mt.pi, 180)
sintheta = vsin(theta)
degree = 6
weights = np.polyfit(theta, sintheta, degree)
print(weights)
plt.plot(theta, sintheta, theta, poly(theta, weights, degree), theta, sintheta - poly(theta, weights, degree))
plt.show()
			
