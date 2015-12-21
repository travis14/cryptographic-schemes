# Function: gcd
# ---------------
# Computes the gcd of two integers using the Euclidean algorithm
def gcd(a, b):
    assert(type(a) == type(1) and type(b) == type(1))

    m, n = (a, b) if a > b else (b, a) #m is the larger of m, n
    while True:
    	r = m % n
    	if r == 0:
    		return n
    	m = n 
    	n = r