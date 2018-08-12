### Descriptors

* Python descriptors allow a programmer to create managed attributes.
* In other object-oriented languages, you will find getter and setter methods to manage attributes.
* However, Python allows a programmer to manage the attributes simply with the attribute name, without losing their protection.
* This is achieved by defining a `descriptor` class, that implements any of **\_\_get\_\_, \_\_set\_\_, \_\_delete\_\_** methods.

```python
class EmpNameDescriptor:

    def __get__(self, obj, owner):
        return self.__empname

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value
```

* The descriptor, `EmpNameDescriptor` is defined to manage `empname` attribute.
* It checks if the value of `empname` attribute is a string or not.

```python
class EmpIdDescriptor:

    def __get__(self, obj, owner):
        return self.__empid

    def __set__(self, obj, value):
        if hasattr(obj, 'empid'):
            raise ValueError("'empid' is read only attribute")

        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")

        self.__empid = value
```
* The descriptor, `EmpIdDescriptor` is defined to manage `empid` attribute.

```python
class Employee:
    empid = EmpIdDescriptor()           
    empname = EmpNameDescriptor()       

    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
```

* `Employee` class is defined such that, it creates `empid` and `empname` attributes from descriptors `EmpIdDescriptor` and `EmpNameDescriptor`.

```python

e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)  

e1.empname = 'Williams'
print(e1.empid, '-', e1.empname)

e1.empid = 76347322  
```

* You can observe that accessing attributes `empid` and `empname` appear as if you are accessing them directly.
* However when executing the expression `e1.empid = 76347322`, the \_\_set\_\_ method defined in `EmpIdDescriptor` is executed and raises `"ValueError: 'empid'` is read only attribute".

#### Properties

* Descriptors can also be created using `property()` type.
* It is easy to create a descriptor for any attribute using `property()`.

##### Syntax of defining a Property

```python

property(fget=None, fset=None, fdel=None, doc=None)

# fget : attribute get method
# fset : attribute set method
# fdel : attribute delete method
# doc : docstring

```

##### Properties - Example

```python
class Employee:
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name

    def getEmpID(self):
        return self.__empid

    def setEmpID(self, value):
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value

    empid = property(getEmpID, setEmpID)
```

* `empid` attribute created using `property`.

```python
def getEmpName(self):
    return self.__empname

def setEmpName(self, value):
    if not isinstance(value, str):
        raise TypeError("empname' must be a string.")
    self.__empname = value

def delEmpName(self):
    del self.__empname

empname = property(getEmpName, setEmpName, delEmpName)
e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)    # -> '123456 - John'
del e1.empname    # Deletes 'empname'
print(e1.empname) #Raises 'AttributeError'    

```

* `empname` attribute created using `property`. It is deleted when `delEmpName` method is called.
* When `del e1.empname` is executed, it in turn calls `delEmpName` method.
* Hence accessing `empname` attribute after the `del` expression results in `AttributeError`.

##### Property Decorators

* Descriptors can also be created with property decorators.
* While using property decorators, an attribute's get method will be same as its name and will be decorated with property.
* In a case of defining any set or `delete` methods, they will be decorated with respective `setter` and `deleter` methods.

```python
class Employee:

    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name

    @property
    def empid(self):
        return self.__empid

    @empid.setter
    def empid(self, value):
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value

    @property
    def empname(self):
        return self.__empname

    @empname.setter
    def empname(self, value):
    if not isinstance(value, str):
        raise TypeError("'empname' must be a string.")
    self.__empname = value

    @empname.deleter
    def empname(self):
        del self.__empname

e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)    # -> '123456 - John'
del e1.empname    # Deletes 'empname'
print(e1.empname) #Raises 'AttributeError'
```

* `get` and `set` methods of `empid` attribute are decorated with property.
* `get`, `set`, and `del` methods of `empname` are decorated with property.
* `deleter` method corresponding to `empname` attribute is called when the expression, `del e1.empname` is executed.

