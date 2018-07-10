
# Python3 interpreter on a Mac

* [Python3 Download](https://www.python.org/downloads/release/python-370/)
* [Python Language Reference](https://docs.python.org/3/tutorial/classes.html)
* [Python variables as pointers](http://scottlobdell.me/2013/08/understanding-python-variables-as-pointers/)
* [USGS Json](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
* [Python JSON Reference](https://docs.python.org/3/library/json.html)

```

Naveens-MacBook-Pro:~ navkar$ python3
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4+4
8
>>> print("Hello")
Hello
>>> exit()

```

## What does if \_\_name\_\_== "\_\_main\_\_" do?
Consider the following lines of code...

### Foo.py
```
print __name__
if __name__ == '__main__':
    print 'XXXX'
```

File foo.py can be used in the following two ways...

### imported in another file : 
```
import foo
```

In this case \_\_name\_\_ is foo, the code section does not execute and will not print XXXX.

### executed directly : 
```
python foo.py
```

* When it is executed directly, \_\_name\_\_ is same as \_\_main\_\_ and the code in that section executes and prints XXXX
* One can write various unit tests within the same module.

### List comprehensions

[list-comprehensions](http://blog.cdleary.com/2010/04/learning-python-by-example-list-comprehensions/)

Syntax : **result** = [**transform**  **iteration**  **filter** ]

#### Creates a new list with the lengths of each of the items 
```
fruits = ['apple', 'mango', 'kiwi', 'watermelon', 'pear']
list_len=[len(item) for item in fruits]
In [1]: list_len
Out[1]: [5, 5, 4, 10, 4]
```

#### Find fruits starting with letter 'a' in the list of fruits and create a new list 
```
fruits = ['apple', 'mango', 'kiwi', 'watermelon', 'pear']
find_apple = [item for item in list if item.startswith('a')]
```




