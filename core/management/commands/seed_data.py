from django.core.management.base import BaseCommand

from core.models import InterviewQuestion, PracticeQuestion, Question, Topic


CURRICULUM = [
    ('Basics', 'basics', 'Python fundamentals: syntax, variables, dynamic typing, built-in types, casting, operators, comments, and indentation.', [
        ('What is Python?', 'Python is a high-level, readable, interpreted programming language.', 'print("Hello, World!")'),
        ('What does dynamically typed mean?', 'Python determines types at runtime and a name can refer to values of different types.', 'value = 10\nvalue = "now a string"'),
        ('What is the difference between is and ==?', '== compares values; is checks whether two names refer to the same object. Use is None for None checks.', 'a = [1, 2]\nb = [1, 2]\nprint(a == b)\nprint(a is b)'),
        ('What are valid Python variable naming rules?', 'Names start with a letter or underscore, contain letters, numbers, and underscores, are case-sensitive, and cannot be keywords.', 'user_name = "Alice"\nMAX_LIMIT = 100'),
    ], [
        ('Swap two variables without a temporary variable.', 'Use tuple unpacking: left, right = right, left.'),
        ('Check whether a number is even with a bitwise operator.', 'The least significant bit of an even number is zero, so use number & 1.'),
        ('Explain mutable and immutable values.', 'Lists and dictionaries can change in place; strings, tuples, and integers cannot.'),
        ('What do bool("") and bool("False") return?', 'An empty string is falsey; every non-empty string is truthy.'),
    ], ['Why is bool a subclass of int?', 'What happens when a variable is used before assignment?', 'Why should you avoid naming a variable list or str?']),
    ('Control Flow', 'control-flow', 'Decision-making and repetition with if, elif, else, for, while, range, break, continue, and pass.', [
        ('How do if, elif, and else work?', 'Python tests conditions from top to bottom. The first true branch runs; else runs when none is true.', 'age = 20\nif age < 18:\n    label = "Minor"\nelif age < 60:\n    label = "Adult"\nelse:\n    label = "Senior"'),
        ('What is the difference between break, continue, and pass?', 'break exits a loop, continue skips an iteration, and pass intentionally does nothing.', 'for number in range(5):\n    if number == 2:\n        continue\n    if number == 4:\n        break\n    print(number)'),
    ], [('Print even numbers from 1 to 50.', 'Use range and an if condition with modulo.'), ('Reverse a number with while.', 'Take the last digit with % 10 and remove it with // 10.'), ('Print a triangle of stars.', 'Use an outer loop for rows and an inner loop for stars.'), ('When is pass useful?', 'Use it for an intentionally empty branch or placeholder.')], ['When should you choose while over for?', 'How does range save memory?', 'What does a loop else clause do?']),
    ('Functions', 'functions', 'Reusable behavior with def, return values, default and keyword arguments, args, kwargs, lambdas, recursion, scope, and closures.', [
        ('What are *args and **kwargs?', '*args collects extra positional arguments into a tuple; **kwargs collects extra keyword arguments into a dictionary.', 'def total(*args, **kwargs):\n    return sum(args) + kwargs.get("tax", 0)'),
        ('What is a closure?', 'A closure is an inner function that remembers values from its enclosing scope after the outer function returns.', 'def outer(message):\n    def inner():\n        return message\n    return inner'),
        ('Why are mutable default arguments dangerous?', 'Defaults are created once when the function is defined, so a mutable default can retain values between calls. Use None instead.', 'def add_item(item, items=None):\n    items = [] if items is None else items\n    items.append(item)\n    return items'),
    ], [('Add any number of values using *args.', 'Use sum(args).'), ('Write recursive Fibonacci.', 'Use base cases for 0 and 1.'), ('Create a running-counter closure.', 'Use nonlocal count inside the inner function.'), ('Compare lambda and def.', 'Lambda is a compact single-expression function; def is clearer for larger behavior.')], ['Explain local and global scope.', 'What must every recursive function have?', 'How do keyword arguments improve readability?']),
    ('Strings', 'strings', 'Text values, string methods, formatting, indexing, slicing, reversing, and string immutability.', [
        ('Why are strings immutable?', 'Strings cannot change in place. Operations that appear to modify one create a new string, making strings safe to share and hash.', 'text = "Python"\nreversed_text = text[::-1]'),
        ('What are common string formatting approaches?', 'F-strings are the modern preferred approach; str.format and percent formatting are also available.', 'name = "Alice"\nmessage = f"Hello, {name}"'),
    ], [('Check whether a string is a palindrome.', 'Compare it with its reversed form after normalizing case.'), ('Count vowels.', 'Iterate over lowercase characters and check membership in a vowel set.'), ('Reverse without slicing.', 'Iterate from the final index to the first.'), ('Check whether two strings are anagrams.', 'Normalize both and compare sorted characters or frequency dictionaries.')], ['How does string slicing work?', 'Why are strings hashable?', 'What is the difference between split and partition?']),
    ('Data Structures', 'data-structures', 'Lists, tuples, dictionaries, sets, frozensets, comprehensions, and shallow versus deep copying.', [
        ('Compare list, tuple, dictionary, and set.', 'Lists are ordered and mutable, tuples ordered and immutable, dictionaries map keys to values, and sets store unique values.', 'items = [1, 2]\npoint = (10, 20)\nuser = {"name": "A"}\nunique = {1, 2, 2}'),
        ('What is shallow versus deep copy?', 'A shallow copy duplicates the outer object but shares nested objects. A deep copy recursively duplicates nested objects.', 'import copy\nshallow = copy.copy(value)\ndeep = copy.deepcopy(value)'),
        ('Why cannot a list be a dictionary key?', 'Keys must be hashable and stable. Lists are mutable and unhashable; tuples can be keys when their contents are hashable.', 'lookup = {(10, 20): "point"}'),
    ], [('Find duplicate list elements.', 'Track seen values in a set.'), ('Merge dictionaries with overlapping keys.', 'Use unpacking or the | operator and decide which value wins.'), ('Find the intersection of two sets.', 'Use intersection or the & operator.'), ('Convert tuples into a dictionary.', 'Pass two-item tuples to dict.'), ('Build a comprehension.', 'Use {key: expression for item in iterable}.')], ['When would you use a tuple?', 'How do dictionaries achieve fast lookup?', 'What does hashable mean?']),
    ('Object-Oriented Programming', 'object-oriented-programming', 'Classes, objects, encapsulation, inheritance, polymorphism, abstraction, methods, MRO, operator overloading, and magic methods.', [
        ('What are the four pillars of OOP?', 'Encapsulation bundles data and behavior, inheritance reuses behavior, polymorphism supports different implementations, and abstraction hides detail.', 'from abc import ABC, abstractmethod\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass'),
        ('What are self and __init__?', 'self refers to the current instance. __init__ initializes that instance after creation.', 'class Dog:\n    def __init__(self, name):\n        self.name = name'),
        ('Compare instance, class, and static methods.', 'Instance methods receive self, class methods receive cls, and static methods receive neither automatically.', 'class User:\n    @classmethod\n    def guest(cls):\n        return cls()'),
        ('What is method resolution order?', 'MRO is the order Python follows to search classes for methods, especially with multiple inheritance.', 'print(MyClass.mro())'),
    ], [('Create an Employee with private salary and raise.', 'Use a name-mangled __salary attribute.'), ('Explain inheritance with a real-world example.', 'Use it only when the child truly is a kind of the parent.'), ('Overload the + operator.', 'Implement __add__ and return a compatible object.'), ('Create an abstract Shape.', 'Use ABC and @abstractmethod.')], ['Overloading versus overriding?', 'When is composition better than inheritance?', 'What are dunder methods?']),
    ('Exception Handling', 'exception-handling', 'Graceful errors with try, except, else, finally, raise, custom exceptions, and built-in exception types.', [
        ('How do try, except, else, and finally work?', 'try contains risky code, except handles selected errors, else runs on success, and finally always runs.', 'try:\n    result = int(value)\nexcept ValueError:\n    result = 0\nfinally:\n    print("done")'),
        ('When should you create a custom exception?', 'Create one when callers need to distinguish a meaningful domain failure from standard errors.', 'class InvalidAgeError(Exception):\n    pass'),
    ], [('Handle ValueError and ZeroDivisionError.', 'Use specific except clauses.'), ('Create InvalidAgeError.', 'Extend Exception and raise it for invalid ages.'), ('Handle FileNotFoundError.', 'Catch it and provide a useful fallback.'), ('Explain why bare except is bad.', 'It hides unexpected bugs and catches too broadly.')], ['Exception versus BaseException?', 'What if finally raises an exception?', 'Why should exceptions be specific?']),
    ('File Handling', 'file-handling', 'Reading and writing files safely with open, context managers, CSV, JSON, and cleanup behavior.', [
        ('Why is with open preferred?', 'The context manager closes the file automatically even if an exception occurs.', 'with open("file.txt", "r", encoding="utf-8") as file:\n    content = file.read()'),
        ('How do you work with JSON?', 'json.dumps and loads convert strings; json.dump and load work with files.', 'import json\ndata = {"name": "Alice"}\ntext = json.dumps(data)'),
    ], [('Count lines in a file.', 'Iterate over the file object.'), ('Read a JSON key safely.', 'Use dict.get when the key may be absent.'), ('Append text to a file.', 'Open with mode a.'), ('Handle a missing file.', 'Catch FileNotFoundError.')], ['What is a context manager?', 'Text versus binary file modes?', 'When is CSV preferable to JSON?']),
    ('Iterators and Generators', 'iterators-and-generators', 'The iterator protocol, generators, yield, generator expressions, lazy evaluation, and memory-efficient processing.', [
        ('What is an iterator?', 'An iterator produces values through __iter__ and __next__. Exhaustion raises StopIteration.', 'iterator = iter([1, 2])\nprint(next(iterator))'),
        ('What does yield do?', 'yield pauses a function and preserves state, turning it into a lazy generator.', 'def count_up_to(limit):\n    for number in range(1, limit + 1):\n        yield number'),
    ], [('Generate even numbers up to n.', 'Use range with a step of two and yield.'), ('Compare list and generator comprehensions.', 'Lists build immediately; generators are lazy.'), ('Build a custom iterator.', 'Implement __iter__ and __next__.'), ('Why do generators save memory?', 'They keep only current state.')], ['Iterable versus iterator?', 'What happens after generator exhaustion?', 'When should you avoid a generator?']),
    ('Functional Programming', 'functional-programming', 'map, filter, reduce, lambda functions, decorators, functools, caching, and partial application.', [
        ('What do map, filter, and reduce do?', 'map transforms, filter keeps matching items, and reduce combines values.', 'from functools import reduce\ndoubles = list(map(lambda x: x * 2, [1, 2, 3]))\ntotal = reduce(lambda a, b: a + b, [1, 2, 3])'),
        ('What is a decorator?', 'A decorator wraps a callable to add behavior without changing its core implementation.', 'def log_call(function):\n    def wrapper(*args, **kwargs):\n        print("called")\n        return function(*args, **kwargs)\n    return wrapper'),
        ('What is lru_cache useful for?', 'It caches results based on arguments, making repeated deterministic calls faster.', 'from functools import lru_cache\n@lru_cache\ndef fib(n):\n    return n if n < 2 else fib(n - 1) + fib(n - 2)'),
    ], [('Uppercase strings with map.', 'Pass str.upper to map.'), ('Keep odd numbers with filter.', 'Test number % 2 == 1.'), ('Write an execution-time decorator.', 'Use time.perf_counter and functools.wraps.'), ('Rewrite a loop with map.', 'Express the loop transformation as a function.')], ['Decorator versus higher-order function?', 'Why use functools.wraps?', 'When is a comprehension clearer?']),
    ('Modules and Packages', 'modules-and-packages', 'Reusable organization with modules, packages, imports, __init__.py, module search paths, and the main guard.', [
        ('Module versus package?', 'A module is one Python file. A package groups modules in a directory and commonly has __init__.py.', 'from pathlib import Path'),
        ('Why use the main guard?', 'It runs code only when a file is executed directly, not when imported.', 'if __name__ == "__main__":\n    main()'),
    ], [('Create and import a module.', 'Put a function in a .py file and import it.'), ('Explain __init__.py.', 'It initializes a package and can expose package APIs.'), ('Compare import forms.', 'Explicit module imports keep namespace clarity.'), ('Inspect module search paths.', 'Use sys.path.')], ['How does Python find imports?', 'What risks come with wildcard imports?', 'How do circular imports happen?']),
    ('Advanced Python', 'advanced-python', 'Memory management, garbage collection, GIL, threading, multiprocessing, async, metaclasses, monkey patching, slots, LEGB, serialization, regex, and type hints.', [
        ('What is the GIL?', 'In standard CPython, the Global Interpreter Lock allows one thread to execute Python bytecode at a time. Threads still help with I/O; processes help CPU work.', 'from threading import Thread\n# Threads are useful for I/O-bound work'),
        ('When choose threading, multiprocessing, or async?', 'Use threading for concurrent I/O with shared memory, multiprocessing for CPU-bound parallel work, and async for cooperative I/O.', 'import asyncio\nasync def greet():\n    await asyncio.sleep(1)\n    return "Hello"'),
        ('What is the LEGB rule?', 'Names are searched in Local, Enclosing, Global, then Built-in scopes.', 'value = "global"\ndef show():\n    value = "local"\n    return value'),
        ('Compare pickle and JSON.', 'pickle handles many Python objects but must not load untrusted data. JSON is portable text with fewer types.', 'import json\njson.dumps({"name": "Alice"})'),
        ('What are type hints?', 'Optional annotations document intended types and help tooling but are not enforced at runtime.', 'def add(a: int, b: int) -> int:\n    return a + b'),
    ], [('Explain the GIL.', 'One CPython thread executes bytecode at a time.'), ('Write a simple async function.', 'Use async def and await.'), ('Explain circular references.', 'The cyclic garbage collector can clean objects that reference one another.'), ('Use re to validate email.', 'Use a carefully chosen pattern and fullmatch.'), ('When does __slots__ help?', 'It can reduce per-instance memory by restricting attributes.')], ['How does garbage collection work?', 'What is a metaclass?', 'What is monkey patching?', 'How does async differ from threading?', 'What is serialization?']),
    ('Python Internals and Ecosystem', 'python-internals-and-ecosystem', 'CPython, alternative implementations, bytecode, PVM, virtual environments, pip, PEP 8, walrus operator, and Python 2 versus 3.', [
        ('What happens between source and execution?', 'CPython compiles source into bytecode, then the Python Virtual Machine executes it.', 'import dis\ndis.dis("x = 1")'),
        ('Why use virtual environments?', 'They isolate project dependencies so package versions do not conflict.', 'python -m venv .venv\npython -m pip install requests'),
        ('What is the walrus operator?', 'The := operator assigns a value inside an expression.', 'if (count := len(items)) > 0:\n    print(count)'),
    ], [('Compare CPython and PyPy.', 'CPython is the standard C implementation; PyPy uses a JIT.'), ('Explain PEP 8 naming.', 'Use readable lowercase snake_case and uppercase constants.'), ('Use the walrus operator in a loop.', 'Assign a value while testing it.'), ('Name Python 2/3 differences.', 'Print, division, and Unicode behavior changed.')], ['What is bytecode?', 'What does pip do?', 'How do lock files improve reproducibility?']),
    ('Testing and Best Practices', 'testing-and-best-practices', 'Unit testing with unittest or pytest, debugging, logging, assertions, fixtures, maintainability, and clean Python practices.', [
        ('Why is unit testing important?', 'Unit tests verify small behavior quickly, catch regressions, and make refactoring safer.', 'def add(a, b):\n    return a + b\n\ndef test_add():\n    assert add(2, 3) == 5'),
        ('Why use logging instead of print?', 'Logging supports levels, timestamps, handlers, formatting, and configurable destinations.', 'import logging\nlogging.basicConfig(level=logging.INFO)\nlogging.info("started")'),
    ], [('Write a pytest prime test.', 'Cover prime, composite, one, and negative values.'), ('Compare print debugging and logging.', 'Print is temporary; logging is structured and configurable.'), ('Explain fixtures.', 'Fixtures provide reusable setup and cleanup.'), ('Compare assert and raise.', 'Assert documents an invariant; raise is application control flow.')], ['How do you debug production issues?', 'What makes a unit test maintainable?', 'What is test isolation?']),
    ('Quick Revision', 'quick-revision', 'A rapid review of core types, functions, collections, OOP, exceptions, iterators, functional tools, internals, and testing.', [
        ('What is a generator?', 'A memory-efficient iterator produced by a function containing yield.', ''),
        ('What is the GIL?', 'A CPython lock that permits one thread to execute Python bytecode at a time.', ''),
        ('What is the LEGB rule?', 'The name lookup order is Local, Enclosing, Global, Built-in.', ''),
        ('What is a context manager?', 'An object that controls setup and cleanup around a with block.', ''),
        ('What is a decorator?', 'A callable that wraps another callable to add behavior.', ''),
        ('What is PEP 8?', 'Python’s style guide for readable, consistent code.', ''),
    ], [('Explain list, tuple, dict, and set in one minute.', 'Mention ordering, mutability, key-value lookup, and uniqueness.'), ('Explain is versus ==.', 'Use two separate lists with equal contents.'), ('Explain shallow versus deep copy.', 'Focus on whether nested objects are shared.'), ('Explain multiprocessing versus threading.', 'Contrast separate memory and CPU work with shared memory and I/O.')], ['Define dynamic typing.', 'Define encapsulation.', 'Define an iterator.', 'Define a context manager.', 'Define a virtual environment.']),
    ('Important Interview Questions', 'important-interview-questions', 'Final-round preparation covering conceptual, coding, tricky, and behavioral Python interview questions.', [
        ('Why does 0.1 + 0.2 not exactly equal 0.3?', 'Binary floating-point cannot represent many decimal fractions exactly, so stored approximations create a small precision difference.', 'print(0.1 + 0.2)'),
        ('What happens with a mutable default argument?', 'The default list is shared between calls because it is created when the function is defined.', 'def add(x, values=[]):\n    values.append(x)\n    return values'),
        ('How do you remove duplicates while preserving order?', 'Track seen values in a set and append an item only the first time it appears.', 'def unique(items):\n    seen = set()\n    result = []\n    for item in items:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result'),
        ('How would you optimize a slow Python script?', 'Measure with profiling first, improve the algorithm and data access, reduce unnecessary work, then consider caching or concurrency.', ''),
    ], [('Reverse a string without built-in reverse methods.', 'Iterate from the final character to the first.'), ('Find the second-largest number without sorting.', 'Track the largest and second-largest distinct values in one pass.'), ('Count word frequency.', 'Normalize words and accumulate counts in a dictionary or Counter.'), ('Write an execution-time decorator.', 'Use time.perf_counter and functools.wraps.'), ('Write a Fibonacci generator.', 'Yield successive values while updating two state variables.'), ('Flatten a nested list.', 'Use recursion or a stack.'), ('Implement an LRU cache.', 'Combine a dictionary with an ordered structure for recency.')], [
        'What is the difference between a list and a tuple?', 'What is the difference between is and ==?', 'Explain mutable versus immutable types.', 'What is the GIL?', 'Explain the four pillars of OOP.', 'Compare static, class, and instance methods.', 'What are decorators?', 'Compare deep and shallow copy.', 'How does garbage collection work?', 'What is a generator?', 'Reverse a string without reverse methods.', 'Find the second-largest number.', 'Check for a palindrome.', 'Remove duplicates preserving order.', 'Count word frequency.', 'Log execution time with a decorator.', 'Generate Fibonacci values.', 'Merge dictionaries with overlapping keys.', 'Implement an LRU cache.', 'Flatten a nested list.', 'Why does 0.1 + 0.2 differ from 0.3?', 'Explain mutable default arguments.', 'Why cannot lists be dictionary keys?', 'Why does True == 1?', 'How would you optimize a slow Python script?', 'When use multiprocessing over threading?', 'How investigate a memory leak?', 'How debug a production issue?', 'Describe effective OOP usage.', 'How communicate technical tradeoffs?',
    ]),
]


