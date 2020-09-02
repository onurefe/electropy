import math
import cmath
import numpy
import matplotlib.pyplot as plt
from math import pi
from math import sqrt
from numpy import arange

# Circuit model: Cp // (Rs+Ls+Cs)
def getImpedance(f, Cp, Rs, Ls, Cs):
	w = 2*pi*f
	num = w*Rs*Cs + 1j * (Ls*Cs*w**2 - 1)
	denom = 1j*Rs*Cs*Cp*w**2 - w*Cp*(Ls*Cs*w**2 - 1) + w*Cs
	return (num/denom)

def getRlcParams(fres, impres, Q, Cp):
	wr = 2 * pi * fres
	rs = sqrt(1.0 / ((1.0/impres)**2 - (wr*Cp)**2))
	cs = 1.0 / (Q*rs*wr)
	ls = 1.0 / (cs*wr**2)
	ret = {'Rs':rs, 'Ls':ls, 'Cs':cs}
	return ret

def bodePlot(fstart, fstop, Cp, Rs, Ls, Cs, steps = 1000):
	imps = []
	phases = []
	freqs = arange(fstart, fstop, (fstop - fstart)/steps)
	for f in freqs:
		imps.append(abs(getImpedance(f, Cp, Rs, Ls, Cs)))
		phases.append(cmath.phase(getImpedance(f, Cp, Rs, Ls, Cs)))		
	
	plt.subplot(2, 1, 1)
	plt.plot(freqs, imps)
	plt.title('')
	plt.ylabel('Impedance')

	plt.subplot(2, 1, 2)
	plt.plot(freqs, phases)
	plt.xlabel('Frequency (1/s)')
	plt.ylabel('Phase')

	plt.show()
