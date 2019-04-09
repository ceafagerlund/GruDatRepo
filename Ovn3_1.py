# Alexander Fagerlund, grudat19 uppg 3.1

def factorial(n):
   """Given natural number n, factorial finds n!."""
   if n == 1 or n == 0:
      return 1
   else:
      return n*factorial(n-1)


# Test
assert not factorial(3) == 5
assert factorial(3) == 6
assert not factorial(10) == 456789
assert factorial(1) == 1
assert factorial(0) == 1


### Giltighetsbevis:

### Basfall: Om n = 0 eller n = 1 returneras 0! = 1! = 1.

### Induktionsantagande: Antag att factorial är korrekt för talet n > 0.

### För talet  n+1 > 1 är factorial(n+1) = (n+1)*factorial(n). Vi antog att
### factorial(n) = n!, så factorial(n+1) = (n+1)*factorial(n)
### = (n+1)*n! = (n+1)!.

### Eftersom vi vet att factorial är korrekt för n = 1 > 0 och att om
### det gäller för  något n > 0 gäller det även för n + 1 är factorial korrekt 
### för alla n i N (inklusive n = 0, som vi kontrollerat separat).
