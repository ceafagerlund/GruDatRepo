# Alexander Fagerlund, grudat19 uppg 3.2, VG-version.


def mode(data):
    """Given array "data" of integers, finds mode. ...
    If multiple values equally common, returns ...
    minimum value. Not defined for empty list, ...
    don't try. Time complexity: O(n) (expected time)."""

    hash_table = dict()
    key_stats = []
    minimum = data[0]

    for i in range (0,len(data)):
        if data[i] in hash_table:   #is data key in table
            hash_table[data[i]] += 1 #if key, up the value
        else:
            hash_table[data[i]] = 1 # set initial valuecount to 1
        if hash_table[data[i]] > hash_table[minimum]:   #updating minimum value
            minimum = data[i]
        elif hash_table[data[i]] == hash_table[minimum] and data[i] < minimum:
            minimum = data[i]
    print("Typvärdet är:",minimum)
    return minimum

#Testing code
assert mode([1,8,9,345,8,9,9,8]) == 8
assert mode([2]) == 2
assert mode([7,6,7,7,6,66666666666666]) == 7
assert mode([0]) == 0
assert mode([1,1,1,1,1,1,1,1,1,0]) == 1
