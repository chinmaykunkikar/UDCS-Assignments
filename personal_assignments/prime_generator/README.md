# Prime number generator

There are many methods of generating prime number upto a given limit. The most common and fastest being the `prime seives`. There are many seive algorithms:

* [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes "Wikipedia")
* [Sieve of Atkin](https://en.wikipedia.org/wiki/Sieve_of_Atkin "Wikipedia")
* [Wheel sieves](https://en.wikipedia.org/wiki/Wheel_factorization "Wikipedia")
* [Sieve of Sundaram](https://en.wikipedia.org/wiki/Sieve_of_Sundaram "Wikipedia")

The most famous being the first two, *sieve of Eratosthenes* and *sieve of Atkin*.

### Sieve of Eratosthenes

The sieve of Eratosthenes is the most efficient ways to find all primes smaller than `n` when `n` is lesser than 10 million. It is also the oldest known algorithm, dating back to 270BC.

##### Algorithm

1. Create a list of consecutive integers from 2...n
2. Initially, let p=2 (the first prime number).
3. Starting from p^2, count up in increments of p and mark each of these numbers greater than or equal to p^2 itself in the list. These numbers will be p(p+1), p(p+2), p(p+3), etc..
4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.

##### Time and space complexities of Sieve of Eratosthenes

* *Time complexity*: `O(n(log(log(n))))`
* *Space complexity*: `O(n)`

The python implementation of this solution is as follows:

```python
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
    for p in range(2, lim):
        if primes[p]:
            print(p)
```

##### Disadvantages

* The algorithm traverses along the memory multiple times and only manipulates single element at a time.
* Time complexity `O(n(log(log(n))))` is not very efficient.

### Sieve of Atkin

Sieve of Atkin is computationally efficient than Sieve of Eratosthenes as it marks multiple of square of prime numbers.

##### Algorithm

1. Create a list named `final list` and fill it with `[2,3,5]`.
2. Create a list named `sieve list` with an entry for each positive integer and intially mark them as non prime.
3. For each entry number n in the sieve list, with *modulo-sixty remainder* `r`:
   * If r is [1, 13, 17, 29, 37, 41, 49, 53], flip the entry for each possible solution to `4x^2 + y^2 = N`.
   * If r is [7, 19, 31, 43], flip the entry for each possible solution to `3x^2 + y^2 = N`.
   * If r is [11, 23, 47, 59], flip the entry for each possible solution to `3x^2 – y^2 = N` when `x > y`.
   * If r is something else, ignore it.
4. Start with the lowest number in the sieve list.
5. Take the next number in the sieve list still marked prime.
6. Include the number in the results list.
7. Square the number and mark all multiples of that square as non prime. Note that the multiples that can be factored by 2, 3, or 5 need not be marked, as these will be ignored in the final enumeration of primes.
8. Repeat steps four through seven.

##### Time and space complexities of Sieve of Atkin

* *Time complexity*: `O(n)`
* *Space complexity*: `O(n)`
