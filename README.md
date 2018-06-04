
# Python Query Objects Lab

## Introduction

We have gotten pretty good at storing our instance objects and retrieving them using class variables and class methods. We've also basically mastered how to return our instance and class data in all kinds of fun ways and formats. So, now we are going to practice separating these two jobs. If we think about it, we will probably want to re-use a lot of these query methods like `sort_by` or `find_by` on more than just one class. So, instead of creating the same methods in multiple classes, we can define another class, `Query`, which will hold all these query methods and help clean up our other classes. Let's get started!

## Objectives
* Define a Query class and a Person class
* Define Query class methods that return information about a given class
* Import the Query class into other classes to utilize the query methods
* Define class methods that call the Query class from another class

## Define Our Classes

Okay, step one is to define our two initial classes. We will be working with a Person class and a Query class. Define these in the provided person.py and query.py files. We only need an `__init__` method for the Person class, and a person should be initialized with a `_name` and an `_age`. We also need the person class to keep track of all the people, or person instance objects as we like to call them. Let's save them in our `_all` class variable that points to a list and define a class method, `all` that returns the `_all` list.


```python
from person import Person
Person("Jeff", 31)
Person("Molly", 24)
Person("Kevin", 38)
Person("Rachel", 27)
Person("Devin", 25)
Person("Michelle", 33)
```


```python
from query import Query
```

## Define Our Class Methods 
Next, we want to define query class methods that return information about the person class. Below are a few class methods we can define in the Query class to operate on the person instance objects.  Each class method should accept another class as a parameter.  That way, we can pass the Person class into Query's class methods to operate on the Person class.


```python
Query.count(Person) 
# returns a number for the total count of person instances
```


```python
Query.find_by_name(Person, "Jeff") 
# returns first person instance object who's name is "Jeff"
```


```python
Query.name_starts_with(Person, "M") 
# returns a list of person instance objects whose name starts with the letter 'M'
```


```python
Query.is_older_than(Person, 30) 
# returns a list of person instance objects whose age is greater than 30
```


```python
Query.mean_age(Person) 
# returns the mean age of all person instance objects
```

## Importing The Query Class as a Module

Great! We defined a lot of exciting class methods and they are all working! But it seems a little weird that we are asking the Query class what the mean_age is, right? We understand what's happening but, maybe it would make more sense for us to ask the Person class what the mean age is?

```python
Person.mean_age()
```

Wow, yeah that seems to make a lot more sense. It is immediately more evident that we are asking the Person class what the mean age is for all person instance objects.

We still want to have our separation of concerns and keep the querying to the Query class, but we now want to define class methods in the Person class that call the Query class instead of the Query class being called directly. 

To accomplish this, we will need to do one more thing to set up our classes correctly. We need to import the Query class into our Person class.

```python 
from query import Query
```

To learn more about importing modules in Python, refer to the documentation [here.](https://docs.python.org/2/tutorial/modules.html)

## Using Query in Our Person Class

Great! Now define class methods on the Person class for `count`, `find_by_name`, `name_starts_with`, `is_older_than`, and `mean_age`. They should return the exact same values as the above class methods for the Query class, but they should simply call the corresponding Query class methods and return the result.


```python
Person.count() 
# returns a number for the total count of person instances

Person.find_by_name("Jeff") 
# returns first person instance object who's name is "Jeff"

Person.name_starts_with("M") 
# returns a list of person instance objects whose name starts with the letter 'M'

Person.is_older_than(30) 
# returns a list of person instance objects whose age is greater than 30

Person.mean_age() 
# returns the mean age of all person instance objects)
```

> **Note:** As we can see above, we no longer need to pass in a reference to the Person class in our arguments since we are using the Person class to call these methods. We will still need to pass those arguments into the Query class methods, however.

## Summary


In this lab, we practiced using a local class as a module to create a separation of concerns for our program. By defining a Query class that operates on our other class(es), we were able to make our code cleaner and [D.R.Y.](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)er. We can define our query methods in the Query class and import them into any other class we'd like instead of defining the same methods in each class we make. Great work! Feel free to continue practicing by defining other classes more methods to use with the Query class.
