'''
@author: chinmaykunkikar
'''
# sieve of Atkin

from math import sqrt

lim = 100

sqrtLim = (int)(sqrt(lim)) + 1 # we add 1 here because the integer sqrt squared is less than limit and a non-prime number may get added to the top of the list
#print("sqrtLim: {}".format(sqrtLim))

def SieveOfAtkin(lim):
	# initialise the prime array with False values equal to the limit n
    primes = [False] * lim
	# only values of 5+ are sieved by using the algorithm, so manually set 2 and 3
    primes[2] = True
    primes[3] = True
#
# Flip primes[n] to True if one of the following is true: 
# 1) n = 4*x*x + y*y has odd number of solutions and n % 12 = 1 or n % 12 = 5.
# 2) n = 3*x*x + y*y has odd number of solutions and n % 12 = 7.
# 3) n = 3*x*x - y*y has odd number of solutions, x > y and n % 12 = 11.
#
    for x in range(1, sqrtLim):
        for y in range(1, sqrtLim):
            n = 4*x*x + y*y
            #print("N1: {}, X1: {}, Y1: {}".format(n, x, y))
            if n <= lim and (n % 12 == 1 or n % 12 == 5):
                primes[n] = not primes[n]
            n = 3*x*x + y*y
            #print("N2: {}, X2: {}, Y2: {}".format(n, x, y))
            if n <= lim and (n % 12 == 7):
                primes[n] = not primes[n]
            n = 3*x*x - y*y
            #print("N3: {}, X3: {}, Y3: {}".format(n, x, y))
            if n <= lim and (n % 12 == 11):
                primes[n] = not primes[n]

# now eliminate non-primes (multiples of squares) by sieving
    for n in range(5, lim):
        if primes[n]:
            i = 1
            while(i*n*n < lim):
                primes[i*n*n] = False
                i += 1
# print the primes
    print("The prime numbers are:")
    for a in range(lim):
        if (primes[a]):
            print(a, end=" ")


# main
SieveOfAtkin(lim)