EXACT_TOPIC_NAMES = {
    'modules-and-packages': 'Modules & Packages',
    'data-structures': 'Data Structures (List, Tuple, Dict, Set)',
    'object-oriented-programming': 'Object-Oriented Programming (OOP)',
    'iterators-and-generators': 'Iterators & Generators',
    'functional-programming': 'Functional Programming (map/filter/reduce/decorators)',
    'advanced-python': 'Advanced Python (Memory, GIL, Threading, Async, Metaclasses)',
    'python-internals-and-ecosystem': 'Python Internals & Ecosystem',
    'testing-and-best-practices': 'Testing & Best Practices',
    'quick-revision': 'Quick Revision — All Concepts, Simple Definitions',
    'important-interview-questions': 'Important Interview Questions (Final Round Prep)',
}


EXACT_PRACTICE = {
    'basics': [
        ('What does "dynamically typed" mean in Python?', 'Think about when Python decides a value\'s type.'),
        ('What\'s the difference between int() and float() conversion?', 'Compare whole-number and decimal conversion.'),
        ('Write a program to swap two variables without a temp variable.', 'Use tuple unpacking.'),
        ('What happens if indentation is wrong in Python?', 'Python uses indentation to define blocks.'),
        ('Explain the difference between is and == with an example.', 'Compare object identity with value equality.'),
        ('What is the difference between mutable and immutable data types? Give 2 examples of each.', 'Lists are mutable; strings are immutable.'),
        ('Why is bool considered a subclass of int in Python? What does True + True return?', 'Check bool inheritance and numeric behavior.'),
        ('Difference between list, tuple, and set — when would you use each?', 'Compare order, mutability, and uniqueness.'),
        ('What\'s the difference between / and //? Give an example.', 'One performs true division; the other floors.'),
        ('Explain identity operators versus comparison operators.', 'Use is for identity and == for value.'),
        ('What\'s the difference between set and frozenset?', 'One is mutable and the other immutable.'),
        ('Write a program using bitwise operators to check if a number is even or odd.', 'Inspect the lowest bit with &.'),
        ('Why can frozenset be a dictionary key, but a list cannot?', 'Dictionary keys must be hashable.'),
        ('What does bool("") and bool("False") return, and why?', 'Empty strings are falsey; non-empty strings are truthy.'),
        ('What are the rules for naming a valid Python variable?', 'Check the first character, allowed characters, case, and keywords.'),
        ('What happens if you name a variable the same as a built-in function?', 'The built-in name becomes shadowed in that scope.'),
        ('What error do you get if you use a variable before assigning it?', 'The name is not defined yet.'),
    ],
    'control-flow': [
        ('Write a program to print all even numbers from 1–50 using a loop.', 'Use range and modulo.'),
        ('What\'s the difference between break and continue?', 'One exits the loop; the other skips an iteration.'),
        ('Write a program using while to reverse a number.', 'Use % 10 and // 10 repeatedly.'),
        ('When would you use pass in real code?', 'Use it as an intentional no-op or placeholder.'),
        ('Print a pattern (triangle of stars) using nested loops.', 'Use one loop for rows and one for columns.'),
    ],
    'functions': [
        ('Write a function using *args to add any number of numbers.', 'Use sum(args).'),
        ('What\'s the difference between a normal function and a lambda function?', 'Compare named multi-statement functions with single-expression functions.'),
        ('Write a recursive function to calculate Fibonacci numbers.', 'Use base cases and recursive calls.'),
        ('Explain mutable default arguments and give an example bug.', 'The default object is shared between calls.'),
        ('Write a closure that keeps a running counter each time it\'s called.', 'Use an enclosing count and nonlocal.'),
    ],
    'strings': [
        ('Write a program to check if a string is a palindrome.', 'Compare the string with its reverse.'),
        ('Count the number of vowels in a string.', 'Check each lowercase character against a vowel set.'),
        ('Reverse a string without using slicing.', 'Build the result character by character from the end.'),
        ('Check if two strings are anagrams of each other.', 'Compare normalized character frequencies.'),
        ('Explain why strings are immutable in Python.', 'String operations create new strings rather than modifying one in place.'),
    ],
    'data-structures': [
        ('Find duplicate elements in a list.', 'Track values already seen in a set.'),
        ('Merge two dictionaries in Python.', 'Use unpacking or the dictionary union operator.'),
        ('Write a program to find the intersection of two sets.', 'Use set intersection or &.'),
        ('Why can\'t you use a list as a dictionary key?', 'Lists are mutable and unhashable.'),
        ('Convert a list of tuples into a dictionary.', 'Use dict on two-item tuples.'),
    ],
    'object-oriented-programming': [
        ('Create a class Employee with encapsulated salary and a method to give a raise.', 'Use a private salary attribute and a method.'),
        ('Explain inheritance with a real-world example.', 'Describe a specialized child type reusing parent behavior.'),
        ('What\'s the difference between method overloading and method overriding?', 'Overriding replaces inherited behavior; Python does not use Java-style signature overloading.'),
        ('Write a class that overloads the + operator.', 'Implement __add__.'),
        ('What is an abstract class, and why would you use one?', 'Use ABC to define a required interface.'),
    ],
    'exception-handling': [
        ('Write code that handles both ValueError and ZeroDivisionError.', 'Catch the specific exception types.'),
        ('Create a custom exception for Invalid Age and raise it conditionally.', 'Subclass Exception and raise it for invalid input.'),
        ('What\'s the difference between Exception and BaseException?', 'BaseException also includes control-flow exceptions such as KeyboardInterrupt.'),
        ('What happens if an exception occurs inside a finally block?', 'The finally exception can replace the original exception.'),
        ('Explain why bare except is bad practice.', 'It hides unexpected failures.'),
    ],
    'file-handling': [
        ('Write code to count the number of lines in a text file.', 'Iterate over the file inside a with block.'),
        ('Read a JSON file and print a specific key value.', 'Use json.load and dictionary access.'),
        ('Why is with open preferred over manually calling open and close?', 'It guarantees cleanup.'),
        ('Write code to append text to an existing file.', 'Open with mode a.'),
        ('How would you handle FileNotFoundError gracefully?', 'Catch the specific exception and report a useful message.'),
    ],
    'iterators-and-generators': [
        ('Write a generator function that yields even numbers up to n.', 'Use yield with a range step of two.'),
        ('What\'s the difference between a list comprehension and a generator expression?', 'One builds immediately; the other is lazy.'),
        ('Why are generators more memory-efficient than lists?', 'They produce one value at a time.'),
        ('What happens when you call next on an exhausted generator?', 'It raises StopIteration.'),
        ('Build a custom iterator class using __iter__ and __next__.', 'Implement the iterator protocol.'),
    ],
    'functional-programming': [
        ('Use map to convert a list of strings to uppercase.', 'Map str.upper across the list.'),
        ('Use filter to get only odd numbers from a list.', 'Filter with number % 2 == 1.'),
        ('Write a decorator that logs how long a function takes to run.', 'Use time.perf_counter and functools.wraps.'),
        ('What is the benefit of lru_cache?', 'It caches repeated results for the same arguments.'),
        ('Rewrite a for loop using map and lambda.', 'Move the loop transformation into a lambda.'),
    ],
    'modules-and-packages': [
        ('What\'s the difference between a module and a package?', 'A module is a file; a package groups modules.'),
        ('Why do we use if __name__ == "__main__"?', 'It distinguishes direct execution from importing.'),
        ('What\'s the difference between import module and from module import x?', 'One keeps the module namespace; the other binds x directly.'),
        ('What is __init__.py used for?', 'It initializes a package and can expose its API.'),
        ('How does Python find modules when importing?', 'Inspect Python\'s module search path.'),
    ],
    'advanced-python': [
        ('Explain the GIL and its effect on multithreading.', 'One CPython thread executes Python bytecode at a time.'),
        ('When would you choose multiprocessing over threading?', 'Choose processes for CPU-bound parallel work.'),
        ('Write a simple async function using asyncio.', 'Use async def and await.'),
        ('What is a circular reference, and how does Python clean it up?', 'The cyclic garbage collector handles unreachable cycles.'),
        ('What\'s the difference between pickle and json?', 'Pickle is Python-specific and unsafe for untrusted data; JSON is portable text.'),
        ('Use re to validate an email format.', 'Compile a pattern and use fullmatch.'),
    ],
    'python-internals-and-ecosystem': [
        ('What\'s the difference between CPython and PyPy?', 'CPython is the standard C implementation; PyPy uses a JIT.'),
        ('Why do we use virtual environments?', 'They isolate project dependencies.'),
        ('What does PEP 8 recommend for naming variables?', 'Use readable lowercase snake_case names.'),
        ('Give an example of using the walrus operator in a loop.', 'Assign a value while testing it.'),
        ('Name two major differences between Python 2 and Python 3.', 'Print syntax, division, and Unicode behavior are examples.'),
    ],
    'testing-and-best-practices': [
        ('Write a simple pytest test for a function that checks if a number is prime.', 'Cover prime, composite, one, and negative values.'),
        ('What\'s the difference between print debugging and logging?', 'Logging is structured and configurable.'),
        ('Why is unit testing important in real projects?', 'It catches regressions and enables safer changes.'),
        ('What are test fixtures?', 'Reusable test setup and cleanup data.'),
        ('What\'s the difference between assert and raising an exception?', 'Assert checks an invariant; raise controls application behavior.'),
    ],
    'quick-revision': [],
    'important-interview-questions': [],
}


