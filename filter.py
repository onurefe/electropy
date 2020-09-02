import math
from math import atan
from math import pi

def rcPhase(r,c,f):
	return (-atan(2*pi*f*r*c) * (180.0/pi))

def cutOff(r,c):
	return (1.0 / (2*pi*r*c))
	
