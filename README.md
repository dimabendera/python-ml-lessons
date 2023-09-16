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
#### Section 2: Strings
#### Section 3: Conditionals
#### Section 4: Lists
#### Section 5: Loops
#### Section 6: Functions
#### Section 7: File handling
- with open(filename) as textfile: ...
- file.read()
- Reading text files 
- Reading CSV files
- File handling flags (r, w, b, +)
- Writing to files



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



<h2> Конвертація  </h2>

notebbok в html
<code>
jupyter nbconvert --to html ./your_notebook.ipynb
</code>

