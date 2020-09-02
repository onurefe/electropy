import math
import numpy
from matplotlib import pyplot as plt 
from math import pi

def collectorGateCoupling(Rg, Lg, Ci, Cr, f):
	w = 2*math.pi*f
	num = math.sqrt(Rg**2 + (w*Lg)**2)*w*Cr
	Ce = Ci+Cr		
	denom = math.sqrt((1.0 - Lg*Ce*w**2)**2 + (Rg*Ce*w)**2)
	return (num/denom) 

def graphGateCoupling(Rg, Lg, Ci, Cr, fstart = 2e5, fstop = 3e7, steps = 1000):
	freqs = numpy.arange(fstart, fstop, (fstop - fstart)/steps)
	coupling = []
	for f in freqs:
		coupling.append(collectorGateCoupling(Rg, Lg, Ci, Cr, f))
	
	print("Max coupling is:")
	print(max(coupling))
	print('\n')
	plt.plot(freqs, coupling)
	plt.show()
	
