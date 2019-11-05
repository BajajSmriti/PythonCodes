Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list = [1,2,(1,2,3),"monday"]
>>> list
[1, 2, (1, 2, 3), 'monday']
>>> list.append(501)
>>> list
[1, 2, (1, 2, 3), 'monday', 501]
>>> list1 = [601]
>>> list1
[601]
>>> list = list + list1
>>> list
[1, 2, (1, 2, 3), 'monday', 501, 601]
>>> list[3] =777
>>> list
[1, 2, (1, 2, 3), 777, 501, 601]
>>> for lst in list:
	print(lst)

	
1
2
(1, 2, 3)
777
501
601
>>> 101.201,777 = list[]
SyntaxError: invalid syntax
>>> mytuple list[-3::]
SyntaxError: invalid syntax
>>> mytuple = list[-3::]
>>> mytuple
[777, 501, 601]
>>> batches = {'java':34,'SAP':25,'Testing':30,'SOA':22}
>>> batches
{'java': 34, 'SAP': 25, 'Testing': 30, 'SOA': 22}
>>> batches.keys()
dict_keys(['java', 'SAP', 'Testing', 'SOA'])
>>> for kry in batches:
	print(batches[keys])

	
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    print(batches[keys])
NameError: name 'keys' is not defined
>>> for kry in batches:
	print(batches[kry])

	
34
25
30
22
>>> help(dictionary)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    help(dictionary)
NameError: name 'dictionary' is not defined
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if D has a key k, else False.
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
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> batches.get(keys)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    batches.get(keys)
NameError: name 'keys' is not defined
>>> help(tuple)
Help on class tuple in module builtins:

class tuple(object)
 |  tuple() -> empty tuple
 |  tuple(iterable) -> tuple initialized from iterable's items
 |  
 |  If the argument is a tuple, the return value is the same object.
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
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  count(...)
 |      T.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.

>>> 
================ RESTART: C:/python day 1/thriddayfunction.py ================
>>> 
================ RESTART: C:/python day 1/thriddayfunction.py ================
Hi,welcome to accenture
end of function
outside function
>>> 
================ RESTART: C:/python day 1/thriddayfunction.py ================
HiMandar,welcome to accenture
end of function
outside function
>>> 
================ RESTART: C:/python day 1/thriddayfunction.py ================
HiMandar,welcome to accenture
end of function
outside function
100
>>> 
================ RESTART: C:/python day 1/thriddayfunction.py ================
HiMandar,welcome to accenture
end of function
outside function
100
None
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Traceback (most recent call last):
  File "C:/python day 1/functions.py", line 15, in <module>
    printinfodefault()
TypeError: printinfodefault() missing 1 required positional argument: 'name'
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
Traceback (most recent call last):
  File "C:/python day 1/functions.py", line 43, in <module>
    list(filter(lambda x : x%3)==0,range(2,100))
TypeError: filter expected 2 arguments, got 1
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
Traceback (most recent call last):
  File "C:/python day 1/functions.py", line 43, in <module>
    list(filter(lambda x : x%3)==0,foo)
TypeError: filter expected 2 arguments, got 1
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
Traceback (most recent call last):
  File "C:/python day 1/functions.py", line 50, in <module>
    print_prams(x=1,y=2,z=1)
NameError: name 'print_prams' is not defined
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
Traceback (most recent call last):
  File "C:/python day 1/functions.py", line 50, in <module>
    print_params(x=1,y=2,z=1)
  File "C:/python day 1/functions.py", line 48, in print_params
    print(prams)
NameError: name 'prams' is not defined
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
{'x': 1, 'y': 2, 'z': 1}
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
{'x': 1, 'y': 2, 'z': 1}
Traceback (most recent call last):
  File "C:/python day 1/functions.py", line 61, in <module>
    print_mix_all(1,2,3,4,5,x=1,y=2)
TypeError: print_mix_all() got multiple values for argument 'x'
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
{'x': 1, 'y': 2, 'z': 1}
1 2
Traceback (most recent call last):
  File "C:/python day 1/functions.py", line 61, in <module>
    print_mix_all(1,2,3,4,5,a=1,b=2)
  File "C:/python day 1/functions.py", line 58, in print_mix_all
    print(pospr)
