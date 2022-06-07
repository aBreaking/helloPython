import datetime

import tbpy

tbpy.init()

symbols=['rb000.SHFE']
freq='1d'
begintime=datetime.datetime.strptime('20220505','%Y%m%d')
endtime=datetime.datetime.strptime('20220512','%Y%m%d')
bars=tbpy.get_history(symbols, freq,begintime, endtime, fields=None, timeout='30s')
print(bars)