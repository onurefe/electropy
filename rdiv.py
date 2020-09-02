def rup(vcc, vo, rdown):
	return (rdown * (vcc / vo - 1.0))

def rdown(vcc, vo, rup):
	return (rup * ((vcc / vo) - 1.0))

def rdiv(vcc, vo, rtotal):
	rup = (vo / vcc) * rtotal
	rdown = rtotal - rup
	return {'rup':rup, 'rdown':rdown}
	

