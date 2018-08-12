## Fundamental DataFrame Operations

Covers the basic operations that you can do on your newly created DataFrame: adding, selecting, deleting, renaming.

### How To Select an Index or Column From a Pandas DataFrame

### How To Add an Index, Row or Column to a Pandas DataFrame

### How to Delete Indices, Rows or Columns From a Pandas Data Frame

### How to Rename the Index or Columns of a Pandas DataFrame

### How To Format The Data in Your Pandas DataFrame

### How To Create an Empty DataFrame

The function that you will use is the Pandas `Dataframe()` function: it requires you to pass the data that you want to put in, the indices and the columns.

Remember that the data that is contained within the data frame doesn’t have to be homogenous. It can be of different data types!

There are several ways in which you can use this function to make an empty DataFrame. Firstly, you can use `numpy.nan` to initialize your data frame with NaNs. Note that `numpy.nan` has type `float`.

```python
import pandas as pd

df = pd.DataFrame(np.nan, index=[0,1,2,3], columns=['A'])
print(df)
```

#### Output

```bash
<script.py> output:
        A
    0 NaN
    1 NaN
    2 NaN
    3 NaN
```

The data type of the data frame is inferred by default: because `numpy.nan` has type `float`, the data frame will also contain values of type `float`. You can, however, also force the `DataFrame` to be of a certain type by adding the attribute `dtype` and filling in the desired type. Just like in this example:

```python
df = pd.DataFrame(index=range(0,4),columns=['A'], dtype='float')
print(df)
```

Note that if you don’t specify the axis labels or index, they will be constructed from the input data based on common sense rules.





