'''
@author: chinmaykunkikar
'''
# sieve of Eratosthenes
def SieveOfEratosthenes(lim):
    primes = [True for i in range(lim+1)]
    p = 2
    while (p * p <= lim):
        # if primes[p] is not changed, then it is a prime
        if (primes[p] == True):
            # update all multiples of p
            for i in range(p * p, lim+1, p):
                primes[i] = False
        p += 1

    # print prime numbers
    print("The prime numbers for the set limit are: ")
    for p in range(2, lim):
        if primes[p]:
            print(p, end=" ")

lim = 113
SieveOfEratosthenes(lim)