FINAL_INTERVIEW_QUESTIONS = [
    'What is the difference between a list and a tuple?',
    "What's the difference between is and ==?",
    'Explain mutable vs immutable data types with examples.',
    'What is the GIL, and how does it affect multithreading?',
    'Explain the four pillars of OOP with real examples.',
    'What is the difference between @staticmethod, @classmethod, and instance methods?',
    'What are decorators, and where have you used them?',
    "What's the difference between deep copy and shallow copy?",
    "Explain how Python's garbage collector works.",
    'What is a generator, and why would you use one over a list?',
    'Reverse a string without using built-in reverse methods.',
    'Find the second-largest number in a list without sorting.',
    'Check if a string is a palindrome.',
    'Remove duplicates from a list while preserving order.',
    'Write a program to count word frequency in a sentence.',
    'Implement a custom decorator that logs execution time.',
    'Write a generator to produce Fibonacci numbers.',
    'Merge two dictionaries and handle overlapping keys.',
    'Implement a basic LRU cache without using functools.',
    'Write code to flatten a nested list.',
    'Why does 0.1 + 0.2 != 0.3 in Python?',
    "What's the output of the mutable default argument example and why?",
    'Why can not lists be used as dictionary keys?',
    "What's the difference between == and .equals() in Python?",
    'Explain why True == 1 returns True in Python.',
    'How would you optimize a slow-running Python script?',
    'When would you use multiprocessing instead of multithreading?',
    'How do you handle memory leaks in Python caused by circular references?',
    "What's your approach to debugging a production issue in Python?",
    'Explain a real project where you used OOP principles effectively.',
]


