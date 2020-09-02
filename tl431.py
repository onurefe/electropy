vref = 2.495

def vka(rup, rdown):
	return (vref * (1.0 + (rup/rdown)))

def rup(rdown, vka):
	return (rdown * ((vka/vref) - 1.0))

def rdown(rup, vka):
	return (rup / ((vka/vref) - 1.0))
