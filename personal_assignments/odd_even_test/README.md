# Odd-Even tests

There is a standard program that checks whether a given number input is odd or even.

```python
n = int(input("Enter a number: "))
if (n % 2) != 0:
   print("{} is odd".format(n))
else:
   print("{} is even".format(n))
```

But in analysis of algorithms, we talk about efficiency of a program in terms of time and space. The program can be further optimized using *bit manipulation* (`&`) as follows:

```python
n = int(input("Enter a number: "))
if n & 1:
   return '{} is odd'.format(n)
else:
   return '{} is even'.format(n)
```

The `timeit` module of python can calculate the runtime of the programs.
According to [an answer on stackoverflow](https://stackoverflow.com/a/1089945 "Is & faster than % when checking for odd numbers?"), the difference between `%` and `&` is around 10 nanoseconds. The author says *"Convincing programmers that micro-optimizations are essentially irrelevant has proven to be an impossible task."* He means that such **micro-optimizations don't really matter**.
The same answer also quotes [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth "Wikipedia") saying that *"We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil."*
Also, using `&` instead of standard modulo `%`, which most programmers use universally, affects the readability of code.
