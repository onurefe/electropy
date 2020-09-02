import math

def rsnubber(f, c):
	return (1.0 / (2*math.pi*f*c))

def csnubber(f, r):
	return (1.0 / (2*math.pi*f*r))

def ceq(cdecouple, cfilt, csec, lpri, lsec):
	return (1.0 / (1.0 / cdecouple + 1.0 / (cfilt + csec*(lsec/lpri))))
	
def leq(lfilt, lpri, lsec, ldecomp):
	return (1.0 / (1.0/lfilt + lsec/(ldecomp*lpri)))

def fidealfilt(fstart, fend):
	return (((3.0*fstart)**3 * fend)**0.25)

def ffilt(ceq, leq):
	w = (1.0/(ceq*leq))**0.5
	return (w/(2*math.pi))

def lfilt(ffilt, ceq):
	w = 2.0*math.pi*ffilt
	l = 1.0 / (ceq * w**2)
	return l

def cfilt(ffilt, leq):
	w = 2.0*math.pi*ffilt
	c = 1.0 / (leq * w**2)
	return c
