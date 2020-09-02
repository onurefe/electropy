import math as mt
import matplotlib.pyplot as plt
import numpy as np

def plotPoly(weights, degree, min, max, steps):
	x = np.linspace(min, max, steps)	
	plt.plot(x, poly(x, weights, degree), label = 'x(t)') 
	plt.plot(x, dpoly(x, weights, degree), label = 'v(t)')
	plt.plot(x, ddpoly(x, weights, degree), label = 'a(t)')
	plt.plot(x, dddpoly(x, weights, degree), label = 'j(t)')
	plt.legend(loc='upper left')
	plt.show()

def dddpoly(x, weights, degree):
	dddweights = []
	for i in range(3, degree + 1):
		dddweights.append(i * (i - 1) * (i - 2) * weights[i])
	
	print(dddweights)
	return poly(x, dddweights, degree-3)

def ddpoly(x, weights, degree):
	ddweights = []
	for i in range(2, degree + 1):
		ddweights.append(i * (i - 1) * weights[i])
	
	return poly(x, ddweights, degree-2)

def dpoly(x, weights, degree):
	dweights = []
	for i in range(1, degree + 1):
		dweights.append(i * weights[i])
	
	return poly(x, dweights, degree-1)

def poly(x, weights, degree):
	result = 0.0
	vpow = np.vectorize(mt.pow)
	
	for i in range(degree + 1):
		result = result + weights[i] * vpow(x, i)
	
	return result

