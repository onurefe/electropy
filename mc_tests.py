import math as mh

def getDistance(j, Vi, Ts, Tf):
	a = (j / 12.0) * (Ts * Ts * Ts - Tf * Tf * Tf)
	b = Vi * (Ts + Tf)
	c = (j / 6.0) * Ts * Ts * Tf

	return (a+b+c)

def exitSpeed(j, Vi, Ts, Tf):
	return (Vi + (j / 6.0) * (Ts * Ts - Tf * Tf))
