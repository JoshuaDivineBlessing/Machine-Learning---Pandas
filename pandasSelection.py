Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> dates = pd.date_range('20130102', periods=6)
>>> dates
DatetimeIndex(['2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05',
               '2013-01-06', '2013-01-07'],
              dtype='datetime64[ns]', freq='D')
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns(list('AJCP))
								      
SyntaxError: EOL while scanning string literal
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns(list('AJCP'))
		      df
		      
SyntaxError: invalid syntax
>>> df
		      
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    df
NameError: name 'df' is not defined
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('AJCP'))
		      
>>> df
		      
                   A         J         C         P
2013-01-02 -2.476570  0.240185  2.625547  0.838647
2013-01-03  0.130084  0.734255  1.329862 -0.865932
2013-01-04  0.651805  1.426528 -1.195455  0.266781
2013-01-05  0.255188 -1.840815 -0.591340 -1.956884
2013-01-06 -0.719760  0.093481  1.567523 -0.424086
2013-01-07 -0.713884  1.442737 -0.084102 -0.217524
>>> 

>>> df['J']
		      
2013-01-02    0.240185
2013-01-03    0.734255
2013-01-04    1.426528
2013-01-05   -1.840815
2013-01-06    0.093481
2013-01-07    1.442737
Freq: D, Name: J, dtype: float64
>>> df[0:2]
		      
                   A         J         C         P
2013-01-02 -2.476570  0.240185  2.625547  0.838647
2013-01-03  0.130084  0.734255  1.329862 -0.865932
>>> df.J
		      
2013-01-02    0.240185
2013-01-03    0.734255
2013-01-04    1.426528
2013-01-05   -1.840815
2013-01-06    0.093481
2013-01-07    1.442737
Freq: D, Name: J, dtype: float64
>>> df.loc[dates[0]]
		      
A   -2.476570
J    0.240185
C    2.625547
P    0.838647
Name: 2013-01-02 00:00:00, dtype: float64
>>> df.loc[dates[2]]
		      
A    0.651805
J    1.426528
C   -1.195455
P    0.266781
Name: 2013-01-04 00:00:00, dtype: float64
>>> df.loc[dates[0],'A']
		      
-2.4765696294470145
>>> df.iloc
		      
<pandas.core.indexing._iLocIndexer object at 0x092A3450>
>>> df.loc(help)
		      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    df.loc(help)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexing.py", line 98, in __call__
    axis = self.obj._get_axis_number(axis)
  File "C:\Users\Joshua\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 375, in _get_axis_number
    .format(axis, type(self)))
ValueError: No axis named Type help() for interactive help, or help(object) for help about object. for object type <class 'pandas.core.frame.DataFrame'>
>>> df.iloc[1]
								      
A    0.130084
J    0.734255
C    1.329862
P   -0.865932
Name: 2013-01-03 00:00:00, dtype: float64
>>> df.iloc[:,1:3]
								      
                   J         C
2013-01-02  0.240185  2.625547
2013-01-03  0.734255  1.329862
2013-01-04  1.426528 -1.195455
2013-01-05 -1.840815 -0.591340
2013-01-06  0.093481  1.567523
2013-01-07  1.442737 -0.084102
>>> 
