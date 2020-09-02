def maxPulse(l, vcc, isat):
	return (isat * l / vcc)

def maxN(vcc, l, c, vsat, pulseWidth):
	Epulse = 0.5 * l * ((vcc / l) * pulseWidth)**2
	Esat = 0.5 * c * vsat**2
	return (round((Esat / Epulse) - 0.5))

def inductance(vcc, c, n, pulseWidth, cvoltage):
	Ecap = 0.5 * c * cvoltage**2
	Epulse = Ecap / n
	return (((vcc * pulseWidth)**2) / (2 * Epulse))
