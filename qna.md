
## Questions and Answers

### Python Programming

#### Any Python Script can act like a Module. State if the statement is True or False?

true

#### Which of the following modules are used to deal with Data compression and archiving?

All

#### Which of the following methods of 'random' module is used to pick a single element, randomly, from a given list of elements?

Choice

#### Which of the following statement retreives names of all builtin objects?

import builtins; builtins.__dict__.keys()

#### Which of the following is not a way to import the module 'm1' or the functions 'f1' and 'f2' defined in it?

```
import f1, f2 from m1
```

#### In Python, which of the following files is mandatory to treat a folder as a package?

```
__init.py__
```

#### Which of the following module is not used for parsing command line arguments automatically?
cmdparse 

#### Which of the following expression can be used to check if the file 'C:\Sample.txt' exists and is also a regular file?
os.path.isfile(C:\Sample.txt)

#### Which of the following keyword is necessary in defining a generator function?
yield

#### Which methods are defined in an iterator class?



### Programming Question

```python
class A:
    x = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        A.x += 1

    def __init__(self):
        A.x += 1

    def displayCount(self):
        print('Count : %d' % A.x)

    def display(self):
        print('a :', self.a, ' b :', self.b)

a1 = A('George', 25000)
a2 = A('John', 30000)
a3 = A()
a1.display()
a2.display()
print(A.x)
```

#### Answer
Will print out an error.

### Programming Question

```python

class A:
    def __init__(self, x=5, y=4):
        self.x = x
        self.y = y

    def __str__(self):
        return 'A(x: {}, y: {})'.format(self.x, self.y)
        
    def __eq__(self, other):
        return self.x * self.y == other.x * other.y
     
def f1():
    a = A(12, 3)
    b = A(3, 12)
    if (a == b):
        print(b != a)
        print(a)

f1()
```

#### Answer

```python

False
A(x: 12, y: 3)

```

### Programming Question
```python
class class1:
    a = 1

    def f1(self):
        a = 2
        class1.a += 1
        print(class1.a, end=' ')
        print(a, end=' ')

class1().f1()
class1().f1()

```

#### Answer

```txt
2 2 3 2
```

#### What does seek method of a file object do?

Moves the current file position to a different location at a defined offset.

#### Which of the following syntax is used to name a grouped portion of a match?

?P<group_name>

[Match Objects](https://docs.python.org/2.0/lib/match-objects.html)

#### What does the match method of re module do?

it matches the pattern at any position of the string


#### What is the output of the expression re.split(r'[aeiou]', 'abcdefghij')?

['abcd', 'efgh', 'ij']

#### In a match found by a defined pattern, how to group various portions of a match

Using square brackets, []

#### Which of the following expression is used to compile the pattern p?

re.regex(p)

#### Which of the following methods of a match object, mo, is used to view the named group portions of match in the form of a dictionary

mo.groupdict()

#### Which of the following methods of a match object, mo, is used to view the grouped portions of match in the form of a tuple

mo.groups()

#### Python DB

![]()



