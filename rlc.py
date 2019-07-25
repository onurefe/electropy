import math

def printCompensationCapacitorArray(currentRating, safetyFactor, inductance, startFreq, stopFreq, steps):
	R = stopFreq / startFreq
	
	for i in range(0, steps):
		__max_freq = startFreq + startFreq * math.pow(R, (i-1.0) / steps)
		__nominal_freq = startFreq * math.pow(R, 1.0 / (2.0*steps)) * math.pow(R, i / (1.0 * steps))
		__capacity = getLCCapacity(inductance, __nominal_freq)	
		__voltage = getCapacitiveReactance(__capacity, __max_freq) * currentRating
		
		user_msg = "{}.th capacitor needed to be: {}uF {}Volts"
		print(user_msg.format(i+1, __capacity * 10**6, __voltage))	
	 
def getLCCapacity(inductance, freq):
	return (1.0 / (4.0 * (math.pi * freq)**2.0 * inductance))  			

def getLCInductance(capacity, freq):
	return (1.0 / (4.0 * (math.pi * freq)**2.0 * capacity))

def getLCFrequency(capacity, inductance):
	return (1.0 / (2.0 * math.pi * math.sqrt(capacity * inductance)))

def getRCTime(resistance, capacitance):
	return (resistance * capacitance)

def getRCFrequency(resistance, capacitance):
	return (1.0 / (2.0 * math.pi * resistance * capacitance))

def getCapacitiveReactance(capacity, freq):
	return (1.0 / (2.0 * math.pi * capacity * freq))

def getInductiveReactance(inductance, freq):
	return (2.0 * math.pi * inductance * freq)

def getCapacitorVoltage(capacity, energy):
	return (math.sqrt(2.0 * energy / capacity))
