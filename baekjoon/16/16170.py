# 오늘의 날짜는?

import time

t = time.gmtime()              # UTC 기준
print(time.strftime("%Y", t))
print(time.strftime("%m", t))
print(time.strftime("%d", t))