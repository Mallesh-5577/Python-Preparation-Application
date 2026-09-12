# 🐍 Python Full Interview Preparation Guide

---

# 📑 INDEX

1. Basics
2. Control Flow
3. Functions
4. Strings
5. Data Structures (List, Tuple, Dict, Set)
6. Object-Oriented Programming (OOP)
7. Exception Handling
8. File Handling
9. Iterators & Generators
10. Functional Programming (map/filter/reduce/decorators)
11. Modules & Packages
12. Advanced Python (Memory, GIL, Threading, Async, Metaclasses)
13. Python Internals & Ecosystem
14. Testing & Best Practices
15. Quick Revision — All Concepts, Simple Definitions
16. Important Interview Questions (Final Round Prep)

---

# 1. BASICS

### What is Python?
**Simple definition:** Python is a high-level, easy-to-read, interpreted programming language. "Interpreted" means it runs code line-by-line instead of needing to compile the whole program first.
```python
print("Hello, World!")
```

### Variables & Dynamic Typing
**Simple definition:** A variable is a name that stores a value. Python figures out the type automatically — you never declare it.
```python
x = 10       # int
x = "hi"     # now a string — totally fine in Python
```

## Rules (Conditions) for Declaring Variables

### 1. Naming Rules (Must Follow — otherwise error)

- **Must start with a letter (a-z, A-Z) or an underscore (`_`)** — never a number.
```python
name = "Alice"     # valid
_name = "Alice"    # valid
1name = "Alice"    # SyntaxError
```

- **Can contain letters, numbers, and underscores only** — no spaces or special characters (`@`, `-`, `%`, etc.)
```python
user_name1 = "Bob"   # valid
user-name = "Bob"    # SyntaxError
user name = "Bob"    # SyntaxError
```

- **Case-sensitive** — `Name`, `name`, and `NAME` are three different variables.
```python
name = "Alice"
Name = "Bob"
print(name, Name)   # Alice Bob (different variables!)
```

- **Cannot be a Python reserved keyword** (`if`, `for`, `class`, `True`, `None`, `import`, etc.)
```python
class = "test"   # yntaxError — 'class' is a keyword
```
Check reserved keywords anytime with:
```python
import keyword
print(keyword.kwlist)
```

### 2. Best Practice Rules (Not enforced, but expected — PEP 8)

- Use **lowercase with underscores** for variable names: `user_age`, `total_price`
- Use **meaningful names**, not `x`, `y`, `a1` (unless in short loops/math)
- Constants are written in **ALL_CAPS**: `MAX_LIMIT = 100`
- Avoid starting with double underscore unless you specifically need name-mangling in classes (`__var`)

### 3. Other Important Conditions

- **No need to declare a type** — Python infers it automatically (dynamic typing).
```python
x = 10        # int
x = "hello"   # now string — totally allowed
```
- **Must be assigned a value before use**, or you'll get a `NameError`.
```python
print(y)   # NameError: name 'y' is not defined
y = 5
print(y)   # 5
```
- Variable names **can technically override built-in function names, but shouldn't** — this is a best-practice rule, not a hard error.
```python
list = [1, 2, 3]   # works, but now list() function is broken for rest of program
```

## Data Types
**Simple definition:** The different kinds of values Python can store — numbers, text, true/false, collections, etc. Every value in Python has a "type," and Python figures it out automatically.

Python data types are grouped into categories. Here's the full breakdown:

### 1. Numeric Types

**a) int (Integer)**
- Whole numbers, positive or negative, no decimal point.
- Python `int` has **no size limit** (unlike C/Java) — it can be as big as your memory allows.
```python
age = 25
big_number = 10 ** 100   # works fine, no overflow
```

**b) float (Floating Point)**
- Numbers with a decimal point.
- Based on IEEE 754 — can have small precision errors.
```python
price = 19.99
print(0.1 + 0.2)   # 0.30000000000000004 (precision quirk)
```

**c) complex**
- Numbers with a real and imaginary part, written with `j`.
- Rarely used outside scientific/engineering code.
```python
z = 3 + 4j
z.real   # 3.0
z.imag   # 4.0
```

### 2. Text Type

**str (String)**
- A sequence of characters (text), written in quotes (`'` or `"`).
- **Immutable** — once created, it can't be changed in place.
```python
name = "Alice"
name[0] = "M"   # TypeError — strings can't be modified
```

### 3. Boolean Type

**bool**
- Only two values: `True` or `False`.
- Important: `bool` is actually a **subclass of int** — `True` = 1, `False` = 0.
```python
is_active = True
True + True   # 2
```

### 4. Sequence Types

**a) list**
- Ordered, **changeable (mutable)** collection. Allows duplicates.
```python
fruits = ["apple", "banana", "apple"]
```

**b) tuple**
- Ordered, **unchangeable (immutable)** collection. Allows duplicates.
- Faster than lists and can be used as dictionary keys (since immutable).
```python
point = (10, 20)
```

**c) range**
- Represents a sequence of numbers, mainly used in loops. Memory-efficient (doesn't store all numbers at once).
```python
r = range(0, 10, 2)   # 0, 2, 4, 6, 8
```

### 5. Mapping Type

**dict (Dictionary)**
- Stores data as **key : value** pairs.
- Keys must be unique and immutable (hashable); values can be anything.
```python
person = {"name": "Alice", "age": 30}
```

### 6. Set Types

**a) set**
- Unordered collection of **unique** items (no duplicates).
- Useful for removing duplicates and fast membership checks.
```python
nums = {1, 2, 2, 3}   # {1, 2, 3}
```

**b) frozenset**
- Same as a set, but **immutable** (can't add/remove items after creation).
```python
locked = frozenset({1, 2, 3})
```

### 7. None Type

**NoneType**
- Represents "no value" or "nothing" — Python's version of null.
- There is only ONE `None` object in the whole program (a singleton) — always check it using `is None`, not `== None`.
```python
result = None
if result is None:
    print("No value yet")
```

### 8. Binary Types (good to know, less commonly asked)
- `bytes` — immutable sequence of bytes: `b"hello"`
- `bytearray` — mutable sequence of bytes
- `memoryview` — a view into another object's memory buffer without copying it

### Quick Summary Table

| Category | Types | Mutable? |
|---|---|---|
| Numeric | int, float, complex | No |
| Text | str | No |
| Boolean | bool | No |
| Sequence | list, tuple, range | list: Yes, others: No |
| Mapping | dict | Yes |
| Set | set, frozenset | set: Yes, frozenset: No |
| None | NoneType | No |
| Binary | bytes, bytearray, memoryview | bytearray: Yes, others: No |

---

## Type Conversion (Casting)
**Simple definition:** Changing a value from one data type to another.

- `int()` → converts to integer
- `float()` → converts to decimal
- `str()` → converts to text
- `list()` / `tuple()` / `set()` → convert between collection types
- `bool()` → converts to True/False

```python
int("5")        # 5
str(100)        # "100"
float("3.1")    # 3.1
list("abc")     # ['a', 'b', 'c']
bool(0)         # False
bool("hello")   # True (any non-empty string is True)
```

**Important gotcha:**
```python
int("3.5")           # ValueError — can't directly convert decimal string
int(float("3.5"))    # 3 — convert to float first, then int
```

---

## Operators
**Simple definition:** Symbols used to perform actions on values — math, comparisons, logic, and more.

### 1. Arithmetic Operators
- Used for mathematical calculations.
- `+` addition, `-` subtraction, `*` multiplication, `/` division (returns float)
- `//` floor division (rounds down, returns int-like result), `%` modulus (remainder), `**` exponent (power)
```python
7 + 3    # 10
7 / 2    # 3.5
7 // 2   # 3
7 % 2    # 1
2 ** 3   # 8
```

### 2. Comparison (Relational) Operators
- Compare two values, always return `True` or `False`.
- `==` equal to, `!=` not equal to, `>` greater than, `<` less than, `>=` greater or equal, `<=` less or equal
```python
5 == 5   # True
5 != 3   # True
5 > 3    # True
```

### 3. Logical Operators
- Combine multiple conditions.
- `and` → True only if BOTH are true
- `or` → True if AT LEAST ONE is true
- `not` → reverses the result
```python
True and False   # False
True or False    # True
not True         # False
```

### 4. Assignment Operators
- Assign values to variables, often combined with an operation.
- `=` assign, `+=` add and assign, `-=` subtract and assign, `*=`, `/=`, `//=`, `%=`, `**=`
```python
x = 5
x += 3    # x = x + 3 -> 8
x *= 2    # x = x * 2 -> 16
```

### 5. Identity Operators (important for interviews)
- Check if two variables point to the **same object in memory** (not just equal value).
- `is` → same object, `is not` → different objects
```python
a = [1, 2]
b = [1, 2]
a == b     # True (same values)
a is b     # False (different objects in memory)
```

### 6. Membership Operators (important for interviews)
- Check if a value exists inside a sequence (list, string, tuple, etc.)
- `in` → value is present, `not in` → value is absent
```python
5 in [1, 5, 9]        # True
"a" not in "python"   # True
```

### 7. Bitwise Operators (often asked in advanced rounds)
- Operate directly on the binary (bit-level) representation of numbers.
- `&` AND, `|` OR, `^` XOR, `~` NOT, `<<` left shift, `>>` right shift
```python
5 & 3    # 1  (0101 & 0011 = 0001)
5 | 3    # 7  (0101 | 0011 = 0111)
5 << 1   # 10 (shifts bits left, multiplies by 2)
```

### Quick Summary Table

| Operator Type | Examples | Purpose |
|---|---|---|
| Arithmetic | `+ - * / // % **` | Math calculations |
| Comparison | `== != > < >= <=` | Compare values |
| Logical | `and or not` | Combine conditions |
| Assignment | `= += -= *= /=` | Assign/update values |
| Identity | `is / is not` | Check same object in memory |
| Membership | `in / not in` | Check presence in a sequence |
| Bitwise | `& \| ^ ~ << >>` | Bit-level operations |

### Comments & Indentation
**Simple definition:** Comments (`#`) are notes for humans, ignored by Python. Indentation (spaces) defines code blocks — Python uses spacing instead of `{}`.
```python
# This is a comment
if True:
    print("Indented block")   # 4 spaces standard
```

### Practice Questions — Basics
1. What does "dynamically typed" mean in Python?
2. What's the difference between `int()` and `float()` conversion?
3. Write a program to swap two variables without a temp variable.
4. What happens if indentation is wrong in Python?
5. Explain the difference between `is` and `==` with an example.
6. What is the difference between mutable and immutable data types? Give 2 examples of each.
7. Why is `bool` considered a subclass of `int` in Python? What does `True + True` return?
8. Difference between `list`, `tuple`, and `set` — when would you use each?
9. What's the difference between `/` and `//`? Give an example.
10. Explain identity operators (`is`, `is not`) vs comparison operators (`==`, `!=`) with an example.
11. What's the difference between `set` and `frozenset`?
12. Write a program using bitwise operators to check if a number is even or odd.
13. Why can `frozenset` be used as a dictionary key, but a regular `list` cannot?
14. What does `bool("")` and `bool("False")` return, and why?
15. What are the rules for naming a valid Python variable? Give 2 examples of invalid names and explain why.
16. What happens if you name a variable the same as a built-in function like `list` or `str`?
17. What error do you get if you use a variable before assigning it a value?

---

# 2. CONTROL FLOW

### if / elif / else
**Simple definition:** Lets your program make decisions based on conditions.
```python
age = 20
if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

### for loop & while loop
**Simple definition:** `for` repeats over a known sequence (list, range). `while` repeats as long as a condition is true.
```python
for i in range(3):
    print(i)     # 0 1 2

n = 3
while n > 0:
    print(n)
    n -= 1
```

### break, continue, pass
**Simple definition:**
- `break` → stop the loop completely
- `continue` → skip this round, go to next
- `pass` → do nothing (placeholder)
```python
for i in range(5):
    if i == 2: continue
    if i == 4: break
    print(i)   # 0 1 3
```

### range()
**Simple definition:** Generates a sequence of numbers, commonly used in loops.
```python
list(range(2, 10, 2))   # [2, 4, 6, 8]
```

### 📝 Practice Questions — Control Flow
1. Write a program to print all even numbers from 1–50 using a loop.
2. What's the difference between `break` and `continue`?
3. Write a program using `while` to reverse a number.
4. When would you use `pass` in real code?
5. Print a pattern (triangle of stars) using nested loops.

---

# 3. FUNCTIONS

### Defining Functions
**Simple definition:** A reusable block of code you can call by name.
```python
def greet(name):
    return f"Hello, {name}"
```

### Default & Keyword Arguments
**Simple definition:** Default arguments have a preset value if none is given. Keyword arguments let you pass values by name, in any order.
```python
def greet(name, msg="Hi"):
    return f"{msg}, {name}"

greet("Alice")                 # Hi, Alice
greet(name="Bob", msg="Hey")   # Hey, Bob
```

### *args and **kwargs
**Simple definition:** Let a function accept any number of extra arguments. `*args` = extra positional values (tuple). `**kwargs` = extra named values (dict).
```python
def total(*args, **kwargs):
    print(args)      # (1, 2, 3)
    print(kwargs)    # {'tax': 5}

total(1, 2, 3, tax=5)
```

### Lambda Functions
**Simple definition:** A short, unnamed function written in a single line.
```python
square = lambda x: x * x
square(4)   # 16
```

### Recursion
**Simple definition:** A function that calls itself to solve a smaller version of the same problem.
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

### Variable Scope (Local/Global)
**Simple definition:** Local variables exist only inside a function. Global variables exist throughout the program.
```python
x = "global"
def show():
    x = "local"
    print(x)   # local
show()
print(x)       # global
```

### Closures
**Simple definition:** A function that remembers values from where it was created, even after that outer function finishes.
```python
def outer(msg):
    def inner():
        print(msg)
    return inner

hi = outer("Hello!")
hi()   # Hello!
```

### Practice Questions — Functions
1. Write a function using `*args` to add any number of numbers.
2. What's the difference between a normal function and a lambda function?
3. Write a recursive function to calculate Fibonacci numbers.
4. Explain what happens with mutable default arguments — give an example bug.
5. Write a closure that keeps a running counter each time it's called.

---

# 4. STRINGS

### String Basics & Methods
**Simple definition:** A string is text data. Python has built-in methods to manipulate it.
```python
s = "Hello World"
s.lower()      # 'hello world'
s.upper()      # 'HELLO WORLD'
s.split()      # ['Hello', 'World']
s.replace("World", "Python")  # 'Hello Python'
```

### String Formatting
**Simple definition:** Ways to insert variables into text.
```python
name = "Alice"
f"Hello, {name}"          # f-string (modern, preferred)
"Hello, {}".format(name)  # .format() method
```

### String Slicing
**Simple definition:** Extracting part of a string using index ranges.
```python
s = "Python"
s[0:3]    # 'Pyt'
s[-1]     # 'n'
s[::-1]   # 'nohtyP' (reversed)
```

### Practice Questions — Strings
1. Write a program to check if a string is a palindrome.
2. Count the number of vowels in a string.
3. Reverse a string without using slicing.
4. Check if two strings are anagrams of each other.
5. Explain why strings are immutable in Python.

---

# 5. DATA STRUCTURES

### Lists
**Simple definition:** An ordered collection of items you CAN change.
```python
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.remove("apple")
```

### Tuples
**Simple definition:** An ordered collection of items you CANNOT change.
```python
point = (10, 20)
```

### Dictionaries
**Simple definition:** Key-value pairs, like a real dictionary (word → meaning).
```python
person = {"name": "Alice", "age": 30}
person["age"]         # 30
person.get("city", "N/A")  # safe access with default
```

### Sets & Frozensets
**Simple definition:** A collection of unique items, no duplicates, no fixed order.
```python
nums = {1, 2, 2, 3}   # {1, 2, 3}
frozen = frozenset({1, 2, 3})  # unchangeable set
```

### Comprehensions
**Simple definition:** A short one-line way to build a list/dict/set using a loop.
```python
squares = [x*x for x in range(5)]
evens_dict = {x: x*x for x in range(3)}
```

### Shallow vs Deep Copy
**Simple definition:** Shallow copy copies the outer object but shares inner nested objects. Deep copy copies everything completely, independently.
```python
import copy
a = [[1,2],[3,4]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)
```

### Practice Questions — Data Structures
1. Find duplicate elements in a list.
2. Merge two dictionaries in Python.
3. Write a program to find the intersection of two sets.
4. Why can't you use a list as a dictionary key?
5. Convert a list of tuples into a dictionary.

---

# 6. OBJECT-ORIENTED PROGRAMMING (OOP)

### Classes & Objects
**Simple definition:** A class is a blueprint; an object is a real thing built from that blueprint.
```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} says Woof!"

