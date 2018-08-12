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
    RangeIndex(start=0, stop=2, step=1)

<script.py> output:
    (2, 3)
    2

```



