# Primality tests

Checking whether a number is **prime** is called as primality test. There are several tests to check whether a number is prime or not (or in some cases, if a number is composite). They are generally categorized as -

* Probabilistic Tests (Monte Carlo tests) or
* Deterministic Tests

---
The most **basic algorithm** for testing whether a number is prime or not is to divide the given number `n` from the range of `2..n-1`. If the number gets divided evenly (generates no remainder), then the number is composite, otherwise, it is a prime number. But this test if **not efficient** for large numbers at it has a time complexity of `O(n)`. It means that as the `n` gets larger, the time it takes to run the algorithm will increase proportionally to n.
###### This algorithm can be optimized by introducing few conditions -

1. Only dividing `n` till `sqrt(n)` and not `n-1`. Because a larger factor of n must be a multiple of smaller factor that has already been checked.
2. Eliminating the multiples of 2. This will directly eliminate all the even number from the array of divisors till sqrt(n).
3. Prime numbers greater than 6 are in the form of `(6k+1) or (6k-1)`. This is because all integers can be expressed in the form `(6k+i)` for some `int k` and for `i = {-1, 0, 1, 2, 3, 4}`; `2` divides `(6k+0), (6k+2), (6k+4)`; and `3` divides `(6k+3)`. So a more efficient method is to test if n is divisible by 2 or 3, and then to check through all the numbers of the form `(6k+1 <= sqrt(n) || 6k-1 <= sqrt(n))`.

These optimization conditions will reduce time complexity to `O(sqrt(n))`. Which is still not very fast as an improvement over `O(n)`.

The python implementation of this optimized solution is as follows:

```python
def isPrime(n) :
    # in case of 0 and -ve numbers
    if (n <= 0) :
        return "Input only positive integers"
    # in case of 1
    if (n = 1) :
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
            return '{} is NOT a prime number. It is divisible by {} or {}'.format(n, k, k+2)
        k += 6  # will give us the next multiple of 6

    return '{} is a prime number'.format(n)
```

The following will be the *test cases* that will make sure every loop is visited.

```python
# test cases
print(isPrime(1))          # case of 1
print(isPrime(2))          # case of 2 and 3
print(isPrime(3))          # case of 2 and 3
print(isPrime(-47))        # case of a negative number
print(isPrime(42))         # divisible by 2 and 3
print(isPrime(113))        # prime
print(isPrime(23))         # prime
print(isPrime(814733))     # random
print(isPrime(73939133))   # largest 8-digit prime
```

---

### Probabilistic Tests

These tests are more commonly practiced in real world. They provide provable bounds on the probability of being fooled by a composite number. These tests are the fastest of the algorithms discovered among the primality tests. Probabilistic tests generate a 'probable prime' number and are not "brute forced" like the method discussed above. They have probabilistic factors involved which will produce the answers. Since these are not determined mathematically, there is a possibility of getting a wrong answer. These tests have a randomness factor called seed. This seed can be adjusted for accurate answers. The error of getting wrong answers can be reduced by running the algorithm repeatedly a few times just to be sure. These tests usually test whether a number is composite rather than if it is a prime number.
Probabilistic tests are very efficient algorithms since the time complexity can go upto `O(ln^2 n)` for some algorithms like [Baillie-PSW test](https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test "Wikipedia").
A very commonly implemented probabilistic algorithm is [Fermat's algorithm](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem "Wikipedia") and [Miller-Rabin's algorithm](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test "Wikipedia").

### Deterministic Tests

These tests have the ability to surely tell whether a number is prime or not. Can be provable and deterministic  and polynomial time can be calculated mathematically. The most famous test was developed by M. **A**grawal, N. **K**ayal and N. **S**axena of IIT Kanpur in 2002. Also known as **AKS Test**, this was the first *provably unconditional deterministic polynomial time* test. The complexity of this algorithm was `O(ln^12 n)` which was further reduced to `O(ln^6 n)` by adding a condition that if the [Sophie Germain cojecture](https://en.wikipedia.org/wiki/Sophie_Germain_prime "Wikipedia") is true. The conjecture says that *'p is prime if 2p+1 is also prime'*.
Lenstra-Pomerance presented a version of AKS test that runs in time `O(ln^6 n)` unconditionally.
Despite being the **most efficient** algorithm in theory, AKS is never used in the real world because although deterministic algorithms have the ability to surely tell whether a number is prime or not, probabilistic algorithms are faster than deterministic tests. The program can be run a few times to make sure the number is prime. Also, the probability of an error is just 20 in a billion. But AKS test is important for development of Computer Science.
