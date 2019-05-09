# Halsduksuppgift med caching, Gru_dat, Alexander Fagerlund

def CacheScarf(n,h,cache):
    """Finds maximum profit from making scarves from n meters
    of yarn, n being a natural number. Do not use other input.
    Time complexity: O(n^2)."""
    cache = [None]*n        #works, as no reset is made after last call
    prev = 0
    if n == 0:              # base case
        return 0
    else:
        for i in range (1,n+1):
            new = 0
            if not cache[n-i]:  # checks if already computed
                cache[n-i] = CacheScarf(n-i,h,cache)
            new += cache[n-i]   #adds recursion call value
            if i <= 4:
                    new += h[i] #adds h-value                   
            if prev < new:
                prev = new
    maximum = prev              # finds maximum
    return maximum


cache = []

# Unit test:
h = [0,2,5,6,9]
assert CacheScarf(5,h,cache) == 12
assert CacheScarf(4,h,cache) == 10
assert CacheScarf(3,h,cache) == 7
assert CacheScarf(2,h,cache) == 5
assert CacheScarf(1,h,cache) == 2
assert CacheScarf(0,h,cache) == 0



# Unit test:

