Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myarray=[['blue','blue','red','red'],['true','false','true','false']]
>>> myarray
[['blue', 'blue', 'red', 'red'], ['true', 'false', 'true', 'false']]
>>> import pandas as pd
>>> import numpy as py
>>> myindex = pd.MultiIndex.from_arrays(myarray,names=['name1','name2'])
>>> myindex
MultiIndex(levels=[['blue', 'red'], ['false', 'true']],
           codes=[[0, 0, 1, 1], [1, 0, 1, 0]],
           names=['name1', 'name2'])
>>> myseries= ps.Series(np.random.randn(4),index=myindex)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    myseries= ps.Series(np.random.randn(4),index=myindex)
NameError: name 'ps' is not defined
>>> myseries= pd.Series(np.random.randn(4),index=myindex)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    myseries= pd.Series(np.random.randn(4),index=myindex)
NameError: name 'np' is not defined
>>> import numpy as np
>>> myseries= pd.Series(np.random.randn(4),index=myindex)
>>> myseries
name1  name2
blue   true    -1.743168
       false   -2.331646
red    true    -1.975513
       false    0.216436
dtype: float64
>>> myseries['blue']
name2
true    -1.743168
false   -2.331646
dtype: float64
>>> 

>>> 
=============================== RESTART: Shell ===============================
>>> pd.Series([1,2,])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pd.Series([1,2,])
NameError: name 'pd' is not defined
>>> import pandas as pd
>>> import numpy as np
>>> d={'ca':[1,2,3,4],'cb':[5,6,7,8]}
>>> df= pd.DataFrame(d)
>>> df
   ca  cb
0   1   5
1   2   6
2   3   7
3   4   8
>>> df['cb']
0    5
1    6
2    7
3    8
Name: cb, dtype: int64
>>> df[0]
Traceback (most recent call last):
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 2656, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    df[0]
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 2658, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0
>>> df['0']
Traceback (most recent call last):
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 2656, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: '0'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    df['0']
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 2658, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: '0'
>>> df.loc['0']
Traceback (most recent call last):
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 2656, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 129, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index_class_helper.pxi", line 91, in pandas._libs.index.Int64Engine._check_type
KeyError: '0'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    df.loc['0']
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexing.py", line 1500, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexing.py", line 1913, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexing.py", line 141, in _get_label
    return self.obj._xs(label, axis=axis)
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 3585, in xs
    loc = self.index.get_loc(key)
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 2658, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 129, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index_class_helper.pxi", line 91, in pandas._libs.index.Int64Engine._check_type
KeyError: '0'
>>> df.iloc[1]
ca    2
cb    6
Name: 1, dtype: int64
>>> type(_)
<class 'pandas.core.series.Series'>
>>> df[2:4]
   ca  cb
2   3   7
3   4   8
>>> df[2:3]
   ca  cb
2   3   7
>>> df
   ca  cb
0   1   5
1   2   6
2   3   7
3   4   8
>>> df['cnew']=df['cb']%2==0
>>> df
   ca  cb   cnew
0   1   5  False
1   2   6   True
2   3   7  False
3   4   8   True
>>> 
