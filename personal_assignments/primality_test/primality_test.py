'''
author: @chinmaykunkikar
'''

def isPrime(n) :
    # in case of 0 and -ve numbers
    if (n <= 0) :
        return '{}. Input only positive integers.'.format(n)
    # in case of 1
    if (n == 1) :
        return '{} is NOT a prime number'.format(n)

    # this will return true if n is 2 or 3
    if (n <= 3) : 
        return '{} is a prime number'.format(n)

    # if n is divisible by either 2 or 3, then it is not prime.
    # Also if we check the form (6k+i) here,
    # 2 divides (6k+0), (6k+2), (6k+4); and 3 divides (6k+3).
    if (n % 2 == 0 or n % 3 == 0) : 
        return '{} is NOT a prime number. It is divisible by 2 or 3.'.format(n)

    # now check if (6k+1) or (6k-1) factorizes n
    k = 5   # we take k = 5 here because it is in the form (6k-1)
    while(k * k <= n) : 
        if (n % k == 0 or n % (k + 2) == 0) :   # here we check for (6k-1) and (6k+1)
            return '{} is NOT a prime number. It is divisible by {} or {}.'.format(n, k, k+2)
        k += 6  # will give us the next multiple of 6

    return '{} is a prime number'.format(n)

# test cases
print(isPrime(1))          # case of 1
print(isPrime(2))          # case of 2 and 3
print(isPrime(3))          # case of 2 and 3
print(isPrime(-947))       # case of a negative number
print(isPrime(42))         # divisible by 2 and 3
print(isPrime(113))        # prime
print(isPrime(23))         # prime
print(isPrime(814733))     # random
print(isPrime(73939133))   # largest 8-digit prime