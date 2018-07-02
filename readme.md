
# Python3 interpreter on a Mac

* [Python3 Download](https://www.python.org/downloads/release/python-370/)
* [Python Language Reference](https://docs.python.org/3/tutorial/classes.html)

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

```
print __name__
if __name__ == '__main__':
    print 'XXXX'
```

A file code.py can be used in the following two ways...

### imported in another file : 
```
import foo
```

In this case \_\_name\_\_ is foo, the code section does not get executed and does not print XXXX.

### executed directly : 
```
python foo.py
```

* When it is executed directly, \_\_name\_\_ is same as \_\_main\_\_ and the code in that section is executed and prints XXXX
* One use of this functionality to write various kind of unit tests within the same module.
