Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mytuple = (5,6,7)
>>> mytuple
(5, 6, 7)
>>> mytuple = ()
>>> mytuplr
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    mytuplr
NameError: name 'mytuplr' is not defined
>>> mytuple
()
>>> mytuple = (10,10,"INDIA")
>>> mytuple
(10, 10, 'INDIA')
>>> mytuple = ("INDIA",[1,2,3],(3,4,5))
>>> mytuple
('INDIA', [1, 2, 3], (3, 4, 5))
>>> mytuple = 1,2,3,"india"
>>> mytuple
(1, 2, 3, 'india')
>>> a,b,c,d = mytuple
>>> a
1
>>> b
2
>>> c
3
>>> d
'india'
>>> e
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> mytuple =(1)
>>> mytuple
1
>>> type(mytuple)
<class 'int'>
>>> mytuple=(1,)
>>> mytuple
(1,)
>>> type(mytuple)
<class 'tuple'>
>>> mytuple = 1,
>>> mytuple
(1,)
>>> mytuple =(10,11,12,13,14,15,16,17)
>>> mytuple
(10, 11, 12, 13, 14, 15, 16, 17)
>>> mytuple[0]
10
>>> mytuple[3,0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    mytuple[3,0]
TypeError: tuple indices must be integers or slices, not tuple
>>> mytuple(-7)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    mytuple(-7)
TypeError: 'tuple' object is not callable
>>> mytuple[-7]
11
>>> mytuple[1:5]
(11, 12, 13, 14)
>>> mytuple[:-3]
(10, 11, 12, 13, 14)
>>> mytuple[-3:]
(15, 16, 17)
>>> mytuple[2]=100
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    mytuple[2]=100
TypeError: 'tuple' object does not support item assignment
>>> mytuple1 = 10,11,12
>>> mytuple2 = 13,14,15
>>> mytuple3 = mytuple1+mytuple2
>>> mytuple3
(10, 11, 12, 13, 14, 15)
>>> del mytuple2
>>> mytuple2
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    mytuple2
NameError: name 'mytuple2' is not defined
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
