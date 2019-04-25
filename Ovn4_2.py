# Övning 4, uppgift 2, Alexander Fagerlund

def Countingsort(vect):
    """Given array "vect" with length n of natural numbers...
    with maximum value k, sorts array with worst case time...
    complexity O(n + k). Not defined for other input, don't try."""

    freqs = [0]*(max(vect)+1)   # O(n), but only done twice.
    cumul_freqs = [0]*(max(vect)+1)
    sort = [0]*len(vect)
    
    for i in range (0,len(vect)): # O(n)      
        freqs[vect[i]] += 1
    print(freqs)

    for i in range (0,len(freqs)):  # O(k)
        if i > 0:
            cumul_freqs[i] += cumul_freqs[i-1]
        cumul_freqs[i] += freqs[i]
    print(cumul_freqs)

    for i in range(0,len(vect)):
        sort[cumul_freqs[vect[i]]-1] = vect[i]  
        cumul_freqs[vect[i]] -= 1
    print(sort)
    return sort
            
    


# Unit test

assert Countingsort([8,9,4,4,4,0,1,5,10]) == [0,1,4,4,4,5,8,9,10]
assert Countingsort([1,2]) == [1,2]
assert Countingsort([0]) == [0]
assert Countingsort([4,5,345,5]) == [4,5,5,345]