SYLLABUS_DEFINITIONS = {
    'basics': [
        ('Variables & Dynamic Typing', 'A variable is a name that stores a value. Python figures out the type automatically, so a name can later refer to a different type.', 'x = 10\nx = "hi"'),
        ('Data Types', 'Python values include numeric types, strings, booleans, sequences, mappings, sets, None, and binary types. Values have types and may be mutable or immutable.', ''),
        ('int, float, and complex', 'int stores whole numbers, float stores decimal values, and complex stores real and imaginary parts using j.', 'age = 25\nprice = 19.99\nz = 3 + 4j'),
        ('str and bool', 'str is immutable text. bool has only True and False and is a subclass of int.', 'name = "Alice"\nis_active = True'),
        ('list, tuple, and range', 'A list is ordered and mutable, a tuple is ordered and immutable, and range represents a memory-efficient number sequence.', 'fruits = ["apple"]\npoint = (10, 20)\nr = range(0, 10, 2)'),
        ('dict, set, and frozenset', 'dict stores key-value pairs, set stores unique mutable values, and frozenset stores unique immutable values.', 'person = {"name": "Alice"}\nnums = {1, 2, 2}\nlocked = frozenset({1, 2})'),
        ('NoneType and binary types', 'NoneType represents no value. bytes and memoryview are immutable binary views while bytearray is mutable.', 'result = None\ndata = b"hello"'),
        ('Type Conversion (Casting)', 'Casting changes a value from one type to another with functions such as int, float, str, list, tuple, set, and bool.', 'int("5")\nfloat("3.1")\nlist("abc")'),
        ('Operators', 'Python provides arithmetic, comparison, logical, assignment, identity, membership, and bitwise operators.', '7 // 2\n5 in [1, 5, 9]\n5 & 3'),
        ('Comments & Indentation', 'Comments are notes ignored by Python. Indentation defines code blocks and four spaces is the standard.', '# comment\nif True:\n    print("Indented block")'),
    ],
    'control-flow': [
        ('if / elif / else', 'These statements let a program make decisions based on conditions.', 'if age < 18:\n    print("Minor")\nelif age < 60:\n    print("Adult")\nelse:\n    print("Senior")'),
        ('for loop & while loop', 'for repeats over a sequence; while repeats while a condition remains true.', 'for i in range(3):\n    print(i)\n\nn = 3\nwhile n > 0:\n    n -= 1'),
        ('break, continue, pass', 'break stops a loop, continue skips an iteration, and pass does nothing as a placeholder.', 'for i in range(5):\n    if i == 2: continue\n    if i == 4: break'),
        ('range()', 'range generates a sequence of numbers commonly used in loops.', 'list(range(2, 10, 2))'),
    ],
    'functions': [
        ('Defining Functions', 'A function is a reusable block of code called by name.', 'def greet(name):\n    return f"Hello, {name}"'),
        ('Default & Keyword Arguments', 'Default arguments provide a fallback value. Keyword arguments pass values by parameter name.', 'def greet(name, msg="Hi"):\n    return f"{msg}, {name}"'),
        ('*args and **kwargs', '*args collects extra positional values in a tuple and **kwargs collects extra named values in a dictionary.', 'def total(*args, **kwargs):\n    print(args, kwargs)'),
        ('Lambda Functions', 'A lambda is a short, unnamed, single-expression function.', 'square = lambda x: x * x'),
        ('Recursion', 'Recursion is when a function calls itself to solve a smaller version of the same problem.', 'def factorial(n):\n    if n == 1: return 1\n    return n * factorial(n - 1)'),
        ('Variable Scope', 'Local variables exist inside a function; global variables exist throughout the program.', 'x = "global"\ndef show():\n    x = "local"\n    print(x)'),
        ('Closures', 'A closure remembers values from where it was created even after the outer function finishes.', 'def outer(msg):\n    def inner(): print(msg)\n    return inner'),
    ],
    'strings': [
        ('String Basics & Methods', 'Strings are text data with methods such as lower, upper, split, and replace.', 's = "Hello World"\ns.lower()\ns.replace("World", "Python")'),
        ('String Formatting', 'Formatting inserts values into text. F-strings are the modern preferred form.', 'name = "Alice"\nf"Hello, {name}"'),
        ('String Slicing', 'Slicing extracts a portion of a string using index ranges.', 's = "Python"\ns[0:3]\ns[::-1]'),
    ],
    'data-structures': [
        ('Lists', 'A list is an ordered collection of items that can be changed.', 'fruits = ["apple", "banana"]\nfruits.append("cherry")'),
        ('Tuples', 'A tuple is an ordered collection of items that cannot be changed.', 'point = (10, 20)'),
        ('Dictionaries', 'A dictionary stores key-value pairs.', 'person = {"name": "Alice", "age": 30}\nperson.get("city", "N/A")'),
        ('Sets & Frozensets', 'A set contains unique items without a fixed order; a frozenset is immutable.', 'nums = {1, 2, 2}\nfrozen = frozenset({1, 2, 3})'),
        ('Comprehensions', 'A comprehension is a concise way to build a collection using an expression and loop.', 'squares = [x * x for x in range(5)]'),
        ('Shallow vs Deep Copy', 'A shallow copy shares nested objects; a deep copy recursively copies everything.', 'import copy\nshallow = copy.copy(a)\ndeep = copy.deepcopy(a)'),
    ],
    'object-oriented-programming': [
        ('Classes & Objects', 'A class is a blueprint; an object is a real instance built from that blueprint.', 'class Dog:\n    def __init__(self, name): self.name = name\nd = Dog("Rex")'),
        ('Encapsulation', 'Encapsulation bundles data and methods and hides internal details.', 'class Account:\n    def __init__(self): self.__balance = 0'),
        ('Inheritance', 'Inheritance lets a class reuse properties and methods from another class.', 'class Cat(Animal):\n    def speak(self): return "Meow"'),
        ('Polymorphism', 'Polymorphism lets the same method name behave differently for different objects.', 'for animal in [Animal(), Cat()]:\n    print(animal.speak())'),
        ('Abstraction', 'Abstraction hides complex details and exposes only what is necessary.', 'from abc import ABC, abstractmethod'),
        ('Dunder / Magic Methods', 'Special methods such as __str__ and __add__ connect custom objects to Python syntax.', 'class Point:\n    def __add__(self, other): return "Added!"'),
        ('Operator Overloading', 'Operator overloading redefines operators such as + or == using dunder methods.', 'def __add__(self, other):\n    return Point()'),
    ],
    'exception-handling': [
        ('try / except / else / finally', 'These clauses handle errors gracefully. else runs on success and finally always runs.', 'try:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print("Cannot divide")\nfinally:\n    print("Always")'),
        ('Raising Exceptions', 'raise manually triggers an exception.', 'raise ValueError("Invalid input")'),
        ('Custom Exceptions', 'A custom exception is a class created by inheriting from Exception.', 'class InsufficientFundsError(Exception):\n    pass'),
        ('Common Built-in Exceptions', 'Common built-ins include ValueError, TypeError, KeyError, IndexError, ZeroDivisionError, and FileNotFoundError.', ''),
    ],
    'file-handling': [
        ('Reading/Writing Files', 'Files can be opened to read or write data.', 'with open("file.txt", "w") as f:\n    f.write("Hello")'),
        ('Context Managers', 'The with statement handles setup and cleanup automatically, including closing files.', 'with open("file.txt") as f:\n    content = f.read()'),
        ('Working with CSV/JSON', 'Python provides csv and json modules for structured data.', 'import json\ndata = {"name": "Alice"}\njson.dumps(data)'),
    ],
    'iterators-and-generators': [
        ('Iterators', 'An iterator produces one item at a time through __iter__ and __next__.', 'iterator = iter([1, 2])\nnext(iterator)'),
        ('Generators', 'A generator builds an iterator with yield without storing all values in memory.', 'def count_up_to(n):\n    for i in range(n): yield i'),
        ('Generator Expressions', 'A generator expression uses parentheses and creates values lazily.', 'gen = (x * x for x in range(5))'),
    ],
    'functional-programming': [
        ('map(), filter(), reduce()', 'map applies a function, filter keeps matching values, and reduce combines values into one result.', 'list(map(lambda x: x * 2, [1, 2, 3]))'),
        ('Decorators with Arguments', 'A decorator factory accepts configuration and returns a decorator that wraps a function.', 'def repeat(times):\n    def decorator(func): return func\n    return decorator'),
        ('functools module', 'functools provides tools such as lru_cache for caching and partial for pre-filling arguments.', 'from functools import lru_cache'),
    ],
    'modules-and-packages': [
        ('Importing Modules', 'Importing reuses code from another file.', 'import math\nfrom math import sqrt'),
        ('Custom Modules/Packages', 'A module is one .py file; a package is a folder of modules with __init__.py.', ''),
        ('if __name__ == "__main__"', 'This block runs only when a file is executed directly, not when imported.', 'if __name__ == "__main__":\n    main()'),
    ],
    'advanced-python': [
        ('Memory Management & Garbage Collection', 'Python uses reference counting and a garbage collector for circular references.', 'import gc\ngc.collect()'),
        ('GIL', 'The Global Interpreter Lock allows only one thread to run Python code at a time in standard CPython.', ''),
        ('Multithreading vs Multiprocessing', 'Threading shares memory and suits I/O; multiprocessing uses separate memory and suits CPU-bound work.', ''),
        ('Async Programming (async/await)', 'Async code pauses while waiting and lets other tasks run without blocking on network operations.', 'async def greet():\n    await asyncio.sleep(1)'),
        ('Metaclasses', 'A metaclass is a class of a class and controls how classes are created.', ''),
        ('Monkey Patching', 'Monkey patching changes existing behavior at runtime without editing its source.', ''),
        ('__slots__', '__slots__ restricts allowed attributes and can save memory.', 'class User:\n    __slots__ = ("name",)'),
        ('Namespaces & LEGB Rule', 'Python searches Local, Enclosing, Global, then Built-in namespaces.', ''),
        ('Serialization', 'Serialization converts objects to a storable or transferable format and back.', 'import json\njson.dumps({"a": 1})'),
        ('Regular Expressions', 'The re module searches and matches patterns in text.', 'import re\nre.findall(r"\\d+", "2 cats")'),
        ('Type Hints / Annotations', 'Optional annotations describe intended types for readability and tooling.', 'def add(a: int, b: int) -> int:\n    return a + b'),
    ],
    'python-internals-and-ecosystem': [
        ('CPython vs Other Implementations', 'CPython is the common C implementation; PyPy is JIT-compiled and Jython runs on Java.', ''),
        ('Bytecode & PVM', 'Python source is compiled into bytecode and executed by the Python Virtual Machine.', ''),
        ('Virtual Environments & pip', 'A virtual environment isolates Python setup; pip installs packages from PyPI.', ''),
        ('PEP 8', 'PEP 8 is Python\'s official style guide.', ''),
        ('Walrus Operator (:=)', 'The walrus operator assigns a value inside an expression.', 'if (n := len([1, 2, 3])) > 2:\n    print(n)'),
        ('Python 2 vs Python 3', 'Python 3 is current and differs in print syntax, division behavior, and Unicode support.', ''),
    ],
    'testing-and-best-practices': [
        ('Unit Testing (unittest, pytest)', 'Unit tests check that individual pieces of code work correctly.', 'def test_add():\n    assert add(2, 3) == 5'),
        ('Debugging Techniques', 'Debugging finds and fixes bugs using print, pdb, or IDE breakpoints.', ''),
        ('Logging Module', 'The logging module records program execution in a configurable way.', 'import logging\nlogging.info("This is a log message")'),
    ],
}

