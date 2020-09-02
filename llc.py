import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

def plotWaveform(swave_freq, l_tank, c_tank, l_mutual, r_series = 0.0, turn_ratio = 1.0, \
r_load = 10000000.0, resolution = 1000, num_of_harmonics = 100, plot_title='Time domain response'):
	swave_period = 1.0 / swave_freq
	t = np.arange(0, 2.0 * swave_period, swave_period / resolution)
	sum_y = 0

	for i in range(0, num_of_harmonics):
		w = 2.0 * (2.0*i + 1) * math.pi * swave_freq 
		coeff = 4.0 / ((2.0*i + 1) * math.pi)
		f_resp = freqResponse(w, l_tank, c_tank, l_mutual, r_series, turn_ratio, r_load)
		__y = coeff * f_resp * math.e**(1j * w * t)
		sum_y += __y

	response = sum_y;
	
	fig, ax = plt.subplots()
	ax.plot(t, response)

	ax.set(xlabel='Time(s)', ylabel='Normalized amplitude',
	       title=plot_title)
	ax.grid()

	fig.savefig("series llc plot-time response.png")
	plt.show()

def plotBodeGain(start_freq, stop_freq, steps, l_tank, c_tank, l_mutual, \
r_series = 0.0, turn_ratio = 1.0, r_load = 10000000.0, plot_title='Bode plot(gain)'):
	# Create frequency range.
	f = np.arange(start_freq, stop_freq, steps)
	w = f * np.pi * 2
	
	# Find out Gain.
	g = abs(freqResponse(w, l_tank, c_tank, l_mutual, r_series, turn_ratio, r_load)) 
	
	fig, ax = plt.subplots()
	ax.plot(f, g)

	ax.set(xlabel='Frequency (Hz)', ylabel='Gain',
	       title=plot_title)
	ax.grid()

	fig.savefig("series llc plot-bode gain.png")
	plt.show()

def plotRectifiedPeak(start_freq, stop_freq, steps, l_tank, c_tank, l_mutual, rectifier_cutoff = 40000.0, \
r_series = 0.0, turn_ratio = 1.0, r_load = 10000000.0, plot_title='Normalized peak rectified value'):
	# Create frequency range.
	f = np.arange(start_freq, stop_freq, steps)
	p = []

	# Find out peak value.
	for __f in f:
		p.append(abs(getRectifiedPeak(__f, l_tank, c_tank, l_mutual, r_series, turn_ratio, \
			r_load, rectifier_cutoff)))
	
	fig, ax = plt.subplots()
	ax.plot(f, p)

	ax.set(xlabel='Frequency (Hz)', ylabel='Rectified peak value',
	       title=plot_title)
	ax.grid()

	fig.savefig("series llc plot-peaks.png")
	plt.show()	

def getRectifiedPeak(swave_freq, l_tank, c_tank, l_mutual, r_series = 0.0, turn_ratio = 1.0, \
r_load = 10000000.0, rectifier_cutoff = 40000.0, resolution = 1000, num_of_harmonics = 100):
	swave_period = 1.0 / swave_freq
	t = np.arange(0, 2.0 * swave_period, swave_period / resolution)
	
	max_y = 0
	sum_y = 0

	for i in range(0, num_of_harmonics):
		f = (2.0*i + 1) * swave_freq
		if f > rectifier_cutoff:
			break
		w = 2.0 * math.pi * f  
		coeff = 4.0 / ((2.0*i + 1) * math.pi)
		f_resp = freqResponse(w, l_tank, c_tank, l_mutual, r_series, turn_ratio, r_load)
		sum_y += coeff * f_resp * math.e**(1j * w * t)
	
	for y in sum_y:
		if (abs(y) > max_y):
			max_y = abs(y)

	return max_y
	

def freqResponse(w, l_tank, c_tank, l_mutual, r_series, turn_ratio, r_load):
	# Find out transformer equivalent impedance.
	transformer_imp = (1j * w * l_mutual * r_load) / (r_load + 1j * turn_ratio**2 * w * l_mutual)
	
	# Calculate total impedance.	
	total_imp = (1j * w * l_tank) + (1.0 / (1j * w * c_tank)) + r_series + transformer_imp
	
	# Find out response.
	g = transformer_imp / total_imp
	
	return g
