import math
import matplotlib.pyplot as plt

def sine_graph(harmonic_count, points):
	A = []
	
	if harmonic_count < 1:
		harmonic_count = 1

	for k in range(0, points):
		sum = 0.0
		for h in range(0, harmonic_count):
			sum += math.sin((h + 1) * k * 2.0 * math.pi / points)

		A.append(sum)
	
	plt.plot(A)
	plt.show()

def cosine_graph(harmonic_count, points):
	A = []
	
	if harmonic_count < 1:
		harmonic_count = 1

	for k in range(0, points):
		sum = 0.0
		for h in range(0, harmonic_count):
			sum += math.cos((h + 1) * k * 2.0 * math.pi / points)

		A.append(sum)
	
	plt.plot(A)
	plt.show()
