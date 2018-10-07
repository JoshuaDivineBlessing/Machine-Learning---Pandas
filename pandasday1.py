Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> s = pd.Series([5,6,9,kl,np.nan,9])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s = pd.Series([5,6,9,kl,np.nan,9])
NameError: name 'kl' is not defined
>>> s = pd. Series([56,12,5,0,3,np.nan,8])
>>> s
0    56.0
1    12.0
2     5.0
3     0.0
4     3.0
5     NaN
6     8.0
dtype: float64
>>> #2) CREATING A DATA FRAME
>>> # COMBINATION OF SERIES IS CALLED A DATA FRAME
>>> dates = pd.data_range('20140101, periods = 8)
			  
SyntaxError: EOL while scanning string literal
>>> dates = pd. date_range('20140101', periods = 6)
			  
>>> dates
			  
DatetimeIndex(['2014-01-01', '2014-01-02', '2014-01-03', '2014-01-04',
               '2014-01-05', '2014-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df = pd.DataFrame(np.random.randn(2,5), index = dates, columns = list('ABCD'))
			  
Traceback (most recent call last):
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4857, in create_block_manager_from_blocks
    placement=slice(0, len(axes[0])))]
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 3205, in make_block
    return klass(values, ndim=ndim, placement=placement)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 125, in __init__
    '{mgr}'.format(val=len(self.values), mgr=len(self.mgr_locs)))
ValueError: Wrong number of items passed 5, placement implies 4

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    df = pd.DataFrame(np.random.randn(2,5), index = dates, columns = list('ABCD'))
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 379, in __init__
    copy=copy)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 536, in _init_ndarray
    return create_block_manager_from_blocks([values], [columns, index])
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4866, in create_block_manager_from_blocks
    construction_error(tot_items, blocks[0].shape[1:], axes, e)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 4843, in construction_error
    passed, implied))
ValueError: Shape of passed values is (5, 2), indices imply (4, 6)
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
>>> df
                   A         B         C         D
2014-01-01  0.289690  0.024699  0.352224  1.443128
2014-01-02 -0.507296 -1.509986  0.390431  0.968050
2014-01-03 -0.296770  1.224124  1.474235 -0.113319
2014-01-04  0.673861 -1.906934  1.270933  1.883875
2014-01-05  0.024384 -0.531412 -1.463297 -0.375779
2014-01-06 -0.704239  0.219949  0.027592  0.610664
>>> s = pd.Timestamp('20180105')
>>> s
Timestamp('2018-01-05 00:00:00')
>>> s
Timestamp('2018-01-05 00:00:00')
>>> df.<TAB>
SyntaxError: invalid syntax
>>> df. head()
                   A         B         C         D
2014-01-01  0.289690  0.024699  0.352224  1.443128
2014-01-02 -0.507296 -1.509986  0.390431  0.968050
2014-01-03 -0.296770  1.224124  1.474235 -0.113319
2014-01-04  0.673861 -1.906934  1.270933  1.883875
2014-01-05  0.024384 -0.531412 -1.463297 -0.375779
>>> df.head(2)
                   A         B         C         D
2014-01-01  0.289690  0.024699  0.352224  1.443128
2014-01-02 -0.507296 -1.509986  0.390431  0.968050
>>> df.tail(2)
                   A         B         C         D
2014-01-05  0.024384 -0.531412 -1.463297 -0.375779
2014-01-06 -0.704239  0.219949  0.027592  0.610664
>>> df.index
DatetimeIndex(['2014-01-01', '2014-01-02', '2014-01-03', '2014-01-04',
               '2014-01-05', '2014-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df.columns
Index(['A', 'B', 'C', 'D'], dtype='object')
>>> df.values
array([[ 0.28969042,  0.02469931,  0.3522243 ,  1.44312752],
       [-0.50729576, -1.50998564,  0.39043092,  0.96805045],
       [-0.29676963,  1.22412392,  1.47423504, -0.1133186 ],
       [ 0.67386091, -1.90693373,  1.27093292,  1.88387461],
       [ 0.02438365, -0.5314116 , -1.46329677, -0.37577878],
       [-0.70423921,  0.219949  ,  0.02759209,  0.61066447]])
>>> df.describe()
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean  -0.086728 -0.413260  0.342020  0.736103
std    0.516691  1.159450  1.049311  0.876880
min   -0.704239 -1.906934 -1.463297 -0.375779
25%   -0.454664 -1.265342  0.108750  0.067677
50%   -0.136193 -0.253356  0.371328  0.789357
75%    0.223364  0.171137  1.050807  1.324358
max    0.673861  1.224124  1.474235  1.883875
>>> #transposing
>>> df.T
   2014-01-01  2014-01-02     ...      2014-01-05  2014-01-06
A    0.289690   -0.507296     ...        0.024384   -0.704239
B    0.024699   -1.509986     ...       -0.531412    0.219949
C    0.352224    0.390431     ...       -1.463297    0.027592
D    1.443128    0.968050     ...       -0.375779    0.610664

[4 rows x 6 columns]
>>> df.sort_index
<bound method DataFrame.sort_index of                    A         B         C         D
2014-01-01  0.289690  0.024699  0.352224  1.443128
2014-01-02 -0.507296 -1.509986  0.390431  0.968050
2014-01-03 -0.296770  1.224124  1.474235 -0.113319
2014-01-04  0.673861 -1.906934  1.270933  1.883875
2014-01-05  0.024384 -0.531412 -1.463297 -0.375779
2014-01-06 -0.704239  0.219949  0.027592  0.610664>
>>> df.sort_index(axis=1, ascending = False)
                   D         C         B         A
2014-01-01  1.443128  0.352224  0.024699  0.289690
2014-01-02  0.968050  0.390431 -1.509986 -0.507296
2014-01-03 -0.113319  1.474235  1.224124 -0.296770
2014-01-04  1.883875  1.270933 -1.906934  0.673861
2014-01-05 -0.375779 -1.463297 -0.531412  0.024384
2014-01-06  0.610664  0.027592  0.219949 -0.704239
>>> df.sort_values(by='A','B')
SyntaxError: positional argument follows keyword argument
>>> df.sort_values(by='AB')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    df.sort_values(by='AB')
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 4421, in sort_values
    stacklevel=stacklevel)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 1382, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'AB'
>>> df.sort_values(by='A')
                   A         B         C         D
2014-01-06 -0.704239  0.219949  0.027592  0.610664
2014-01-02 -0.507296 -1.509986  0.390431  0.968050
2014-01-03 -0.296770  1.224124  1.474235 -0.113319
2014-01-05  0.024384 -0.531412 -1.463297 -0.375779
2014-01-01  0.289690  0.024699  0.352224  1.443128
2014-01-04  0.673861 -1.906934  1.270933  1.883875
>>> 
