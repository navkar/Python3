## Interactive Python from Browsers

* [Ipython](https://www.pythonanywhere.com/try-ipython/)
* [Jupyter](https://jupyter.org/try)

## Python reference

* [modeanalytics-python-basics](https://community.modeanalytics.com/python/tutorial/python-basics/)
* [Interactive Python Study](http://composingprograms.com/pages/11-getting-started.html#programming-in-python)
* [Python Language Reference](https://docs.python.org/3/tutorial/classes.html)
* [Python JSON Reference](https://docs.python.org/3/library/json.html)
* [NumPy reference](https://docs.scipy.org/doc/numpy/reference/)

## Python3 interpreter on a Mac

* [Python3 Download](https://www.python.org/downloads/release/python-370/)
* [Python variables as pointers](http://scottlobdell.me/2013/08/understanding-python-variables-as-pointers/)
* [USGS Json](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)

## Functional Programming with Python

* [learn-functional-python-in-10-minutes](https://hackernoon.com/learn-functional-python-in-10-minutes-to-2d1651dece6f)

```bash
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
```python
print __name__
if __name__ == '__main__':
    print 'XXXX'
```

File foo.py can be used in the following two ways...

### imported in another file : 
```python
import foo
```
In this case \_\_name\_\_ is foo, the code section does not execute and will not print XXXX.

* [how-to-import-modules-in-python](https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3)

### executed directly : 
```python
python foo.py
```
* When it is executed directly, \_\_name\_\_ is same as \_\_main\_\_ and the code in that section executes and prints XXXX
* One can write various unit tests within the same module.

### List comprehensions

[list-comprehensions](http://blog.cdleary.com/2010/04/learning-python-by-example-list-comprehensions/)

Syntax : **result** = [**transform**  **iteration**  **filter** ]

#### Creates a new list with the lengths of each of the items 
```python
fruits = ['apple', 'mango', 'kiwi', 'watermelon', 'pear']
list_len=[len(item) for item in fruits]
In [1]: list_len
Out[1]: [5, 5, 4, 10, 4]
```

#### Find fruits starting with letter 'a' in the list of fruits and create a new list 
```python
fruits = ['apple', 'mango', 'kiwi', 'watermelon', 'pear']
find_apple = [item for item in list if item.startswith('a')]
```

### Generator Expression

* A Generator object is an iterator, whose values are created at the time of accessing them.
* A generator can be obtained either from a generator expression or a generator function.

```python
x = [6, 3, 1]
g = (i**2 for i in x)  # generator expression
print(next(g))         # -> 36
```

### Generator functions

[improve-your-python-yield-and-generators](https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)

### What does \_\_init\_\_ do?

* Set multiple attributes, at once, by defining the initializer method, \_\_init\_\_ , inside the class.
* This method is called by default, during an object creation.
* It takes values passed inside the parenthesis, during an object creation, as it's arguments.
* It also takes self as the first argument, which refers to the current object.

```python
'This is known as a docstring'
class Person:
    'Initialises two attributes of a person.'
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

p1 = Person('George', 'Smith')   
print(p1.fname, '-', p1.lname)           # -> 'George - Smith'
```

### Inheritance

* In Python, every class uses inheritance and is inherited from **object** by default.

```python
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Employee(Person):
    all_employees = []

    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)

```

* In above example, Employee class utilises \_\_init\_\_ method of parent class Person, to create the object.

#### Magic command %save - saves the previous list of commands in a file

```python
%save sample_script.py 1-6
```

#### Magic command %more - view the contents of a file

```python
%show sample_script.py
```

#### Magic command %hist - history of commands

```python
%hist
```

### What is the input of a cell magic method ?

+ Python code written in multiple lines of a single cell.


### Which of the following statement retreives names of all builtin module names?

* The compiled-in module names are in **sys.builtin_module_names**

### Which of the following statement retreives names of all builtin objects?

* A dictionary of key-value pairs: \_\_builtins\_\_.\_\_dict\_\_
* The objects: \_\_builtins\_\_.\_\_dict\_\_.values()

### What does \_\_doc\_\_ do?

* The print(\_\_doc\_\_) command simply re-uses that documentation string to write it to your terminal each time you run the script, and any other python tool (like the interactive interpreter help() function, for example) can introspect that same value.
* Each class or a method definition can have an optional first line, known as docstring.
* Once documented, you can load the script into an interactive interpreter and run help command on the class.

### pass keyword

In Python we use the "pass" keyword (a statement) to indicate that nothing happens—the function, class or loop is empty. With pass, we indicate a "null" block. Pass can be placed on the same line, or on a separate line. Pass can be used to quickly add things that are unimplemented.

### Operator overloading
[Operator overloading](http://thepythonguru.com/python-operator-overloading/)

### Metaclass in python

[metaclasses-in-python](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)

A metaclass is the class of a class. Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves. A class is an instance of a metaclass.

While in Python you can use arbitrary callables for metaclasses (like Jerub shows), the more useful approach is actually to make it an actual class itself. 

**type** is the usual metaclass in Python. In case you're wondering, yes, type is itself a class, and it is its own type. You won't be able to recreate something like type purely in Python, but Python cheats a little. To create your own metaclass in Python you really just want to subclass **type**.

A metaclass is most commonly used as a class-factory. Like you create an instance of the class by calling the class, Python creates a new class (when it executes the 'class' statement) by calling the metaclass. Combined with the normal __init__ and __new__ methods, metaclasses therefore allow you to do 'extra things' when creating a class, like registering the new class with some registry, or even replace the class with something else entirely.

When the class statement is executed, Python first executes the body of the class statement as a normal block of code. The resulting namespace (a dict) holds the attributes of the class-to-be. The metaclass is determined by looking at the baseclasses of the class-to-be (metaclasses are inherited), at the __metaclass__ attribute of the class-to-be (if any) or the __metaclass__ global variable. The metaclass is then called with the name, bases and attributes of the class to instantiate it.

However, metaclasses actually define the type of a class, not just a factory for it, so you can do much more with them. You can, for instance, define normal methods on the metaclass. These metaclass-methods are like classmethods, in that they can be called on the class without an instance, but they are also not like classmethods in that they cannot be called on an instance of the class. type.__subclasses__() is an example of a method on the type metaclass. You can also define the normal 'magic' methods, like __add__, __iter__ and __getattr__, to implement or change how the class behaves.

```python
def make_hook(f):
    """Decorator to turn 'foo' method into '__foo__'"""
    f.is_hook = 1
    return f

class MyType(type):
    def __new__(mcls, name, bases, attrs):

        if name.startswith('None'):
            return None

        # Go over attributes and see if they should be renamed.
        newattrs = {}
        for attrname, attrvalue in attrs.iteritems():
            if getattr(attrvalue, 'is_hook', 0):
                newattrs['__%s__' % attrname] = attrvalue
            else:
                newattrs[attrname] = attrvalue

        return super(MyType, mcls).__new__(mcls, name, bases, newattrs)

    def __init__(self, name, bases, attrs):
        super(MyType, self).__init__(name, bases, attrs)

        # classregistry.register(self, self.interfaces)
        print "Would register class %s now." % self

    def __add__(self, other):
        class AutoClass(self, other):
            pass
        return AutoClass
        # Alternatively, to autogenerate the classname as well as the class:
        # return type(self.__name__ + other.__name__, (self, other), {})

    def unregister(self):
        # classregistry.unregister(self)
        print "Would unregister class %s now." % self

class MyObject:
    __metaclass__ = MyType


class NoneSample(MyObject):
    pass

# Will print "NoneType None"
print type(NoneSample), repr(NoneSample)

class Example(MyObject):
    def __init__(self, value):
        self.value = value
    @make_hook
    def add(self, other):
        return self.__class__(self.value + other.value)

# Will unregister the class
Example.unregister()

inst = Example(10)
# Will fail with an AttributeError
#inst.unregister()

print inst + inst
class Sibling(MyObject):
    pass

ExampleSibling = Example + Sibling
# ExampleSibling is now a subclass of both Example and Sibling (with no
# content of its own) although it will believe it's called 'AutoClass'
print ExampleSibling
print ExampleSibling.__mro__
```

### What does \_\_future\_\_ do?

Put simply, the \_\_future\_\_ statement forces Python interpreters to use newer features of the language.

\_\_future\_\_ is a pseudo-module which programmers can use to enable new language features which are not compatible with the current interpreter. For example, the expression 11/4 currently evaluates to 2. If the module in which it is executed had enabled true division by executing:

```python
from __future__ import division
```

the expression 11/4 would evaluate to 2.75. By importing the \_\_future\_\_ module and evaluating its variables, you can see when a new feature was first added to the language and when it will become the default:

```bash
  >>> import __future__
  >>> __future__.division
  _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)
```

