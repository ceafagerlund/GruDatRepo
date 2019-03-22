# Alexander Fagerlund, grudat19 uppg 1.1

def factorial(n):
   """Given natural number n, find n!."""
   if n == 1 or n == 0:
      return 1
   else:
      return n*factorial(n-1)


# Test
assert not factorial(3) == 5
assert factorial(3) == 6
assert not factorial(10) == 456
assert factorial(1) == 1
assert factorial(0) == 1