SYLLABUS_DEFINITIONS['quick-revision'] = [
    ('Python', 'High-level, interpreted, easy-to-read language.', ''),
    ('Dynamic typing', 'Variable type is decided automatically at runtime.', ''),
    ('int/float/str/bool', 'Whole number / decimal / text / true-false.', ''),
    ('list', 'Ordered, changeable collection.', ''),
    ('tuple', 'Ordered, unchangeable collection.', ''),
    ('dict', 'Key-value pair collection.', ''),
    ('set', 'Collection of unique items with no guaranteed order.', ''),
    ('None', 'Represents nothing.', ''),
    ('is vs ==', 'Identity, or same object, versus value equality.', ''),
    ('*args/**kwargs', 'Extra positional and keyword arguments.', ''),
    ('lambda', 'One-line anonymous function.', ''),
    ('closure', 'Function remembering outer variables.', ''),
    ('decorator', 'Function that wraps another to add behavior.', ''),
    ('generator', 'Memory-efficient iterator using yield.', ''),
    ('iterator', 'Object you loop through one item at a time.', ''),
    ('list comprehension', 'One-line way to build a list from a loop.', ''),
    ('shallow copy', 'Copies the outer object but shares inner objects.', ''),
    ('deep copy', 'Fully independent copy including nested objects.', ''),
    ('class/object', 'Blueprint / actual thing built from that blueprint.', ''),
    ('self', 'Reference to the current object.', ''),
    ('__init__', 'Constructor that runs on object creation.', ''),
    ('encapsulation', 'Bundling and hiding data.', ''),
    ('inheritance', 'Child class reuses parent class code.', ''),
    ('polymorphism', 'Same method name with different behavior.', ''),
    ('abstraction', 'Hiding complexity and showing essentials.', ''),
    ('dunder methods', 'Special methods such as __str__ and __add__.', ''),
    ('MRO', 'Order Python searches classes for a method.', ''),
    ('try/except', 'Handling errors gracefully.', ''),
    ('custom exception', 'Your own error class.', ''),
    ('context manager', 'Automatic setup and cleanup with with.', ''),
    ('iterator protocol', '__iter__ plus __next__.', ''),
    ('map/filter/reduce', 'Transform / filter / combine collection items.', ''),
    ('module', 'A single .py file.', ''),
    ('package', 'Folder of modules with __init__.py.', ''),
    ('garbage collection', 'Automatic freeing of unused memory.', ''),
    ('GIL', 'Only one thread runs Python bytecode at a time in CPython.', ''),
    ('multiprocessing', 'True parallel execution using separate processes.', ''),
    ('async/await', 'Non-blocking code that pauses and resumes.', ''),
    ('metaclass', 'A class of a class.', ''),
    ('__slots__', 'Restrict attributes to save memory.', ''),
    ('LEGB rule', 'Local, Enclosing, Global, Built-in scope order.', ''),
    ('pickle/json', 'Convert Python objects to storable formats.', ''),
    ('regex', 'Pattern matching in text.', ''),
    ('type hints', 'Optional type annotations for clarity.', ''),
    ('PEP 8', 'Python\'s official style guide.', ''),
    ('virtual environment', 'Isolated Python setup.', ''),
    ('unit testing', 'Small tests that verify code correctness.', ''),
    ('logging', 'Structured way to record program events.', ''),
]


