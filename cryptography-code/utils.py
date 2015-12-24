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

# Function: gcd
# ---------------
# Computes the inverse of an integer a modulo m using the Euclidean algorithm
def inverse(a, m):
	assert(type(a) == type(1) and type(m) == type(1))

# Function: gcd
# ---------------
# Computes the exponent of an integer a to the power of e, modulo m 
def exponentiate(a, e, m):
    binRep = bin(e)[2:]
    binExponents = {0: 1}
    for i in range(1, len(binRep)):
        binExponents[i] = (binExponents[i - 1] ** 2) % m
    result = 1
    exp = 0
    for b in reversed(binRep):
        if b == '1':
            result = (result * binExponents[exp]) % m 
        exp += 1
    return result
