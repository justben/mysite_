import math
from sympy import Symbol, solve
LONG = 4

#area
def area(d1, d2, dd):
	p = (d1+d2+dd)/2
	s = math.sqrt(p*(p-d1)*(p-d2)*(p-dd))
	return s

#distance
def ptp(p1, p2):
	d = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
	return d

#distance
def ptl(p, p1, p2):
	d1 = ptp(p, p1)
	d2 = ptp(p, p2)
	dd = ptp(p1, p2)
	S = area(d1, d2, dd)
	distance = round((2*S)/dd, LONG)
	return distance

#xy
def xy(p, p1, p2):
	k = (p2[1]-p1[1])/(p2[0]-p1[0])
	b = p1[1]-k*p1[0]
	k1 = -1/k
	b1 = p[1]-k1*p[0]
	x = Symbol('x')
	xx = round(solve((k-k1)*x+(b-b1))[0], LONG)
	yy = round(k*xx+b, LONG)
	pp = [xx,yy]
	return pp

#shadow
def shadow(p, p1, p2):
	distance = ptl(p, p1, p2)
	if distance <= 10:
		k = -(p2[0]-p1[0])/(p2[1]-p1[1])
		b1 = p1[1]-k*p1[0]
		b2 = p2[1]-k*p2[0]
		if b1 > b2:
			big = b1
			small = b2
		else:
			big = b2
			small = b1

		if p[1] >= p[0]*k+small and p[1] <= p[0]*k+big:
			pp = xy(p, p1, p2)
			return pp
		else:
			return []
	else:
		return []