d = Dog("Rex")
```

### self and __init__
**Simple definition:** `self` refers to the current object. `__init__` is the constructor — runs automatically when an object is created.

### Encapsulation
**Simple definition:** Bundling data + methods together, and hiding internal details using private variables.
```python
class Account:
    def __init__(self):
        self.__balance = 0   # private (name-mangled)
```

### Inheritance
**Simple definition:** A class can inherit properties/methods from another class.
```python
class Animal:
    def speak(self): return "Some sound"

class Cat(Animal):
    def speak(self): return "Meow"
```

### Polymorphism
**Simple definition:** The same method name behaves differently depending on the object.
```python
for a in [Animal(), Cat()]:
    print(a.speak())
```

### Abstraction
**Simple definition:** Hiding complex details, showing only what's necessary.
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

### Dunder / Magic Methods
**Simple definition:** Special methods (`__str__`, `__add__`) that let your objects work with built-in Python syntax.
```python
class Point:
    def __add__(self, other):
        return "Added!"
```

### Class Method vs Static Method vs Instance Method
**Simple definition:**
- Instance method → uses `self`, works on the object
- Class method → uses `cls`, works on the class
- Static method → doesn't use either, just a normal function grouped inside a class

### Method Resolution Order (MRO)
**Simple definition:** The order Python checks classes to find a method, in multiple inheritance.

### Operator Overloading
**Simple definition:** Redefining what operators like `+` or `==` do for your own custom objects (using dunder methods).

### Practice Questions — OOP
1. Create a class `Employee` with encapsulated salary, and a method to give a raise.
2. Explain inheritance with a real-world example (not code).
3. What's the difference between method overloading and method overriding?
4. Write a class that overloads the `+` operator.
5. What is an abstract class, and why would you use one?

---

# 7. EXCEPTION HANDLING

### try / except / else / finally
**Simple definition:** Lets your program handle errors gracefully instead of crashing.
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("Runs if no error")
finally:
    print("Always runs")
```

