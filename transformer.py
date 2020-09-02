import cmath
import math

# Lo1: Open circuit inductance of the primary winding.
# Lo2: Open circuit inductance of the secondary winding.
# Ls1: Short circuit inductance of the primary winding.
# Ls2: Short circuit inductance of the secondary winding.
def getParams(Lo1, Lo2, Ls1, Ls2):
	M = ((Lo1 - Ls1) * (Lo2 - Ls2) * Lo1 * Lo2)**0.25
	L1 = Lo1
	L2 = Lo2
	Ll1 = Ls1
	Ll2 = Ls2
	k = M/(Lo1*Lo2)**0.5
	return {'M':M, 'L1':L1, 'L2':L2, 'Ll1': Ll1, 'Ll2': Ll2, 'k':k}
	
def getInputImpedance(M, L1, L2, f, Zld):
	w = 2*math.pi*f
	return (1j*w*L1 + (w*M)**2 / (1j*w*L2 + Zld))

def getInputCurrent(Vs, M, L1, L2, f, Zld):
	w = 2*math.pi*f
	return (Vs / getInputImpedance(M, L1, L2, f, Zld))

def getLoadCurrent(Vs, M, L1, L2, f, Zld):
	w = 2*math.pi*f
	return (1j * w * M * getInputCurrent(Vs, M, L1, L2, f, Zld) / (1j * w * L2 + Zld))