class Command(BaseCommand):
    help = 'Create or refresh the complete Python interview preparation curriculum.'

    def handle(self, *args, **options):
        for display_order, (name, slug, definition, questions, practice, interview) in enumerate(CURRICULUM, start=1):
            name = EXACT_TOPIC_NAMES.get(slug, name)
            practice = EXACT_PRACTICE[slug]
            interview = FINAL_INTERVIEW_QUESTIONS if slug == 'important-interview-questions' else []
            questions = questions + SYLLABUS_DEFINITIONS.get(slug, [])
            topic, _ = Topic.objects.update_or_create(
                slug=slug,
                defaults={'name': name, 'definition': definition, 'display_order': display_order},
            )
            topic.questions.all().delete()
            topic.practice_questions.all().delete()
            topic.interview_questions.all().delete()
            Question.objects.bulk_create([
                Question(topic=topic, question_text=text, answer_text=answer, code_example=code)
                for text, answer, code in questions
            ])
            PracticeQuestion.objects.bulk_create([
                PracticeQuestion(topic=topic, question_text=text, hint_text=hint)
                for text, hint in practice
            ])
            InterviewQuestion.objects.bulk_create([
                InterviewQuestion(topic=topic, question_text=text)
                for text in interview
            ])

        Topic.objects.exclude(slug__in=[item[1] for item in CURRICULUM]).delete()
        self.stdout.write(self.style.SUCCESS('Seeded the complete 16-section Python interview syllabus.'))