### Raising Exceptions
**Simple definition:** Manually triggering an error using `raise`.
```python
raise ValueError("Invalid input")
```

### Custom Exceptions
**Simple definition:** Your own exception classes, built by inheriting from `Exception`.
```python
class InsufficientFundsError(Exception):
    pass
```

### Common Built-in Exceptions
**Simple definition:** Errors Python already defines: `ValueError`, `TypeError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `FileNotFoundError`.

### Practice Questions — Exception Handling
1. Write code that handles both `ValueError` and `ZeroDivisionError`.
2. Create a custom exception for "Invalid Age" and raise it conditionally.
3. What's the difference between `Exception` and `BaseException`?
4. What happens if an exception occurs inside a `finally` block?
5. Explain why bare `except:` (no exception type) is bad practice.

---

# 8. FILE HANDLING

### Reading/Writing Files
**Simple definition:** Opening files to read data from or write data to them.
```python
with open("file.txt", "w") as f:
    f.write("Hello")

with open("file.txt", "r") as f:
    content = f.read()
```

### Context Managers (with statement)
**Simple definition:** Automatically handles setup/cleanup (like closing a file) even if errors occur.

### Working with CSV/JSON
**Simple definition:** Python has built-in modules (`csv`, `json`) to read/write structured data formats.
```python
import json
data = {"name": "Alice"}
json.dumps(data)     # convert dict to JSON string
json.loads('{"a":1}')  # convert JSON string to dict
```

### Practice Questions — File Handling
1. Write code to count the number of lines in a text file.
2. Write a Python program to read a JSON file and print a specific key's value.
3. Why is `with open()` preferred over manually calling `open()`/`close()`?
4. Write code to append text to an existing file.
5. How would you handle a `FileNotFoundError` gracefully?

---

# 9. ITERATORS & GENERATORS

### Iterators
**Simple definition:** An object you can loop through one item at a time, using `__iter__` and `__next__`.

### Generators
**Simple definition:** An easy way to build an iterator using `yield`, without storing everything in memory.
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

### Generator Expressions
**Simple definition:** Like a list comprehension, but with `()` instead of `[]` — creates a generator, not a full list.
```python
gen = (x*x for x in range(5))
```

### Practice Questions — Iterators & Generators
1. Write a generator function that yields even numbers up to n.
2. What's the difference between a list comprehension and a generator expression?
3. Why are generators more memory-efficient than lists?
4. What happens when you call `next()` on an exhausted generator?
5. Build a custom iterator class using `__iter__` and `__next__`.

---

# 10. FUNCTIONAL PROGRAMMING

### map(), filter(), reduce()
**Simple definition:**
- `map()` → applies a function to every item
- `filter()` → keeps only items matching a condition
- `reduce()` → combines all items into one value
```python
list(map(lambda x: x*2, [1,2,3]))       # [2,4,6]
list(filter(lambda x: x>1, [1,2,3]))    # [2,3]
from functools import reduce
reduce(lambda a,b: a+b, [1,2,3])        # 6
```

### Decorators
**Simple definition:** A function that wraps another function to add extra behavior.
```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def hello(): print("Hi")
```

### Decorators with Arguments
```python
def repeat(times):
    def decorator(func):
        def wrapper(*a, **kw):
            for _ in range(times): func(*a, **kw)
        return wrapper
    return decorator
