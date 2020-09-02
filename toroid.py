import math
from math import pi

class param():
	def __init__(self, *args):
		count = 0
		for arg in args:
			count++
		
		if (count > 0):
			self.a = args[0]
		if (count > 1):
			self.b = args[1]
		if (count > 2):
			self.c = args[2]
		if (count > 3):
			self.d = args[3]
		if (count > 4):
			self.e = args[4]
		if (count > 5):
			print("Argument list can not exceed 5 elements!")
		
class core():
	def __init__(self, **kwargs):
		self.Ae = kwargs['Ae']
		self.Le = kwargs['Le']
		self.ui = kwargs['ui']
		self.V = kwargs['V']
		self.N = kwargs['N']
		self.permparams = kwargs['permparams']
		self.lossparams = kwargs['lossparams']
		self.acpermparams = kwargs['acpermparams']
		self.pfdparams = kwargs['pfdparams']
		return
	
	def H(I):
		return (0.4*pi*self.N*I/self.Le)
	
	def peakFluxDensity(self, Irms, f):
		Imax = Irms * math.sqrt(2.0)
		H = H(Imax)
		return Bpk

	def perm(self, f):
		pr = self.permparams
		return ((1.0 / (pr.a + pr.b * f**pr.c)) + pr.d)

	def acPermeability(Erms, f):
		pr = self.acpermparams
		Bpk = peakFluxDensity(self, Erms, f)
		term0 = 1.0 / (pr.a + pr.b * Bpk**pr.c)
		term1 = 1.0 / (pr.d * Bpk**pr.e)
		term2 = 1.0 / f
		uiac = self.ui * (1e-2/(term0+term1+term2))
		return uiac

	def inductance(self, Erms, f):
		perm = self.ui * self.acPermeability(Erms, f)
		l = 4 * math.pi * 1e-9 * (perm * self.N **2 * self.Ae) / self.Le
		return l

	def coreLoss(self, Erms, f):
		pr = self.lossparams
		Bpk = self.peakFluxDensity(Erms, f)
		return (self.V * 1e-3 * ((f / (pr.a*Bpk**-3 + pr.b*Bpk**-2.3 + pr.c*Bpk**-1.65)) + pr.d * Bpk**2 * f**2))

