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
    x = [4 , 9 , 6, 3, 1]
    x[1]
```    

#### For numpy specifically, you can also use boolean numpy arrays:

```python    
    import numpy as np
    y = np.array(x)
    y[1]


    high = y > 5
    y[high]

```