```

### functools module
**Simple definition:** A module with handy tools like `lru_cache` (caching results) and `partial` (pre-filling function arguments).
```python
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n): return n if n<2 else fib(n-1)+fib(n-2)
```

### Practice Questions — Functional Programming
1. Use `map()` to convert a list of strings to uppercase.
2. Use `filter()` to get only odd numbers from a list.
3. Write a decorator that logs how long a function takes to run.
4. What's the benefit of `lru_cache`?
5. Rewrite a `for` loop using `map()` and `lambda`.

---

# 11. MODULES & PACKAGES

### Importing Modules
**Simple definition:** Reusing code from another file using `import`.
```python
import math
from math import sqrt
```

### Custom Modules/Packages
**Simple definition:** A module = one `.py` file. A package = a folder of modules with `__init__.py`.

### if __name__ == "__main__"
**Simple definition:** Code inside this block runs only when the file is executed directly, not when imported elsewhere.

### Practice Questions — Modules & Packages
1. What's the difference between a module and a package?
2. Why do we use `if __name__ == "__main__":`?
3. What's the difference between `import module` and `from module import x`?
4. What is `__init__.py` used for?
5. How does Python find modules when you `import` something (module search path)?

---

# 12. ADVANCED PYTHON

### Memory Management & Garbage Collection
**Simple definition:** Python automatically frees memory that's no longer used, using reference counting + a garbage collector for circular references.

### GIL (Global Interpreter Lock)
**Simple definition:** A lock that allows only one thread to run Python code at a time, even on multi-core machines.

### Multithreading vs Multiprocessing
**Simple definition:** Threading = multiple tasks sharing memory (good for I/O-bound work). Multiprocessing = separate processes with their own memory (good for CPU-bound work, true parallelism).

### Async Programming (async/await)
**Simple definition:** A way to write code that can pause and let other tasks run while waiting (e.g., for network calls), without using threads.
```python
import asyncio
async def greet():
    await asyncio.sleep(1)
    print("Hello")