NameError: name 'pospr' is not defined
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
{'x': 1, 'y': 2, 'z': 1}
1 2
(3, 4, 5)
{'a': 1, 'b': 2}
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
{'x': 1, 'y': 2, 'z': 1}
1 2
(3, 4, 5)
{'a': 1, 'b': 2}
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
{'x': 1, 'y': 2, 'z': 1}
1 2
(3, 4, 5)
{'a': 1, 'b': 2}
{'a': 5}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/python day 1/functions.py', 'printinfo': <function printinfo at 0x000001F422B78A60>, 'printinfodefault': <function printinfodefault at 0x000001F422B78AE8>, 'printinfovariable': <function printinfovariable at 0x000001F422B78B70>, 'total': <function <lambda> at 0x000001F422B78BF8>, 'foo': [2, 3, 4, 5, 6, 22, 17, 12, 34], 'print_prm': <function print_prm at 0x000001F422B78C80>, 'print_mix_all': <function print_mix_all at 0x000001F422B78D08>, 'money': 2001, 'addmoney': <function addmoney at 0x000001F422B78D90>}
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
Name  Jack
Age  55
output is :
10
output is :
10
20
30
40
5
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
{'x': 1, 'y': 2, 'z': 1}
1 2
(3, 4, 5)
{'a': 1, 'b': 2}
{'a': 5}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/python day 1/functions.py', 'printinfo': <function printinfo at 0x00000229D00D8A60>, 'printinfodefault': <function printinfodefault at 0x00000229D00D8AE8>, 'printinfovariable': <function printinfovariable at 0x00000229D00D8B70>, 'total': <function <lambda> at 0x00000229D00D8BF8>, 'foo': [2, 3, 4, 5, 6, 22, 17, 12, 34], 'print_prm': <function print_prm at 0x00000229D00D8C80>, 'print_mix_all': <function print_mix_all at 0x00000229D00D8D08>, 'money': 2001, 'addmoney': <function addmoney at 0x00000229D00D8D90>}
>>> 
=================== RESTART: C:/python day 1/functions.py ===================
Name  Jack
Age  50
----------------------------------------------
Name  Jack
Age  55
----------------------------------------------
output is :
10
output is :
10
20
30
40
----------------------------------------------
5
----------------------------------------------
[4, 6, 8, 10, 12, 44, 34, 24, 68]
[3, 6, 12]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
----------------------------------------------
{'x': 1, 'y': 2, 'z': 1}
----------------------------------------------
1 2
(3, 4, 5)
{'a': 1, 'b': 2}
----------------------------------------------
{'a': 5}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/python day 1/functions.py', 'printinfo': <function printinfo at 0x0000026D1C228A60>, 'printinfodefault': <function printinfodefault at 0x0000026D1C228AE8>, 'printinfovariable': <function printinfovariable at 0x0000026D1C228B70>, 'total': <function <lambda> at 0x0000026D1C228BF8>, 'foo': [2, 3, 4, 5, 6, 22, 17, 12, 34], 'print_prm': <function print_prm at 0x0000026D1C228C80>, 'print_mix_all': <function print_mix_all at 0x0000026D1C228D08>, 'money': 2001, 'addmoney': <function addmoney at 0x0000026D1C228D90>}
----------------------------------------------
>>> 
===================== RESTART: C:/python day 1/words.py =====================
c
c++
python
.net
>>> 
===================== RESTART: C:/python day 1/words.py =====================
c
c++
python
.net
>>> 
===================== RESTART: C:/python day 1/words.py =====================
c
c++
python
.net
__main__
>>> import words
c
c++
python
.net
words
>>> 
===================== RESTART: C:/python day 1/words.py =====================
c
c++
python
.net
Traceback (most recent call last):
  File "C:/python day 1/words.py", line 11, in <module>
    if __name == '__main__':
NameError: name '__name' is not defined
>>> 
===================== RESTART: C:/python day 1/words.py =====================
c
c++
python
.net
__main__
>>> 
===================== RESTART: C:/python day 1/words.py =====================
c
c++
python
.net
__main__
>>> 
================= RESTART: C:/python day 1/words_cmd_arg.py =================
Traceback (most recent call last):
  File "C:/python day 1/words_cmd_arg.py", line 20, in <module>
    main(sys.argv[1])
IndexError: list index out of range
>>> import words_cmd_arg
>>> help(words_cmd_arg)
Help on module words_cmd_arg:

NAME
    words_cmd_arg - this modules handles command line arguments

FUNCTIONS
    main(argument)
    
    printwords(items)
        this function iterates using for
        args : it takes one arg
        return : nothing

FILE
    c:\python day 1\words_cmd_arg.py


>>> 
