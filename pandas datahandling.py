Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import panda as pd
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import panda as pd
ModuleNotFoundError: No module named 'panda'
>>> import pandas as pd
>>> import numpy as np
>>> df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
NameError: name 'df' is not defined
>>> dates = pd.date_range('20130101', periods =6)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
>>> DF
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    DF
NameError: name 'DF' is not defined
>>> df
                   A         B         C         D
2013-01-01  0.070158  0.629035  0.199517 -0.157134
2013-01-02 -0.657302 -0.729182  1.550022  0.019288
2013-01-03  0.967422  0.225455  0.893080 -0.548872
2013-01-04  1.220210  0.942492 -0.326450 -0.299600
2013-01-05  0.129915 -1.357146 -1.328980  0.384158
2013-01-06  0.655625  0.283885  1.282089 -1.196663
>>> df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
>>> df1.loc[dates[0]:dates[1],E']=1
	    
SyntaxError: EOL while scanning string literal
>>> df1.loc[dates[0]: dates[1],'E']=1
	    
>>> DF1
	    
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    DF1
NameError: name 'DF1' is not defined
>>> df1
	    
                   A         B         C         D    E
2013-01-01  0.070158  0.629035  0.199517 -0.157134  1.0
2013-01-02 -0.657302 -0.729182  1.550022  0.019288  1.0
2013-01-03  0.967422  0.225455  0.893080 -0.548872  NaN
2013-01-04  1.220210  0.942492 -0.326450 -0.299600  NaN
>>> df1.dropna()
	    
                   A         B         C         D    E
2013-01-01  0.070158  0.629035  0.199517 -0.157134  1.0
2013-01-02 -0.657302 -0.729182  1.550022  0.019288  1.0
>>> df1.fillna()
	    
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    df1.fillna()
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 3790, in fillna
    downcast=downcast, **kwargs)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 5348, in fillna
    value, method = validate_fillna_kwargs(value, method)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\util\_validators.py", line 346, in validate_fillna_kwargs
    raise ValueError("Must specify a fill 'value' or 'method'.")
ValueError: Must specify a fill 'value' or 'method'.
>>> df1.fillna(value=3)
                   A         B         C         D    E
2013-01-01  0.070158  0.629035  0.199517 -0.157134  1.0
2013-01-02 -0.657302 -0.729182  1.550022  0.019288  1.0
2013-01-03  0.967422  0.225455  0.893080 -0.548872  3.0
2013-01-04  1.220210  0.942492 -0.326450 -0.299600  3.0
>>> pd.isna(df1)
                A      B      C      D      E
2013-01-01  False  False  False  False  False
2013-01-02  False  False  False  False  False
2013-01-03  False  False  False  False   True
2013-01-04  False  False  False  False   True
>>> df.mean()
A    0.397671
B   -0.000910
C    0.378213
D   -0.299804
dtype: float64
>>> df.median()
A    0.392770
B    0.254670
C    0.546299
D   -0.228367
dtype: float64
>>> df.sum()
A    2.386028
B   -0.005460
C    2.269278
D   -1.798823
dtype: float64
>>> df.mode()
          A         B         C         D
0 -0.657302 -1.357146 -1.328980 -1.196663
1  0.070158 -0.729182 -0.326450 -0.548872
2  0.129915  0.225455  0.199517 -0.299600
3  0.655625  0.283885  0.893080 -0.157134
4  0.967422  0.629035  1.282089  0.019288
5  1.220210  0.942492  1.550022  0.384158
>>> df.std()
A    0.686972
B    0.870510
C    1.086113
D    0.539698
dtype: float64
>>> df.apply(np.cumsum)
                   A         B         C         D
2013-01-01  0.070158  0.629035  0.199517 -0.157134
2013-01-02 -0.587144 -0.100147  1.749539 -0.137846
2013-01-03  0.380278  0.125308  2.642619 -0.686718
2013-01-04  1.600488  1.067800  2.316169 -0.986318
2013-01-05  1.730403 -0.289345  0.987189 -0.602161
2013-01-06  2.386028 -0.005460  2.269278 -1.798823
>>> df.apply(lambda x: x.max() - x.min())
A    1.877512
B    2.299638
C    2.879002
D    1.580820
dtype: float64
>>> #HISTOGRAMMING
>>> s=pd.Series(np.random.randint(0,7,size=10))
>>> s
0    4
1    4
2    2
3    4
4    1
5    6
6    2
7    2
8    1
9    1
dtype: int32
>>> s.value_counts()
4    3
2    3
1    3
6    1
dtype: int64
>>>  df = pd.DataFrame(np.random.randn(10, 4))
SyntaxError: unexpected indent
>>> df = pd.DataFrame(np.random.randn(10, 4))
>>> df
          0         1         2         3
