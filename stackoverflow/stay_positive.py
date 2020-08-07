import functools

"""
For given a list e.g. [-4,3,2,1]. Start with some value x, and add each ofthe list element to it consecutively.
That is calculate a running sum of a x plus each of the array elemnt. Determine the minimum value of x such that the
running sum is always at least 1.

if x = 5, the running sums are:

    5 + -4 = 1
    1 + 3 = 4
    4 + 2 = 6
    6 + 1 = 7
"""

def minStart(arr):
    arr.insert(0,0)
    inital = 0
    add = 0
    for i in range(len(arr)):
        l = arr[:i+1]
        add = functools.reduce((lambda a,b: a+b), l)
        if add<=0:
            inital = inital + abs(add) + 1
            arr[0] = inital
    return inital

arr = [-13,60,-900,-10,-40,-60,-50]

print(minStart(arr))