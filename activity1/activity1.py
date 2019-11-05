Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data = pd.read_csv('D:\R project\Data.csv',parse_dates[0])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data = pd.read_csv('D:\R project\Data.csv',parse_dates[0])
NameError: name 'parse_dates' is not defined
>>> data = pd.read_csv('D:\R project\Data.csv')
>>> data
        Date   Temperature
0   20140101          12.0
1   20140201          16.0
2   20140301          17.0
3   20140401           NaN
4   20140501          13.0
5   20140601          15.0
6   20140701          12.0
7   20140801          11.0
8   20140901           NaN
9   20141001           NaN
10  20141101           NaN
11  20141201          14.0
12  20150101          16.0
13  20150101          16.0
14  20150201          20.0
15  20150301          21.0
16  20150401           NaN
17  20150501           NaN
18  20150601          23.0
19  20150701          42.0
20  20150801          11.0
21  20150901          12.0
22  20151001          13.0
23  20151101          12.0
24  20151201          15.0
>>> fixed=data.fillna(data.mean())
>>> fixed
        Date   Temperature
0   20140101     12.000000
1   20140201     16.000000
2   20140301     17.000000
3   20140401     16.368421
4   20140501     13.000000
5   20140601     15.000000
6   20140701     12.000000
7   20140801     11.000000
8   20140901     16.368421
9   20141001     16.368421
10  20141101     16.368421
11  20141201     14.000000
12  20150101     16.000000
13  20150101     16.000000
14  20150201     20.000000
15  20150301     21.000000
16  20150401     16.368421
17  20150501     16.368421
18  20150601     23.000000
19  20150701     42.000000
20  20150801     11.000000
21  20150901     12.000000
22  20151001     13.000000
23  20151101     12.000000
24  20151201     15.000000
>>> toOut=pd.DataFrame({'Country':pd.Series(['Canada','US','India']),'Capital':pd.Series(['Ottawa','Washington','Delhi'])
			})
>>> toOut
  Country     Capital
0  Canada      Ottawa
1      US  Washington
2   India       Delhi
>>> toOut=toOut[['Country','Capital']]
>>> toOut
  Country     Capital
0  Canada      Ottawa
1      US  Washington
2   India       Delhi
>>> toOutput.to_csv('D:/R project/Output.csv',index=False)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    toOutput.to_csv('D:/R project/Output.csv',index=False)
NameError: name 'toOutput' is not defined
>>> toOut.to_csv('D:/R project/Output.csv',index=False)
>>> 
