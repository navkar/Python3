## Pandas - Concept of a DataFrame

Pandas is a popular Python package for data science, and with good reason: it offers powerful, expressive and flexible data structures that make data manipulation and analysis easy, among many other things. The DataFrame is one of these structures.

### How To Create a Pandas DataFrame

To make a data frame from a NumPy array, you can just pass it to the DataFrame() function in the data argument.

```python
data = np.array([['','Col1','Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])
                
print(pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:]))
```

You first select the values that are contained in the lists that start with `Row1` and `Row2`, then you select the index or row numbers `Row1` and `Row2` and then the column names `Col1` and `Col2`.

Printed out a small selection of the data by subsetting 2D NumPy arrays: you first indicate the row that you want to look in for your data, then the column.

Output

```bash
<script.py> output:
         Col1 Col2
    Row1    1    2
    Row2    3    4
```

#### Example 1: DataFrames from CSV files

```python
import pandas as pd
users = pd.read_csv('datasets/users.csv', index_col=0)
print(users)
```

#### Example 2: Creating DataFrames from different data structures

```python
# Take a 2D array as input to your DataFrame 
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(my_2darray))

# Take a dictionary as input to your DataFrame 
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print(pd.DataFrame(my_dict))

# Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print(pd.DataFrame(my_df))

# Take a Series as input to your DataFrame
my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
print(pd.DataFrame(my_series))
```

Output

```bash
<script.py> output:
       0  1  2
    0  1  2  3
    1  4  5  6
       1  2  3
    0  1  1  2
    1  3  2  4
       A
    0  4
    1  5
    2  6
    3  7
                             0
    Belgium           Brussels
    India            New Delhi
    United Kingdom      London
    United States   Washington
```

#### Example 3: Create a dataframe from a dictionary

```python
import pandas as pd
import numpy as np

cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ['Sunday', 'Sunday', 'Monday', 'Monday']
list_labels = ['city', 'signups', 'visitors', 'weekday']
list_cols = [cities, signups, visitors, weekdays]

# Note: The zip() function in Python 3 and above returns a special zip object, which is essentially a generator. 
# To convert this zip object into a list, you'll need to use list()
zipped =  list(zip(list_labels, list_cols))

print("zipped...")
print(zipped)

data = dict(zipped)
users = pd.DataFrame(data)
print("---- Data frame ---")
print(users)
print("---- Data frame ---")
```
#### Output

```bash
zipped...
[('city', ['Austin', 'Dallas', 'Austin', 'Dallas']), ('signups', [7, 12, 3, 5]), ('visitors', [139, 237, 326, 456]), ('weekday', ['Sunday', 'Sunday', 'Monday', 'Monday'])]
---- Data frame ---
     city  signups  visitors weekday
0  Austin        7       139  Sunday
1  Dallas       12       237  Sunday
2  Austin        3       326  Monday
3  Dallas        5       456  Monday
---- Data frame ---
```


### DataFrame properties

After you have created your DataFrame, you might want to know a little bit more about it. You can use the `shape` property or the `len()` function in combination with the `.index` property:

```python
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))

# Use the `shape` property
print(df.shape)

# Or use the `len()` function with the `index` property
print(len(df.index))
```

The shape property will give you the dimensions of your DataFrame. That means that you will get to know the width and the height of your DataFrame. 

On the other hand, the len() function, in combination with the index property, will only give you information on the height of your DataFrame.

Output

```bash
<script.py> output:
    (2, 3)
    2
```

### Broadcasting with a dictionary

So the term broadcasting comes from numpy, simply put it explains the rules of the output that will result when you perform operations between n-dimensional arrays (could be panels, dataframes, series) or scalar values.

> In order to broadcast, the size of the trailing axes for both arrays in an operation must either be the same size or one of them must be one.

```python
In [6]:    
df = pd.DataFrame({'a':np.random.randn(4), 'b':np.random.randn(4)})
df

Out[6]:
          a         b
0  0.216920  0.652193
1  0.968969  0.033369
2  0.637784  0.856836
3 -2.303556  0.426238

In [7]:    
df * 10

Out[7]:
           a         b
0   2.169204  6.521925
1   9.689690  0.333695
2   6.377839  8.568362
3 -23.035557  4.262381
```

So what is technically happening here is that the scalar value has been broadcasted along the same `dimensions` of the Series and `DataFrame` above.

```python
import pandas as pd

heights = [59.0, 65.2, 62.9, 45.6, 34.5]
data = { 'height': heights, 'sex': 'M'}
results = pd.DataFrame(data)
print(results)


   height sex
0    59.0   M
1    65.2   M
2    62.9   M
3    45.6   M
4    34.5   M
```

## Links

[what-does-the-term-broadcasting-mean-in-pandas-documentation](https://stackoverflow.com/questions/29954263/what-does-the-term-broadcasting-mean-in-pandas-documentation)



