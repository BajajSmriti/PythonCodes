Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> pd.Series(np.random.randn(5),index=['a1','a2','a3','a4','a5'])
a1    0.025085
a2    0.004182
a3    0.332355
a4    0.755957
a5    0.245630
dtype: float64
>>> d={'A':1,'B':2}
>>> pd.Series(d)
A    1
B    2
dtype: int64
>>> d={'c1':pd.Series(['A','Z']),'c2':pd.Series([1,10])}
>>> df=pd.DataFrame(d)
>>> df
  c1  c2
0  A   1
1  Z  10
>>> e={'c1':['Ana','Zoe'],'c2':[1,10]}
>>> df1=pd.DataFrame(e)
>>> df1
    c1  c2
0  Ana   1
1  Zoe  10
>>> d = {'Item 1': pd.DataFrame(np.random.randn(4, 3)), 'Item 2': pd.DataFrame(np.random.randn(4, 2)) }
>>> d
{'Item 1':           0         1         2
0  1.362449  1.291769 -0.230265
1  0.334886 -0.161012  0.446995
2 -0.832120 -0.390282  0.935351
3 -0.200511  1.028751 -1.699296, 'Item 2':           0         1
0  0.694562 -1.375439
1  0.406256  0.801367
2 -0.609609  1.878070
3 -1.014884 -0.074749}
>>> pd.Panel(d)

Warning (from warnings module):
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\idlelib\run.py", line 474
    exec(code, self.locals)
FutureWarning: 
Panel is deprecated and will be removed in a future version.
The recommended way to represent these types of 3-dimensional data are with a MultiIndex on a DataFrame, via the Panel.to_frame() method
Alternatively, you can use the xarray package http://xarray.pydata.org/en/stable/.
Pandas provides a `.to_xarray()` method to help automate this conversion.

<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 3 (minor_axis)
Items axis: Item 1 to Item 2
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 2
>>> pd.to_xarray(d)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    pd.to_xarray(d)
AttributeError: module 'pandas' has no attribute 'to_xarray'
>>> help(to_xarray())
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    help(to_xarray())
NameError: name 'to_xarray' is not defined
>>> help(to_xarray)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    help(to_xarray)
NameError: name 'to_xarray' is not defined
>>> df.to_xarray()
Traceback (most recent call last):
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 2730, in to_xarray
    import xarray
ModuleNotFoundError: No module named 'xarray'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    df.to_xarray()
  File "C:\Users\Simmi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 2733, in to_xarray
    raise ImportError("the xarray library is not installed\n"
ImportError: the xarray library is not installed
you can install via conda
conda install xarray
or via pip
pip install xarray

>>> pd.d.to_xarray()
		      
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    pd.d.to_xarray()
AttributeError: module 'pandas' has no attribute 'd'
>>> pd.df1.to_xarray()
		      
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    pd.df1.to_xarray()
AttributeError: module 'pandas' has no attribute 'df1'
>>> 
