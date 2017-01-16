import math
c = 3.0 * 10**8

def lorentzFactor(v):
	return 1.0/(math.sqrt(1.0-(v**2/c**2)))

# v = input("Enter an expression for v: ")
v = 0.99 * c
print(lorentzFactor(v))