0  0.084157 -1.101703 -1.707957  0.753288
1  1.405378 -0.425304 -0.063559  0.765215
2 -0.606850 -0.756825  0.954330 -1.167361
3  1.259957  0.829929  0.246907  0.541862
4  0.726531 -1.009214 -0.421701 -1.029575
5 -0.065955  0.068362 -1.770766  1.142800
6 -0.322989  0.075362 -1.828991  1.053472
7 -0.404658  0.134083 -0.711269 -1.139436
8  0.826835 -0.311875  0.702583 -1.542086
9 -0.217703  0.159495 -0.077834 -1.304036
>>> pieces = [df[:3], df[3:7], df[7:]]
>>> pd.concat(pieces)
          0         1         2         3
0  0.084157 -1.101703 -1.707957  0.753288
1  1.405378 -0.425304 -0.063559  0.765215
2 -0.606850 -0.756825  0.954330 -1.167361
3  1.259957  0.829929  0.246907  0.541862
4  0.726531 -1.009214 -0.421701 -1.029575
5 -0.065955  0.068362 -1.770766  1.142800
6 -0.322989  0.075362 -1.828991  1.053472
7 -0.404658  0.134083 -0.711269 -1.139436
8  0.826835 -0.311875  0.702583 -1.542086
9 -0.217703  0.159495 -0.077834 -1.304036
>>> left = pd.DataFrame({'key':['jo', 'ays'],'lval':[1,2]})
>>> right = pd.DataFrame({'key':['jo', 'ays'],'lval':[8,5]})
>>> left
   key  lval
0   jo     1
1  ays     2
>>> right
   key  lval
0   jo     8
1  ays     5
>>> pd.merge(left,right)
Empty DataFrame
Columns: [key, lval]
Index: []
>>> pd.merge(left,right, on= 'key')
   key  lval_x  lval_y
0   jo       1       8
1  ays       2       5
>>> df
          0         1         2         3
0  0.084157 -1.101703 -1.707957  0.753288
1  1.405378 -0.425304 -0.063559  0.765215
2 -0.606850 -0.756825  0.954330 -1.167361
3  1.259957  0.829929  0.246907  0.541862
4  0.726531 -1.009214 -0.421701 -1.029575
5 -0.065955  0.068362 -1.770766  1.142800
6 -0.322989  0.075362 -1.828991  1.053472
7 -0.404658  0.134083 -0.711269 -1.139436
8  0.826835 -0.311875  0.702583 -1.542086
9 -0.217703  0.159495 -0.077834 -1.304036
>>> r=df.iloc[3]
>>> df.append(r)
          0         1         2         3
0  0.084157 -1.101703 -1.707957  0.753288
1  1.405378 -0.425304 -0.063559  0.765215
2 -0.606850 -0.756825  0.954330 -1.167361
3  1.259957  0.829929  0.246907  0.541862
4  0.726531 -1.009214 -0.421701 -1.029575
5 -0.065955  0.068362 -1.770766  1.142800
6 -0.322989  0.075362 -1.828991  1.053472
7 -0.404658  0.134083 -0.711269 -1.139436
8  0.826835 -0.311875  0.702583 -1.542086
9 -0.217703  0.159495 -0.077834 -1.304036
3  1.259957  0.829929  0.246907  0.541862
>>> df.append(r, index=10)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    df.append(r, index=10)
TypeError: append() got an unexpected keyword argument 'index'
>>> df.append(r, ignore_index=True)
           0         1         2         3
0   0.084157 -1.101703 -1.707957  0.753288
1   1.405378 -0.425304 -0.063559  0.765215
2  -0.606850 -0.756825  0.954330 -1.167361
3   1.259957  0.829929  0.246907  0.541862
4   0.726531 -1.009214 -0.421701 -1.029575
5  -0.065955  0.068362 -1.770766  1.142800
6  -0.322989  0.075362 -1.828991  1.053472
7  -0.404658  0.134083 -0.711269 -1.139436
8   0.826835 -0.311875  0.702583 -1.542086
9  -0.217703  0.159495 -0.077834 -1.304036
10  1.259957  0.829929  0.246907  0.541862
>>> 
