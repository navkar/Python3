import numpy

arr = [[1,3],[2,4],[3,5]]

arr2d = numpy.array(arr)

# prints 2d array
# [[1 3]
#  [2 4]
#  [3 5]]
print("numpy 2d array")
print(arr2d[:]) # same as print(arr2d)

print("Row 0")
print(arr2d[0,:])

# prints row index 1
# [2 4]
print("Row 1")
print(arr2d[1,:])

# prints all elements of the first column
# [1 2 3]
print("elements of 1st Column")
print(arr2d[:,0])

# prints all elements of the second column
# [3 4 5].
print("elements of 2nd Column")
print(arr2d[:,1])