```

### Metaclasses
**Simple definition:** A "class of a class" — controls how classes themselves are created.

### Monkey Patching
**Simple definition:** Changing or adding behavior to existing code at runtime, without editing its source.

### __slots__
**Simple definition:** Restricts a class to only specific attributes, saving memory.

### Namespaces & LEGB Rule
**Simple definition:** The order Python searches for a variable: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

### Serialization (pickle, json)
**Simple definition:** Converting Python objects into a storable/transferable format (bytes for pickle, text for JSON) and back.

### Regular Expressions (re module)
**Simple definition:** A way to search/match patterns in text.
```python
import re
re.findall(r'\d+', "I have 2 cats and 3 dogs")  # ['2', '3']
```

### Type Hints / Annotations
**Simple definition:** Optional hints about what type a variable/function should be, for readability and tooling (not enforced at runtime).
```python
def add(a: int, b: int) -> int:
    return a + b
```

### Practice Questions — Advanced Python
1. Explain the GIL and its effect on multithreading in simple terms.
2. When would you choose multiprocessing over threading?
3. Write a simple async function using `asyncio`.
4. What is a circular reference, and how does Python clean it up?
5. What's the difference between `pickle` and `json` for serialization?
6. Use the `re` module to validate an email format.

---

# 13. PYTHON INTERNALS & ECOSYSTEM

### CPython vs Other Implementations
**Simple definition:** CPython is the standard, most common Python implementation (written in C). Others include PyPy (faster, JIT-compiled) and Jython (runs on Java).

### Bytecode & PVM
**Simple definition:** Python code is compiled into bytecode (`.pyc`), then run by the Python Virtual Machine (PVM).

### Virtual Environments & pip
**Simple definition:** A virtual environment is an isolated Python setup per project. `pip` installs packages from PyPI.

### PEP 8
**Simple definition:** Python's official style guide for writing clean, readable code.

### Walrus Operator (:=)
**Simple definition:** Lets you assign a value inside an expression (Python 3.8+).
```python
if (n := len([1,2,3])) > 2:
    print(n)
```

### Python 2 vs Python 3
**Simple definition:** Python 3 is the current standard — key differences include `print` as a function, true division by default (`/`), and better Unicode support.

### Practice Questions — Internals & Ecosystem
1. What's the difference between CPython and PyPy?
2. Why do we use virtual environments?
3. What does PEP 8 recommend for naming variables?
4. Give an example of using the walrus operator in a loop.
5. Name two major differences between Python 2 and Python 3.

---

# 14. TESTING & BEST PRACTICES

### Unit Testing (unittest, pytest)
**Simple definition:** Writing small tests to check if individual pieces of your code work correctly.
```python
def add(a, b): return a + b

def test_add():
    assert add(2,3) == 5
```

### Debugging Techniques
**Simple definition:** Methods to find and fix bugs — using `print()`, Python's `pdb` debugger, or IDE breakpoints.

### Logging Module
**Simple definition:** A built-in way to record messages about your program's execution (better than using `print()` for real projects).
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is a log message")
```

### Practice Questions — Testing & Best Practices
1. Write a simple `pytest` test for a function that checks if a number is prime.
2. What's the difference between `print()` debugging and using the `logging` module?
3. Why is unit testing important in real projects?
4. What are test fixtures?
5. What's the difference between `assert` and raising an exception?

---

# 15. QUICK REVISION — ALL CONCEPTS, SIMPLE DEFINITIONS

