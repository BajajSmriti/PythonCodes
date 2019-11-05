Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myset ={ 1,2,3,4,5,6}
>>> myset
{1, 2, 3, 4, 5, 6}
>>> myset ={1,2,(3,4,5),"accentuire"}
>>> .
SyntaxError: invalid syntax
>>> myset ={1,2,3,5,5,5}
>>> myset
{1, 2, 3, 5}
>>> myset =(1,2,[5,6])
>>> myset ={1,2,[5,6]}
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    myset ={1,2,[5,6]}
TypeError: unhashable type: 'list'
>>> myset ={}
>>> myset
{}
>>> type(myset)
<class 'dict'>
>>> myset = set({})
>>> type(myset)
<class 'set'>
>>> myset ={1,2,3}
>>> myset[0]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    myset[0]
TypeError: 'set' object does not support indexing
>>> myset
{1, 2, 3}
>>> myset.add(200)
>>> myset.update([70,80,90])
>>> myset
{1, 2, 3, 70, 200, 80, 90}
>>> myset.update([100,101],[102,103])
>>> myset
{1, 2, 3, 100, 101, 70, 102, 200, 103, 80, 90}
>>> myset.discard(90)
>>> myset
{1, 2, 3, 100, 101, 70, 102, 200, 103, 80}
>>> myset.pop()
1
>>> myset.clear()
>>> myset
set()
>>> myset.pop()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    myset.pop()
KeyError: 'pop from an empty set'
>>> myset.remove(100,101)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    myset.remove(100,101)
TypeError: remove() takes exactly one argument (2 given)
>>> setA = {1,2,3,4,5}
>>> setB = {4,5,6,7,8}
>>> setC = setA | setB
>>> setC
{1, 2, 3, 4, 5, 6, 7, 8}
>>> setD = setA.union(setB)
>>> setD
{1, 2, 3, 4, 5, 6, 7, 8}
>>> setC = setA & setB
>>> setC
{4, 5}
>>> setD =setA.intersection(setB)
>>> setD
{4, 5}
>>> set C = setA - setB
SyntaxError: invalid syntax
>>> setC = setA -setB
>>> setC
{1, 2, 3}
>>> setD = setA.symmetric_difference(setB)
>>> setD
{1, 2, 3, 6, 7, 8}
>>> help(set)
Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
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
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
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
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> mylist =['apple','orange','mango']
>>> for lst in mylist:
	print(lst)

	
apple
orange
mango
>>> mydict ={1:'pune',2:'nagpur','mumbai'}
SyntaxError: invalid syntax
>>> mydict ={1:'pune',2:'nagpur',3:'mumbai'}
>>> for lst in mydict:
	print(lst)

	
1
2
3
>>> print(mydict:lst)
SyntaxError: invalid syntax
>>>  for lst in mydict:
	print(mydict[lst])
	
SyntaxError: unexpected indent
>>> for lst in mydict:
	print(mydict[lst])

	
pune
nagpur
mumbai
>>> 
