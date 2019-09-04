'''
author: @chinmaykunkikar
'''

# check whether a given number is or or even
n = int(input("Enter a number: "))
if (n % 2) != 0:
   print("{} is odd".format(n))
else:
   print("{} is even".format(n))


# more optimized version of the test (not really)
'''
n = int(input("Enter a number: "))
if n & 1:
   return '{} is odd'.format(n)
else:
   return '{} is even'.format(n)
'''