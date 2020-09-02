import math

####### This script contain functions to obtain snubber values for half and full bridge drivers.
def leakageCapacitance(cadd, fring0, fring1):
	x = fring0 / fring1
	clk = cadd / (x**2 - 1)
	return clk

def leakageInductance(cadd, fring0, fring1):
	clk = leakageCapacitance(cadd, fring0, fring1)
	llk = 1.0 / (4.0 *clk * (math.pi * fring0)**2)
	return llk

def resistanceSine(fres, c):
	return (1.0 / (2 * math.pi * fres * c))

def resistance(clk, llk, zeta):
	return (1.0 / (2 * zeta * math.sqrt(clk/llk)))
		
def minCapacitance(clk, llk, zeta):
	Rs = resistance(clk, llk, zeta)
	wring = 1.0 / math.sqrt(clk*llk)
	return (1.0 / (wring * Rs))

#fsw: Switching frequency
#cs: Snubber capacity
#df: Dissipation factor(0-1.0) 
#vpp: Peak to peak voltage.
def capacitancePower(fsw, cs, df, vpp):
	return (vpp**2 * fsw * cs *df)
	
def resistorPower(fsw, cs, vpp):
	return (vpp**2 * fsw * cs)

def sinusoidResistorPower(f, r, c, vpp):
	vrms = vpp / (2.0 * math.sqrt(2.0))	
	w = 2 * math.pi * f
	creact = 1.0 / (w * c)
	return (vrms**2 * r / (r**2 + creact**2))
