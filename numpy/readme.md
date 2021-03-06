## NumPy stands for numeric python

```bash
Naveens-MacBook-Pro:PythonProjects navkar$ pip3 install numpy
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/3a/db/5c4dab58c03a7ea2561353cb240e96198415f09d65dd63d58058e135f2f9/numpy-1.15.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (24.5MB)
    100% |████████████████████████████████| 24.5MB 732kB/s 
Installing collected packages: numpy
Successfully installed numpy-1.15.0
```

## NumPy Subsetting

numpy list is different from regular python list

#### To subset both regular Python lists and numpy arrays, you can use square brackets:

```python
    x = [4, 9, 6, 3, 1]
    x[1]
    # range
    x[1:3] # [start:end] - end is exclusive
    # [9,6] 
```    

#### For numpy specifically, you can also use boolean numpy arrays:

```python
    import numpy as np
    y = np.array(x)
    y[1]

    # high is an array of type boolean
    high = y > 5
    #
    print(y[high])

```

### 2-D array subsetting using NumPy

NOTE: type `ndarray` stands for `N-dimentional array`

```python
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
```

### NumPy Side Effects

numpy is great for doing vector arithmetic. If you compare its functionality with regular Python lists, however, some things have changed.

First of all, numpy arrays cannot contain elements with different types. If you try to build such a list, some of the elements' types are changed to end up with a homogeneous list. This is known as type coercion.

Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists and numpy arrays.

```python
In [1]: np.array([True, 1, 2]) + np.array([3, 4, False])

# NOTE: True is converted to 1, False is converted to 0
Out[1]: array([4, 5, 2])

```

## Statistics 

### Average vs Median

It's always a good idea to check both the median and the mean, to get an idea about the overall distribution of the entire dataset.

```python
import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)
```

