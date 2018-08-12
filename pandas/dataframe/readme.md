## Fundamental DataFrame Operations

Covers the basic operations that you can do on your newly created DataFrame: adding, selecting, deleting, renaming.

### How To Select an Index or Column From a Pandas DataFrame

##### Sample Data

```bash
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9
```
Access the value that is at index 0, in column ‘A’.

```python
# Using `iloc[]`
print(df.iloc[0][0])

# Using `loc[]`
print(df.loc[0]['A'])

# Using `at[]`
print(df.at[0,'A'])

# Using `iat[]`
print(df.iat[0,0])
```

Output

```bash
output:
    1
    1
    1
    1
```

> The most important ones to remember are, without a doubt, .loc[] and .iloc[].

#### How do you select rows and columns?

```python
# Use `iloc[]` to select row `0`
print(df.iloc[0])

# Use `loc[]` to select column `'A'`
print(df.loc[:,'A'])
```

```bash
output:
    A    1
    B    2
    C    3
    Name: 0, dtype: int64
    0    1
    1    4
    2    7
    Name: A, dtype: int64
```

### How To Add an Index, Row or Column to a Pandas DataFrame

When you create a DataFrame, you have the option to add input to the ‘index’ argument to make sure that you have the index that you desire. When you don’t specify this, your DataFrame will have, by default, a numerically valued index that starts with 0 and continues until the last row of your DataFrame.

```python
# Print out your DataFrame `df` to check it out
print(df)

# Set 'C' as the index of your DataFrame
df.set_index('C')
```

Output

```
output:
       A  B  C
    0  1  2  3
    1  4  5  6
```

#### Adding Rows to a DataFrame

Before you can get to the solution, it’s first a good idea to grasp the concept of `loc` and how it differs from other indexing attributes such as `.iloc[]` and `.ix[]`:

`.loc[]` works on labels of your index. This means that if you give in loc[2], you look for the values of your DataFrame that have an index labeled 2.

`.iloc[]` works on the positions in your index. This means that if you give in iloc[2], you look for the values of your DataFrame that are at index ’2`.

`.ix[]` is a more complex case: when the index is integer-based, you pass a label to .ix[]

`.ix[2]` then means that you’re looking in your DataFrame for values that have an index labeled 2. This is just like .loc[]! However, if your index is not solely integer-based, ix will work with positions, just like .iloc[].

```python
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index= [2, 'A', 4], columns=[48, 49, 50])

# Pass `2` to `loc`
print(df.loc[2])

# Pass `2` to `iloc`
print(df.iloc[2])

# Pass `2` to `ix`
print(df.ix[2])
```

Output

```bash
output:
    48    1
    49    2
    50    3
    Name: 2, dtype: int64
    48    7
    49    8
    50    9
    Name: 4, dtype: int64
    48    7
    49    8
    50    9
    Name: 4, dtype: int64

```


### How to Delete Indices, Rows or Columns From a Pandas Data Frame

#### Deleting an Index from Your DataFrame

If you want to remove the index from your DataFrame, you should reconsider because DataFrames and Series always have an index.

However, what you *can* do is, for example:

* resetting the index of your DataFrame or
* remove the index name, if there is any, by executing `del df.index.name`,
* remove duplicate index values by resetting the index, dropping the duplicates of the index column that has been added to your DataFrame and reinstating that duplicateless column again as the index:

```python
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]), 
                  index= [2.5, 12.6, 4.8, 4.8, 2.5], 
                  columns=[48, 49, 50])
                  
df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index')
```

### How to Rename the Index or Columns of a Pandas DataFrame


```python
# Check out your DataFrame `df`
print(df)

# Define the new names of your columns
newcols = {
    'A': 'new_column_1', 
    'B': 'new_column_2', 
    'C': 'new_column_3'
}

# Use `rename()` to rename your columns
df.rename(columns=newcols, inplace=True)

# Use `rename()` to your index
df.rename(index={1: 'a'})
```

### How To Format The Data in Your Pandas DataFrame

To replace certain strings in your DataFrame, you can easily use replace(): pass the values that you would like to change, followed by the values you want to replace them by.

```python
# Study the DataFrame `df` first
print(df)

# Replace the strings by numerical values (0-4)
df.replace(['Awful', 'Poor', 'OK', 'Acceptable', 'Perfect'], [0, 1, 2, 3, 4]) 
```

#### Removing Parts From Strings in the Cells of Your DataFrame

```python
# Check out your DataFrame
print(df)

# Delete unwanted parts from the strings in the `result` column
df['result'] = df['result'].map(lambda x: x.lstrip('+-').rstrip('aAbBcC'))

# Check out the result again
print(df)
```

```bash
output:
      class test result
    0     1    2    +3b
    1     4    5    -6B
    2     7    8    +9A
      class test result
    0     1    2      3
    1     4    5      6
    2     7    8      9
```


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