| Concept | Simple Definition |
|---|---|
| Python | High-level, interpreted, easy-to-read language |
| Dynamic typing | Variable type decided automatically at runtime |
| int/float/str/bool | Whole number / decimal / text / true-false |
| list | Ordered, changeable collection |
| tuple | Ordered, unchangeable collection |
| dict | Key-value pair collection |
| set | Unique items, no order |
| None | Represents "nothing" |
| is vs == | Identity (same object) vs value equality |
| *args/**kwargs | Extra positional / keyword arguments |
| lambda | One-line anonymous function |
| closure | Function remembering outer variables |
| decorator | Function that wraps another to add behavior |
| generator | Memory-efficient iterator using `yield` |
| iterator | Object you loop through one item at a time |
| list comprehension | One-line way to build a list from a loop |
| shallow copy | Copies outer object, shares inner objects |
| deep copy | Fully independent copy |
| class/object | Blueprint / actual thing built from it |
| self | Reference to the current object |
| __init__ | Constructor, runs on object creation |
| encapsulation | Bundling + hiding data |
| inheritance | Child class reuses parent class code |
| polymorphism | Same method name, different behavior |
| abstraction | Hiding complexity, showing essentials |
| dunder methods | Special methods like `__str__`, `__add__` |
| MRO | Order Python searches classes for a method |
| try/except | Handling errors gracefully |
| custom exception | Your own error class |
| context manager | Auto setup/cleanup (`with` statement) |
| iterator protocol | `__iter__` + `__next__` |
| map/filter/reduce | Transform / filter / combine collection items |
| module | A single .py file |
| package | Folder of modules with `__init__.py` |
| garbage collection | Auto-freeing unused memory |
| GIL | Only one thread runs Python code at a time |
| multiprocessing | True parallel execution using separate processes |
| async/await | Non-blocking code that pauses and resumes |
| metaclass | A "class of a class" |
| __slots__ | Restrict attributes to save memory |
| LEGB rule | Local → Enclosing → Global → Built-in scope order |
| pickle/json | Convert Python objects to storable formats |
| regex | Pattern matching in text |
| type hints | Optional type annotations for clarity |
| PEP 8 | Python's official style guide |
| virtual environment | Isolated setup per project |
| unit testing | Small tests to verify code correctness |
| logging | Structured way to record program events |

---

# 16. IMPORTANT INTERVIEW QUESTIONS (FINAL PREP)

### Conceptual
1. What is the difference between a list and a tuple?
2. What's the difference between `is` and `==`?
3. Explain mutable vs immutable data types with examples.
4. What is the GIL, and how does it affect multithreading?
5. Explain the four pillars of OOP with real examples.
6. What is the difference between `@staticmethod`, `@classmethod`, and instance methods?
7. What are decorators, and where have you used them?
8. What's the difference between deep copy and shallow copy?
9. Explain how Python's garbage collector works.
10. What is a generator, and why would you use one over a list?

### Coding / Practical
11. Reverse a string without using built-in reverse methods.
12. Find the second-largest number in a list without sorting.
13. Check if a string is a palindrome.
14. Remove duplicates from a list while preserving order.
15. Write a program to count word frequency in a sentence.
16. Implement a custom decorator that logs execution time.
17. Write a generator to produce Fibonacci numbers.
18. Merge two dictionaries and handle overlapping keys.
19. Implement a basic LRU cache (without using `functools`).
20. Write code to flatten a nested list.

### Tricky / "Gotcha" Questions
21. Why does `0.1 + 0.2 != 0.3` in Python?
22. What's the output of this and why?
```python
def add(x, lst=[]):
    lst.append(x)
    return lst
print(add(1))
print(add(2))
```
23. Why can't lists be used as dictionary keys?
24. What's the difference between `==` and `.equals()` (trick — Python has no `.equals()`, unlike Java)?
25. Explain why `True == 1` returns `True` in Python.

### Behavioral / Conceptual Understanding
26. How would you optimize a slow-running Python script?
27. When would you use multiprocessing instead of multithreading?
28. How do you handle memory leaks in Python (circular references)?
29. What's your approach to debugging a production issue in Python?
30. Explain a real project where you used OOP principles effectively.

---
- Advanced topics (GIL, decorators, generators, memory management) are what set apart senior-level answers — expect these in later rounds.

Good luck! 💪
