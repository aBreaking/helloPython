from datetime import datetime

import tbpy

tbpy.init()
#设定品种周期，从 TBquant 读取历史行情数据
symbols=['rb000.SHFE']
str = tbpy.write_fundamental('wave' , 'rb000.SHFE' ,  datetime(2022, 6, 1, 9, 0, 0),  value=float(100))
print(str)