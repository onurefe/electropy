import math

def fourierSum(iteration):
	__sum = 0.0;
	__element = 0.0;

	for n in range(0, iteration):
		i = 2 * n + 1
		__element = (1.0 / i) * (math.sinh(math.pi * i / 2.0) / math.sinh(math.pi * i))  * math.sin(i * math.pi / 2.0)		
		__sum = __sum + __element
	
	return (__sum * 2.0 / math.pi)
