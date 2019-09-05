# Generate multiples

This program accepts integer input `n` from user and prints multiples of 10 of the previous output until iterator `i` matches `n`.

```python
for i in range(1, n+1)
```

`range` is taken from **1...n+1** instead of **0...n** in order to match `i` with the current iteraton instead of matching it with the n-1th iteration.

```python
# debug: print("i: {} n: {}".format(i,n))
```

...is used to check the current iteration for debugging code.
