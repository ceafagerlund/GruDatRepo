# Dynamisk programmering, rekursiv funktion för p(n),
# Gru_dat,Alexander Fagerlund

def p(n,h):
    """Recursively calculates maximum profit...
    from making scarves from n meters of yarn, where
    n is a natural number.
    Time complexity: O(exp(n))."""
    prev = 0
    if n == 0:
        return 0
    else:
        for i in range (1,n+1):
            if i <= 4:
                new = h[i]+p(n-i,h)
                if prev < new:
                    prev = new
            else:
                new = p(n-i-1,h)
                if prev < new:
                    prev = new
        maximum = prev
        return maximum


# Unit test:
h = [0,2,5,6,9]
assert p(5,h) == 12
assert p(4,h) == 10
assert p(3,h) == 7
assert p(2,h) == 5
assert p(1,h) == 2
assert p(0,h) == 0

