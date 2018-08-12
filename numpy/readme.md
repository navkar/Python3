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

```python
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

<class 'numpy.ndarray'>
```