import time
from datetime import datetime, timedelta

# epoch time
print(time.time())


def send_emails():
    for i in range(1000000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

duration = dt2 - dt1
print(duration)
