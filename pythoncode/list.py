Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> 2*5
10
>>> y=20
>>> y
20
>>> 
>>> 

-
>>> _
20
>>> _*10
200
>>> print('welcome')
welcome
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
================== RESTART: C:/python day 1/firstprogram.py ==================
1+1
>>> type(10)
<class 'int'>
>>> type('a")
     
SyntaxError: EOL while scanning string literal
>>> type('accenture')
<class 'str'>
>>> type('100')
<class 'str'>
>>> type(100.5)
<class 'float'>
>>> mystr="Akshay's saving account"
>>> mystr
"Akshay's saving account"
>>> message = "please meet me at accenture"
>>> ivar = 100
>>> Message = "please meet me at accenture"
>>> Message = "please meet me at accenture"
>>> Message
'please meet me at accenture'
>>> message = 10
>>> message
10
>>> 59/60
0.9833333333333333
>>> "15"+2
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    "15"+2
TypeError: must be str, not int
>>> "accenture"+"15"
'accenture15'
>>> org_name = "accenture"
>>> location = "pune"
>>> print(org_name + location)
accenturepune
>>> "15"*3
'151515'
>>> "accenture" * 3
'accentureaccentureaccenture'
>>> yourname = input("enter your name: ")
enter your name: maddy
>>> print("your name is "+ yourname)
your name is maddy
>>> N = 7
>>> 7 + 5
12
>>> x=input()
7
>>> type(x)
<class 'str'>
>>> x=raw_input()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x=raw_input()
NameError: name 'raw_input' is not defined
>>> type(x)
<class 'str'>
>>> x=input()
'the knight who say "ni!"'
>>> x
'\'the knight who say "ni!"\''
>>> x = input()
7
>>> x= int(input("enter a number"))
enter a number 7
>>> type(x)
<class 'int'>
>>> x=input()
7
>>> str1 = "all"
>>> print(str1)
all
>>> str2 = "work"
>>> str3 = "and"
>>> str4 = "no"
>>> str5 = "play"
>>> print( str1 + str2 + str3 + str4 + str5 )
allworkandnoplay
>>> str1= "work "
>>> print( str1 +' ' str2 + str3 + str4 + str5 )
SyntaxError: invalid syntax
>>> ( str1 +' ' +str2 + str3 + str4 + str5 )
'work  workandnoplay'
\
>>> ( str1 +' '+str2 + str3 + str4 + str5 )
'work  workandnoplay'
>>> str1="all"
>>> print( str1 +' ' str2 + str3 + str4 + str5 )
SyntaxError: invalid syntax
>>> print( str1 +' '+ str2 + str3 + str4 + str5 )
all workandnoplay
>>> print( str1 +' '+str2 +' '+str3 +' '+ str4+' ' + str5 )
all work and no play
>>> ( str1 +' ' +str2 + str3 + str4 + str5 )
'all workandnoplay'
>>> 1 and 1
1
>>> a = 1
>>> b = 1
>>> a and b
1
>>> a nor b
SyntaxError: invalid syntax
>>> a == b
True
>>> a != b
False
>>> a <> b
SyntaxError: invalid syntax
>>> (a <> b)
SyntaxError: invalid syntax
>>> c = a + b
>>> c
2
>>> c+= a
>>> c
3
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> 
====================== RESTART: C:/python day2/day2.py ======================
it is 100
>>> 
====================== RESTART: C:/python day2/act2.py ======================
Traceback (most recent call last):
  File "C:/python day2/act2.py", line 6, in <module>
    7%0
ZeroDivisionError: integer division or modulo by zero
>>> 
====================== RESTART: C:/python day2/act2.py ======================
>>> 
====================== RESTART: C:/python day2/act2.py ======================
Traceback (most recent call last):
  File "C:/python day2/act2.py", line 6, in <module>
    if x<y:
NameError: name 'x' is not defined
>>> 
====================== RESTART: C:/python day2/act2.py ======================
Enter x8
Enter y9
x < y
>>> 
====================== RESTART: C:/python day2/act2.py ======================
Enter x9
Enter y9
x = y
>>> 
====================== RESTART: C:/python day2/act2.py ======================
The count is : 0
The count is : 1
The count is : 2
The count is : 3
The count is : 4
>>> 
====================== RESTART: C:/python day2/act2.py ======================
Current letter : P
Current letter : y
Current letter : t
Current letter : h
Current letter : o
Current letter : n
Traceback (most recent call last):
  File "C:/python day2/act2.py", line 26, in <module>
    print('Current fruit :',fruit)
NameError: name 'fruit' is not defined
>>> 
====================== RESTART: C:/python day2/act2.py ======================
Current letter : P
Current letter : y
Current letter : t
Current letter : h
Current letter : o
Current letter : n
Current fruit : banana
Current fruit : apple
Current fruit : mango
Good bye
>>> 
====================== RESTART: C:/python day2/act2.py ======================
Current letter : P  
Current letter : y  
Current letter : t  
Current letter : h  
Current letter : o  
Current letter : n  
Current fruit : banana
Current fruit : apple
Current fruit : mango
Good bye
>>> 
====================== RESTART: C:/python day2/act2.py ======================
Current letter : P Current letter : y Current letter : t Current letter : h Current letter : o Current letter : n Current fruit : banana
Current fruit : apple
Current fruit : mango
Good bye
>>> 
====================== RESTART: C:/python day2/act2.py ======================
P y t h o n Current fruit : banana
Current fruit : apple
Current fruit : mango
Good bye
>>> 
====================== RESTART: C:/python day2/act2.py ======================
PythonCurrent fruit : banana
Current fruit : apple
Current fruit : mango
Good bye
>>> 
====================== RESTART: C:/python day2/evan.py ======================

====================== RESTART: C:/python day2/evan.py ======================

====================== RESTART: C:/python day2/evan.py ======================
2
4
6
8
10
12
14
16
18
20
22
24
>>> 
====================== RESTART: C:/python day2/evan.py ======================
Traceback (most recent call last):
  File "C:/python day2/evan.py", line 9, in <module>
    for x in 25:
TypeError: 'int' object is not iterable
>>> 
====================== RESTART: C:/python day2/evan.py ======================
0
2
4
6
8
10
12
14
16
18
20
22
24
>>> 
====================== RESTART: C:/python day2/evan.py ======================
2
4
6
8
10
12
14
16
18
20
22
24
>>> 
======================= RESTART: C:/python day2/sqr.py =======================
Enter no
======================= RESTART: C:/python day2/sqr.py =======================
Enter no987
Traceback (most recent call last):
  File "C:/python day2/sqr.py", line 2, in <module>
    no1=x%10
TypeError: not all arguments converted during string formatting
>>> 
======================= RESTART: C:/python day2/sqr.py =======================
Enter no89
9
\
>>> 
======================= RESTART: C:/python day2/sqr.py =======================
Enter no98
Traceback (most recent call last):
  File "C:/python day2/sqr.py", line 3, in <module>
    x=x/10
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 
======================= RESTART: C:/python day2/sqr.py =======================
Enter no98
8
9.8
>>> 9%10
9
>>> 9/10
0.9
>>> 9.8/10
0.9800000000000001
>>> 
======================= RESTART: C:/python day2/sqr.py =======================
Enter no987
Traceback (most recent call last):
  File "C:/python day2/sqr.py", line 2, in <module>
    while(x>0):
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 
======================= RESTART: C:/python day2/sqr.py =======================
Enter no987
Traceback (most recent call last):
  File "C:/python day2/sqr.py", line 5, in <module>
    ans+=sq
NameError: name 'ans' is not defined
>>> 
======================= RESTART: C:/python day2/sqr.py =======================
Enter no987
Traceback (most recent call last):
  File "C:/python day2/sqr.py", line 5, in <module>
    ans=ans+sq
NameError: name 'ans' is not defined
>>> 
======================= RESTART: C:/python day2/sqr.py =======================
Enter no987
194
>>> 
====================== RESTART: C:/python day2/fact.py ======================
Enter no15
Traceback (most recent call last):
  File "C:/python day2/fact.py", line 5, in <module>
    x=x-1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
====================== RESTART: C:/python day2/fact.py ======================
Enter no90
Traceback (most recent call last):
  File "C:/python day2/fact.py", line 5, in <module>
    x=x-1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
====================== RESTART: C:/python day2/fact.py ======================
Enter no90
0
>>> 
====================== RESTART: C:/python day2/fact.py ======================
Enter no5
0
>>> 
====================== RESTART: C:/python day2/fact.py ======================
Enter no5
120
>>> """I work for
Acce
digital
in india
"""
'I work for\nAcce\ndigital\nin india\n'
>>> strva="we can \nembade multine \n strings"
>>> strva
'we can \nembade multine \n strings'
>>> print(strva)
we can 
embade multine 
 strings
>>> "double quote is \" and single is \'"
'double quote is " and single is \''
>>> k=\\
SyntaxError: unexpected character after line continuation character
>>> k="\\"
>>> k
'\\'
>>> print(k)
\
>>> raw=r"c:\hi\ki\"
SyntaxError: EOL while scanning string literal
>>> raw=r'c:\ji'
>>> raw
'c:\\ji'
>>> print(raw)
c:\ji
>>> str(496)
'496'
>>> str(8.02e26)
'8.02e+26'
>>> s='accenture'
>>> s[1]
'c'
>>> s[0]
'a'
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(...)
 |      S.__format__(format_spec) -> str
 |      
 |      Return a formatted version of S as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(...)
 |      S.capitalize() -> str
 |      
 |      Return a capitalized version of S, i.e. make the first character
 |      have upper case and the rest lower case.
 |  
 |  casefold(...)
 |      S.casefold() -> str
 |      
 |      Return a version of S suitable for caseless comparisons.
 |  
 |  center(...)
 |      S.center(width[, fillchar]) -> str
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(...)
 |      S.encode(encoding='utf-8', errors='strict') -> bytes
 |      
 |      Encode S using the codec registered for encoding. Default encoding
 |      is 'utf-8'. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(...)
 |      S.expandtabs(tabsize=8) -> str
 |      
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |  
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |  
 |  isdecimal(...)
 |      S.isdecimal() -> bool
 |      
 |      Return True if there are only decimal characters in S,
 |      False otherwise.
 |  
 |  isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |  
 |  isidentifier(...)
 |      S.isidentifier() -> bool
 |      
 |      Return True if S is a valid identifier according
 |      to the language definition.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers
 |      such as "def" and "class".
 |  
 |  islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  isnumeric(...)
 |      S.isnumeric() -> bool
 |      
 |      Return True if there are only numeric characters in S,
 |      False otherwise.
 |  
 |  isprintable(...)
 |      S.isprintable() -> bool
 |      
 |      Return True if all characters in S are considered
 |      printable in repr() or S is empty, False otherwise.
 |  
 |  isspace(...)
 |      S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |  
 |  istitle(...)
 |      S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
 |  
 |  isupper(...)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  join(...)
 |      S.join(iterable) -> str
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |  
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> str
 |      
 |      Return S left-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  lower(...)
 |      S.lower() -> str
 |      
 |      Return a copy of the string S converted to lowercase.
 |  
 |  lstrip(...)
 |      S.lstrip([chars]) -> str
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
 |  replace(...)
 |      S.replace(old, new[, count]) -> str
 |      
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> str
 |      
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  rpartition(...)
 |      S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
 |  
 |  rsplit(...)
 |      S.rsplit(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string, starting at the end of the string and
 |      working to the front.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified, any whitespace string
 |      is a separator.
 |  
 |  rstrip(...)
 |      S.rstrip([chars]) -> str
 |      
 |      Return a copy of the string S with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(...)
 |      S.split(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are
 |      removed from the result.
 |  
 |  splitlines(...)
 |      S.splitlines([keepends]) -> list of strings
 |      
 |      Return a list of the lines in S, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(...)
 |      S.strip([chars]) -> str
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(...)
 |      S.swapcase() -> str
 |      
 |      Return a copy of S with uppercase characters converted to lowercase
 |      and vice versa.
 |  
 |  title(...)
 |      S.title() -> str
 |      
 |      Return a titlecased version of S, i.e. words start with title case
 |      characters, all remaining cased characters have lower case.
 |  
 |  translate(...)
 |      S.translate(table) -> str
 |      
 |      Return a copy of the string S in which each character has been mapped
 |      through the given translation table. The table must implement
 |      lookup/indexing via __getitem__, for instance a dictionary or list,
 |      mapping Unicode ordinals to Unicode ordinals, strings, or None. If
 |      this operation raises LookupError, the character is left untouched.
 |      Characters mapped to None are deleted.
 |  
 |  upper(...)
 |      S.upper() -> str
 |      
 |      Return a copy of S converted to uppercase.
 |  
 |  zfill(...)
 |      S.zfill(width) -> str
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width. The string S is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> s.capitalize()
'Accenture'
>>> s[2]='c'
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s[2]='c'
TypeError: 'str' object does not support item assignment
>>> a='try all is this'
>>> a='this is {1} all is {2} this {3}'
>>> a.format("10","100","200")
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.format("10","100","200")
IndexError: tuple index out of range
>>> a.format(100,20,10)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a.format(100,20,10)
IndexError: tuple index out of range
>>> a.format("a","al","c")
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a.format("a","al","c")
IndexError: tuple index out of range
>>> a.format('a','g','v')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.format('a','g','v')
IndexError: tuple index out of range
>>> a.format(1,10,200)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.format(1,10,200)
IndexError: tuple index out of range
>>> '\u00e5ccenture'
'åccenture'
>>> '\xe5'
'å'
>>> '\345'
'å'
>>> str1='\u00e5ccenture'
>>> type(str1)
<class 'str'>
>>> 
=============================== RESTART: Shell ===============================
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> a=[1,2,3]
>>> a
[1, 2, 3]
>>> a=[1,"abc",2]
>>> a
[1, 'abc', 2]
>>> a[1]
'abc'
>>> a[0]
1
>>> len(a)
3
>>> a[0]=3
>>> a
[3, 'abc', 2]
>>> a=[[a,2],3,[4,5]]
>>> a
[[[3, 'abc', 2], 2], 3, [4, 5]]
>>> 3 in a
True
>>> a[0][0]
[3, 'abc', 2]
>>> 4 in a
False
>>> b=[7,8,[9,10]]
>>> a+b
[[[3, 'abc', 2], 2], 3, [4, 5], 7, 8, [9, 10]]
>>> a=a+[100]
>>> a
[[[3, 'abc', 2], 2], 3, [4, 5], 100]
>>> a.append(400)
>>> a
[[[3, 'abc', 2], 2], 3, [4, 5], 100, 400]
>>> a.insert(3,600)
>>> a
[[[3, 'abc', 2], 2], 3, [4, 5], 600, 100, 400]
>>> a.pop()
400
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    a.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> a.remove(1)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
>>> a.remove(100)
>>> a
[[[3, 'abc', 2], 2], 3, [4, 5], 600]
>>> a.index(600)
3
>>> a.reverse
<built-in method reverse of list object at 0x00000200C718CF48>
>>> a.reverse()
>>> a
[600, [4, 5], 3, [[3, 'abc', 2], 2]]
>>> b=[8,89,0]
>>> b.sort()
>>> b
[0, 8, 89]
>>> b.clear()
>>> b
[]
>>> mylist=['I','N','D','I','A']

>>> mylist[-1]
'A'
>>> mylist[-2]
'I'
>>> mylist
['I', 'N', 'D', 'I', 'A']
>>> mylist[2:5]
['D', 'I', 'A']
>>> mylist[:2]
['I', 'N']
>>> mylist[:-2]
['I', 'N', 'D']
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
