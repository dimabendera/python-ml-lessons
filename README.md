<h1> Лекції python </h1>

<h2> План лекцій</h2>

Основа взята з <a src="https://docs.google.com/document/d/1SgVPHOoGtm_hdNZP5YL_zCDlT11F-SY0_fnqGdfj2-U/edit">документу</a>

<ul>
  <li type="I">Введення. Короткі тести, сесії запитань і відповідей [3 год]
    <ol>
      <li type="1">Визначення цілей, відповідальності;</li>
      <li type="1">Хід розробки, вимоги до продукту, робота в команді, відстеження завдань, таймінг;</li>
      <li type="1">Основи Git, розміщення репозиторіїв (GitHub, GitLab);</li>
      <li type="1">IDE, Установка python, bash (Домашне завдання встановити python, встановити IDE)</li>
    </ol>
  </li>

  <li type="I">Лекція 1. Python. [8h].
    #### Section 1: General Programming Basics
- Simple Math
- Variable Assignment
- Basic Syntax and Logic
- Data Types: int, float, bool, str

#### Section 2: Strings
- Identifying and using strings
- String slicing
- String formatting
- String methods
- - str.replace()
- - str.find()
- - str.count()
- - str.lower()

#### Section 3: Conditionals
- Logical control; changing the behavior of your programs
- and keyword, or keyword
- if / else structure
- if / elif ... / else structure
- Nesting conditionals

#### Section 4: Lists
- Containers for data types
- First In, Last Out (Stack)
- Accessing specific list items through index (slice notation)
- List methods
- - list.append()
- - list.insert()
- - list.pop()
- - list.extend()
- Finding items in list (in keyword)
- Deduplicating a list using list(set(list_to_deduplicate))

#### Section 5: Loops
- for loop (for each item in a list: ...)
- enumerate()
- zip()
- range()
- while loop (ask each time: is this still true?)

#### Section 6: Strings to Lists and Vice-Versa
- str.join() (create a string from a list)
- str.split() (create a list from a string)

#### Section 7: File handling
- with open(filename) as textfile: ...
- file.read()
- Reading text files 
- Reading CSV files
- File handling flags (r, w, b, +)
- Writing to files

#### Section 8: Python's Most Commonly Used Built-in Functions
- - Types (used primarily for converting one type to another)
- int()
- float()
- str()
- bool()
- list()
- set()
- dict()
- - Comparison and Calculation
- abs()
- len()
- max()
- min()
- round()
- sum()
- - Loop (Sequence) Control
- enumerate()
- range() / xrange()
- reversed()
- sorted()
- zip()

#### Section 9: Functions
- def keyword
- arguments
- default arguments
- *args
- **kwargs
- return keyword
- sequence unpacking (return and receive multiple values)
- namespaces

#### Section 10: Dictionaries
- Accessing specific dictionary items through key (looks like a slice)
- Accessing all keys as a list using .keys()
- Faking a sorted dictionary by using sorted() on the .keys()
- Accessing all values as a list using .values()
- Accessing all key, value pairs as a list using .items()
- Adding new items through .fromkeys()
- Checking for whether a key exists with .has_key
- Using .get() to safely get a key's value if it exists without getting an error if not
- Adding new items with direct assignment and .update()

#### Section 11: Dictionaries and Lists, together
- Accessing specific items in a nested list
- Accessing specific items in a nested dictionary
- Accessing specific items in a nested list within a dictionary
- Accessing specific items in a nested dictionary within a list
- If you can do those four above, you can handle receiving JSON API returns

#### Section 12: Standard Library
- import keyword
- from ... import ... as ... structure
- time
- random
- math
- re (regular expressions)
- os
- sys
- json

#### Section 13: External Libraries (Not necessarily in order; keep these in mind)
- Installing external libraries with easy_install
- Using easy_install to install pip (an easier / better way to install external libraries)
- requests (web crawling made easy)
- BeautifulSoup (parsing HTML)
- xlrd (Read Excel .xls files)
- xlwt (Write to Excel .xls files)
- xlsxwriter (Write to Excel .xls and .xlsx files, with additional functionality beyond xlwt)
- cherrypy (Simple, lightweight framework for serving web pages)
- psycopg2 (Connect to and issue SQL commands to your postgresql database)

#### Section 14: Exception Handling
- try / except syntax
- Using multiple excepts
- Recognizing the different error types
- Exception, the generic exception type (use sparingly)
- Nesting exception handling
- try / except / else syntax

#### Section 15: Intermediate Concepts
- List Comprehensions
- Inline Conditionals
- Generators

#### Section 16: Classes
- Classes
- Magic Methods

  </li>
    

  
</ul>


<h2>джерела</h2>
* https://github.com/microsoft/ML-For-Beginners
* https://github.com/microsoft/Data-Science-For-Beginners
* https://github.com/GnuriaN/Python-Roadmap
* https://github.com/Moataz-Elmesmary/Data-Science-Roadmap
* https://github.com/mrankitgupta/Python-Roadmap
* https://github.com/matyushkin/lessons
* http://www.mmf.lnu.edu.ua/ar/1739



<h2> Конвертація в html </h2>

<code>
jupyter nbconvert --to html ./your_notebook.ipynb
</code>