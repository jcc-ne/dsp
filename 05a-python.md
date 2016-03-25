# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> They are both sequence types.  The difference: tuples are immutable, lists are mutable (requires more memory).  Also tuples are generally heterogeneous (dealing with different kinds element) and lists are generally homogeneous.

>> Only tuples can work as keys in dict because dict only accept immutable types as keys.
---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> They are both sequence types.  The difference is, set does not contain duplicated elements. For example:

```
>>> list_a = ['a', 'c', 'c', 'f', 'f', 'h']
>>> set(list_a)

{'a', 'c', 'f', 'h'}
```

>> finding an element in a set is more efficient than in a list for large set of data because it sets up a hash table.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda functions are the anonymous functions created at runtime.

>> It is usually used in conjunction with functions like map, filter, sort.  For example:

```
>>> map(lambda x: x + 1, [1, 2, 3, 4])
[2, 3, 4, 5]

>>> filter(lambda x: x > 2, [1, 2, 3, 4])
[3, 4]

>>> list_a = [1, 2, 3, 4]
>>> list_a.sort(key=lambda x: -x)
>>> list_a
[4, 3, 2, 1]

```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>>  list comprehension is a quick way to create list from some operations.

>> For example, doubling each element, find even elements in a list...

```
list_a = [1, 2, 3, 4]

# list comprehension
[i * 2 for i in list_a]

# map
map(lambda x: x * 2, list_a)

# list comprehension
[i for i in list_a if i % 2 == 0]

# filter
filter(lambda x: x % 2 == 0, list_a)

```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





