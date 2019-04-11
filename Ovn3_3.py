# Alexander Fagerlund, grudat19 uppg 3.3, VG-version

def signsort(data):
    """Separates positive and negative values in array containing NUMBERS. ...
    Counts 0 as positive. Not defined for non-numbers, don't try. ...
    Time complexity: O(n) (average case). Space complexity: O(1)."""
    pos_index_finder = 0    # "walks" to the right from beginning of list, finding indices with positive numbers
    neg_index_finder = len(data) - 1   # "walks" to the left from end of list, finding indices with negative numbers
    pos_index_found = 0
    neg_index_found = 0
    value_holder = None

    while pos_index_finder < neg_index_finder:
        if pos_index_found == 0:
            if data[pos_index_finder] < 0:
                pos_index_finder += 1   # updates index for leftmost positive value.
            else:
                pos_index_found = 1     # leftmost positive found. Prerequisite for swap met.
        if neg_index_found == 0:
            if data[neg_index_finder] >= 0:
                neg_index_finder -= 1   # updates index for rightmost negative value.
            else:
                neg_index_found = 1     # rightmost negative found. Prerequisite for swap met.
        if pos_index_found == 1 and neg_index_found == 1:   # If ready for swap
            value_holder = data[neg_index_finder]
            data[neg_index_finder] = data[pos_index_finder]
            data[pos_index_finder] = value_holder
            pos_index_found = 0     # resets swap readiness.
            neg_index_found = 0
        
    print(data)
    return data







# Unit test:
assert signsort([1,-2]) == [-2, 1]
signsort([-4,6.5,8,-10])
signsort([8,-1,-2,-3,8,0,0,0,-6,8])
assert signsort([0,0,0,0,0,0]) == [0,0,0,0,0,0]
signsort([4,-3,4,-5,-345234626456546546546.54363564365364543566446356,0])
assert signsort([9]) == [9]
signsort([8.56565,-0.01,-2])

